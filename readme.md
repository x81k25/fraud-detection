## Fraud Detection

### Table of Contents

1. Project Overview
2. Installation
3. Usage
4. Notebooks
5. License

### 1. Project Overview

This project consists of a series of notebooks containing different modeling methods for this dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download

The models are compared and finally recommendations are given on which model I belive would the best to sovle this problem.

#### Project Structure
- data/: Directory containing the dataset.
    - the creditcard data file contained in the data folder is an optimized version of the original .csv
    - the data types of objects were specified and it was stored as a parquet file
    - this will have no impact on the data presented in the notebooks, but it shaves ~66% off of the orignal file size and properly preserves data with out having to perform any additional operations other than reading the dataset in
- notebooks/: Directory containing Jupyter notebooks for data exploration, model training, and evaluation.
- scripts/: conatains any python scripts used
- README.md: This file.
- requirements.txt: List of required Python packages.

### 2. Installation

- Clone the repository

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

- Create and activate a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

- Install the required packages


```sh
pip install -r requirements.txt
```

### 3. Usage

- The jupyter notebooks can be run via the command below via the appropriate shell, or with an IDE that supports .ipynb .

```sh
jupyter notebook
```

- The notebooks are intended to run sequenially, in the order listed below; however, they will function in any order you choose.

### 4. Notebooks

This project includes several Jupyter notebooks that showcase different aspects of the project and can be used for analysis or exploration. All of them are contained with the ./notebooks/ directory.

1. 01-data-discovery
    - a quantitative and visual examination of the input data set
    - explores the overall quality of the data 
    - looks at stastical measures of each fields
    - provides relevant visualization, especially of the fields distributions 
2. 02-feature-engineering
    - generates additional features to be used for the classifaction models
3. 03-classification
    - uses a series of different classification models to experiment with which is the most performant 
    - discusses which metrics will be most relevant for this analysis
    - outputs and visualizes relevant metrics to dispaly a comparison of the different models used

### 5. License

This project is licensed under the [License name] License. Please see the LICENSE file for details.