# sus-data-science
Group project for Structured and Unstructured Data course

## Installation

1. Clone the repository

```bash
git clone https://github.com/CWRU-SUSD-Group-Project/sus-data-science.git
```

2. Run the installation script

```bash
bash install.sh
```

3. Create the virtual environment

```bash
bash reinstall-venv.sh
```

4. Download data from Google Drive (see DATA folder) and move it into `data/`

## Running the Project

1. Update the virtual environment

```bash
bash scripts/update.sh
```

2. Activate the virtual environment

```bash
source .venv/bin/activate
```

3. Open Jupyter Lab

```bash
jupyter lab
```

4. Open the notebook

5. Run the notebook

## Managing the Environment

The files in `scripts/` are used to manage the virtual environment. They can be
run in the following manner.

```bash
bash scripts/<script-name>.sh
```

- `reinstall-venv.sh` is used to reinstall the virtual environment
- `update-requirements.sh` is used to update the `requirements.txt` file
- `update.sh` is used install/update the packages in `requirements.txt`
