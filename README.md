# SUS Group Project

Group project for Structured and Unstructured Data course

## Contribution Guidelines

These are the guidelines that project members will adhere to when contributing
to the project.

### Version Control

1. All changes will be made in a branch off of the `main` branch
1. Commit atomically (commit small changes to one or a few files at a time)
1. Commit messages should be descriptive and concise
1. Make a PR to merge your branch into `main` when you are ready to merge
1. Each PR shall be reviewed by one other team member before merging
1. Code reviews will be conducted through the GitHub interface

### Coding Standards

1. Document code using appropriate comments and meaningful names

### Documentation

1. Maintain a README file for major directories with explanations and
instructions for future contributions

## Installation

1. Clone the repository

```bash
git clone https://github.com/CWRU-SUSD-Group-Project/sus-data-science.git
```

2. Change your working directory to the project root

```bash
cd sus-data-science
```

3. Set up git filters

```bash
git config filter.strip-notebook-output-metadata.clean "python -m jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --ClearMetadataPreprocessor.preserve_nb_metadata_mask kernelspec --ClearMetadataPreprocessor.preserve_nb_metadata_mask name --to=notebook --stdin --stdout --log-level=ERROR"
git config filter.strip-notebook-output-metadata.smudge "cat"
```

4. Set up the virtual environment

For Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

For Windows:

```bash
python -m venv .venv
Set-ExecutionPolicy Unrestricted -Scope Process
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

5. Download data from Google Drive (see DATA folder) and move it into `data/00_original/`

## Running the Project

1. Activate the virtual environment

```bash
source .venv/bin/activate
```

2. Open Jupyter Lab

```bash
jupyter lab
```

3. Open the notebook

4. Run the notebook
