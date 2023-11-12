# sus-data-science
Group project for Structured and Unstructured Data course

## Installation

1. Clone the repository

```bash
git clone https://github.com/CWRU-SUSD-Group-Project/sus-data-science.git
```

1. Run the installation script

```bash
bash install.sh
```

1. Download data from Google Drive (see DATA folder) and move it into `data/`

## Running the Project

1. Update the virtual environment

```bash
bash scripts/update.sh
```

1. Activate the virtual environment

```bash
source .venv/bin/activate
```

1. Open Jupyter Lab

```bash
jupyter lab
```

1. Open the notebook

1. Run the notebook

## Managing the Environemtn

The files in `scripts/` are used to manage the virtual environment. They can be
run in the following manner.

```bash
bash scripts/<script-name>.sh
```

- `reinstall-venv.sh` is used to reinstall the virtual environment
- `update-requirements.sh` is used to update the `requirements.txt` file
- `update.sh` is used install/update the packages in `requirements.txt`
