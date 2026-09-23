---
license: mit
language:
- fr
annotations_creators:
- expert-generated
size_categories:
- n<3k
source_datasets:
- Grand Débat National
task_categories:
- text-classification
- text-generation
configs:  # Optional. This can be used to pass additional parameters to the dataset loader, such as `data_files`, `data_dir`, and any builder-specific parameters  
- config_name: default  # Name of the dataset subset, if applicable. Example: default
  data_files:
  - split: train  # Example: train
    path: GDNCC_data_train.jsonl  # Example: data.csv
  - split: test # Example: test
    path: GDNCC_data_test.jsonl   # Example: holdout.csv
  - split: eval # Example: test
    path: GDNCC_data_valid.jsonl   # Example: holdout.csv
- config_name: AU_detection  # Name of the dataset subset. Example: processed
  data_files:
  - split: train  # Example: train
    path: GDNCC_AU_detection_train.jsonl  # Example: data.csv
  - split: test # Example: test
    path: GDNCC_AU_detection_test.jsonl   # Example: holdout.csv
  - split: eval # Example: test
    path: GDNCC_AU_detection_valid.jsonl   # Example: holdout.csv
  - split: corpus  # Example: train
    path: GDNCC_AU_detection.jsonl  # Example: data.csv
---

# Dataset Card for GDN-CC

GDN-CC, short for **Grand Debat National - Corpus Clarification** is a manually annotated dataset for the task of **Corpus Clarification**, introduced in *The GDN-CC Dataset: Automatic Corpus Clarification for AI-enhanced
Democratic Citizen Consultations, Lequeu et al. 2026*. The Corpus Clarification task is preprocessing framework for large-scale consultation data that transforms noisy, multi-topic contributions into structured, self-contained argumentative units ready for downstream analysis.
It is comprised of a three-task pipeline: Argumentative Unit Extraction, Argumentative Structure detection and Argumentaticz Unit Segmentation. 

This process was applied to 1231 contribution to the French citizen consultations "**Grand Debat National**", making up 2285 unique argumentative units. 
splits are provided for comparisons with the original work.


## Citation 
<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

```bibtex
@inproceedings{lequeu-etal-2026-gdn,
    title = "The {GDN}-{CC} Dataset: Automatic Corpus Clarification for {AI}-enhanced Democratic Citizen Consultations",
    author = {Lequeu, Pierre-Antoine  and
      Labat, L{\'e}o  and
      Cave, Laur{\`e}ne  and
      Lejeune, Ga{\"e}l  and
      Yvon, Fran{\c{c}}ois  and
      Piwowarski, Benjamin},
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.1523/",
    doi = "10.18653/v1/2026.acl-long.1523",
    pages = "32976--33006",
    ISBN = "979-8-89176-390-6",
    abstract = "LLMs are ubiquitous in modern NLP, and while their applicability extends to texts produced for democratic activities such as online deliberations or large-scale citizen consultations, ethical questions have been raised for their usage as analysis tools. We continue this line of research with two main goals: (a) to develop resources that can help standardize citizen contributions in public forums at the \textbf{pragmatic level}, and make them easier to use in topic modeling and political analysis; (b) to study how well this standardization can reliably be performed by small, open-weights LLMs, \textit{i.e.} models that can be run locally and transparently with limited resources. Accordingly, we introduce \textbf{Corpus Clarification} as a preprocessing framework for large-scale consultation data that transforms noisy, multi-topic contributions into structured, self-contained argumentative units ready for downstream analysis. We present \textbf{GDN-CC}, a manually-curated dataset of 1,231 contributions to the French \textit{Grand D{\'e}bat National}, comprising 2,285 argumentative units annotated for argumentative structure and manually clarified. We then show that finetuned Small Language Models match or outperform LLMs on reproducing these annotations, and measure their usability for an opinion clustering task. We finally release \textbf{GDN-CC-large}, an automatically annotated corpus of 240k contributions, the largest annotated democratic consultation dataset to date."
}
``` 


