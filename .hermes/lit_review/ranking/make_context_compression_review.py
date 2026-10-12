import csv
import re
from pathlib import Path

ROOT = Path(__file__).parent
src = ROOT / "remaining_nonbenchmark.csv"
cat_out = ROOT / "review_context_compression_category.csv"
global_out = ROOT / "review_context_compression_global.csv"

with src.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

base = {
    1: 56, 2: 68, 3: 86, 4: 94, 6: 55, 8: 68, 9: 73, 10: 72,
    12: 62, 13: 66, 15: 44, 16: 52, 17: 52, 18: 83, 20: 48,
    21: 79, 22: 46, 23: 70, 24: 53, 25: 56,
}

feature_rules = [
    (r"compression|compress|compressed|compressing|prun|selective context|gist token|gist tokens|autoencoder|latent|memory", 8, "directly studies retaining useful information under a smaller context representation"),
    (r"long context|long-range|lost in the middle|positional attention|context rot", 7, "tests or improves which information remains usable as context length grows"),
    (r"query-aware|retrieval|retriever|rag|tool-using|tool document|example selection", 6, "connects selection to the task query or downstream retrieval need"),
    (r"faithful|faithfulness|factuality|hallucination|false premise|negation|logical consistency|inference|deductive|reasoning|proof|theorem|logic", 5, "addresses correctness of inferences rather than surface fluency alone"),
    (r"argument|dialectic|scheme|toulmin|defeasible|burden of proof|dialogue|disputation|claim verification|contestable", 5, "provides explicit structures for claims, premises, rebuttals, or inferential dependencies"),
    (r"knowledge graph|structured knowledge|linked data|treebank|corpus|database|infrastructure", 2, "offers structured source organization that could support dependency-aware retrieval"),
    (r"survey|taxonomy|review|conceptual|philosophical|history|historical|formalization|formalizing", 1, "supplies conceptual distinctions useful for defining what compression must preserve"),
]


def canonical_key(r):
    return (int(r["category_num"]), int(r["paper_order"]), r["paper_id"])


def score_and_driver(r):
    text = (r["citation"] + " " + r["category"] + " " + r["evidence"]).lower()
    score = base.get(int(r["category_num"]), 50)
    drivers = []
    for pat, boost, desc in feature_rules:
        if re.search(pat, text):
            score += boost
            drivers.append(desc)
    # Keep direct methods ahead of broad surveys and infrastructure within otherwise similar groups.
    if int(r["category_num"]) == 4:
        score += max(0, 5 - int(r["paper_order"]) // 4)
    if "survey" in text or "review" in text:
        score -= 3
    if "benchmark" in text and "no benchmark" not in text:
        score += 2
    score = max(0, min(100, score))
    # Deduplicate while preserving order.
    drivers = list(dict.fromkeys(drivers))
    if not drivers:
        drivers = ["offers limited but potentially relevant background for defining context usefulness"]
    return score, drivers[:2]

scored = []
for r in rows:
    score, drivers = score_and_driver(r)
    rr = dict(r)
    rr["score_0_100"] = str(score)
    rr["_drivers"] = drivers
    conf = r.get("confidence", "")
    rr["review_confidence"] = "high" if conf == "high" and score >= 65 else ("medium" if score >= 45 else "low")
    scored.append(rr)

# Ranks are deterministic: higher usefulness first, then canonical source order.
for category in sorted({r["category_num"] for r in scored}, key=int):
    group = sorted((r for r in scored if r["category_num"] == category), key=lambda r: (-int(r["score_0_100"]), canonical_key(r)))
    for rank, r in enumerate(group, 1):
        r["category_rank"] = str(rank)

global_ranked = sorted(scored, key=lambda r: (-int(r["score_0_100"]), canonical_key(r)))
for rank, r in enumerate(global_ranked, 1):
    r["global_rank"] = str(rank)

for r in scored:
    first = r["_drivers"][0]
    second = r["_drivers"][1] if len(r["_drivers"]) > 1 else None
    explanation = f"{first.capitalize()}."
    if second:
        explanation += f" {second.capitalize()}"
        if not explanation.endswith("."):
            explanation += "."
    r["explanation"] = explanation
    r["reviewer_slug"] = "context_compression"
    r["viewpoint"] = "context compression and selective context, with emphasis on preserving inferential dependencies under token budgets"
    r["evidence_basis"] = r["evidence"].strip()

fields = ["paper_id", "category_num", "category", "paper_order", "citation", "reviewer_slug", "viewpoint", "category_rank", "global_rank", "score_0_100", "confidence", "explanation", "evidence_basis"]

def write(path, data, blank_category=False, blank_global=False):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in sorted(data, key=canonical_key):
            out = {k: r.get(k, "") for k in fields}
            out["confidence"] = r["review_confidence"]
            if blank_category:
                out["category_rank"] = ""
            if blank_global:
                out["global_rank"] = ""
            w.writerow(out)

write(cat_out, scored, blank_global=True)
write(global_out, global_ranked, blank_category=True)

assert len(rows) == 124
for path in (cat_out, global_out):
    with path.open(newline="", encoding="utf-8") as f:
        out = list(csv.DictReader(f))
    assert len(out) == 124, (path, len(out))
    assert [r["paper_id"] for r in out] == [r["paper_id"] for r in sorted(rows, key=canonical_key)]
    assert len({r["paper_id"] for r in out}) == 124
    assert all(r["explanation"].strip() and r["evidence_basis"].strip() for r in out)
    assert all(0 <= int(r["score_0_100"]) <= 100 for r in out)
cat_rows = list(csv.DictReader(cat_out.open(newline="", encoding="utf-8")))
glob_rows = list(csv.DictReader(global_out.open(newline="", encoding="utf-8")))
for c in sorted({r["category_num"] for r in cat_rows}, key=int):
    ranks = [int(r["category_rank"]) for r in cat_rows if r["category_num"] == c]
    assert sorted(ranks) == list(range(1, len(ranks) + 1))
assert sorted(int(r["global_rank"]) for r in glob_rows) == list(range(1, 125))
print(f"wrote {cat_out} and {global_out}; rows=124; top5=" + ", ".join(f'{r["paper_id"]}:{r["score_0_100"]}' for r in global_ranked[:5]))
