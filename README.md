# HLT-Project
## Detecting Dietary Restrictions in Recipes
This project aims to develop a classification system  designed to identify and categorize recipes based on specific dietary labels. These labels include whether a recipe is Vegetarian, Dairy Free, Gluten Free, Low Carb, Low Fat, and Low Sodium.

We worked on the [Food Recipe Dataset](https://www.kaggle.com/datasets/snehallokesh31096/recipe/data) available on Kaggle.

### Requirements
```cmd
pip install -r requirements.txt
```

### Repository Structure

```
./
├── 📂 project
│   ├── 📄 data_understanding.ipynb
│   ├── 📄 NER.ipynb
│   ├── 📄 classification_standard_ml.ipynb
│   ├── 📄 static_embeddings_classification.ipynb
│   ├── 📄 RNNs.ipynb
│   ├── 📄 finetuning_veg.ipynb
│   ├── 📄 finetuning_multi.ipynb
│   ├── 📄 requirements.txt
│   └── 📂 utils
│       ├── 📄 macro_tags.py
│       └── ...
│   └── 📂 old_notebooks
│   └── 📂 dataset
│       ├── 📄 dataset.csv
│       └── ...
│   └── 📂 models
│       ├── 📂 bert_model1
│       └── ...
├── 📄 README.md
└── 📄 .gitignore
```

### Project Overview

- `data_understanding.ipynb`: all the cells required to obtain the datasets needed for the rest of the project, and some data analysis.
- `NER.ipynb`: extraction of the ingredients and cleaning with spaCy and Stanza.
- `classification_standard_ml.ipynb`: experiments with RF, MLP, SVM with one-hot encoding.
- `static_embeddings_classification.ipynb`: experiments with RF, MLP, SVM, LogReg with Word2Vec.
- `RNNs.ipynb`: experiments with RNN architectures.
- `finetuning_veg.ipynb`: finetuning of BERT for the single-label task.
- `finetuning_multi.ipynb`: finetuning of BERT for the multi-label task.

The notebooks can be run in the listed order to replicate the experiments.

The [report](https://github.com/lavo2/HLT-Project/blob/main/Report_Group15.pdf) contains the description of the project, with the results of the most significant experiments, and bibliographic references.
  

### Contributors

- [Irene Dovichi](https://github.com/irenedovichi)
- [Marco Lavorini](https://github.com/lavo2)
- [Alice Nicoletta](https://github.com/AliceNi99)
- [Nicola Pitzalis](https://github.com/nicolapitzalis)



