from pathlib import Path
import re
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).parent
SUMMARY_DIR = ROOT / "summaries"
OUTPUT = ROOT / "all_individual_paper_summaries.pdf"

files = sorted(
    SUMMARY_DIR.glob("*_summaries.md"),
    key=lambda p: int(re.match(r"(\d+)_", p.name).group(1)),
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], alignment=TA_CENTER,
    fontSize=20, leading=25, spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="CoverBody", parent=styles["BodyText"], alignment=TA_CENTER,
    fontSize=11, leading=15, textColor="#444444",
))
styles.add(ParagraphStyle(
    name="Topic", parent=styles["Heading1"], fontSize=15, leading=19,
    spaceBefore=10, spaceAfter=10, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="Paper", parent=styles["Heading2"], fontSize=11.5, leading=14,
    spaceBefore=8, spaceAfter=5, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="Summary", parent=styles["BodyText"], fontSize=9.2, leading=12.5,
    spaceAfter=7, alignment=0,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontSize=8.5, leading=11,
    textColor="#555555",
))


def inline_markup(text: str) -> str:
    text = text.strip()
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return text


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColorRGB(0.4, 0.4, 0.4)
    canvas.drawRightString(letter[0] - 0.55 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()

story = [
    Spacer(1, 1.2 * inch),
    Paragraph("Literature Review", styles["CoverTitle"]),
    Paragraph("Individual Paper Summaries", styles["CoverTitle"]),
    Spacer(1, 0.2 * inch),
    Paragraph(
        f"{len(files)} subject areas; one paragraph summary for each retained paper.",
        styles["CoverBody"],
    ),
    Spacer(1, 0.15 * inch),
    Paragraph("Generated from the scholarly literature-review artifacts.", styles["CoverBody"]),
    PageBreak(),
]

for path in files:
    subject = path.stem.replace("_summaries", "").replace("_", " ").title()
    story.append(Paragraph(inline_markup(subject), styles["Topic"]))
    raw = path.read_text(errors="replace")
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline_markup(line[3:]), styles["Paper"]))
        elif line.startswith("### "):
            story.append(Paragraph(inline_markup(line[4:]), styles["Paper"]))
        elif line.startswith("- ") or line.startswith("* "):
            story.append(Paragraph("• " + inline_markup(line[2:]), styles["Summary"]))
        elif line.startswith("|") or line.startswith("---"):
            continue
        else:
            story.append(Paragraph(inline_markup(line), styles["Summary"]))
    story.append(PageBreak())


doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=letter,
    rightMargin=0.62 * inch, leftMargin=0.62 * inch,
    topMargin=0.62 * inch, bottomMargin=0.55 * inch,
    title="Literature Review — Individual Paper Summaries",
    author="Hermes",
)
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes; {len(files)} source files)")
