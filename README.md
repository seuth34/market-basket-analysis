# Smart Market Basket Analysis

## Project Overview
This project uses PySpark FP-Growth algorithm
to analyze customer purchasing behavior
from the Instacart Market Basket Analysis dataset.

## Technologies
- Python
- PySpark
- Streamlit
- FP-Growth
- Kaggle API

## Pipeline
1. Data Ingestion
2. Data Processing
3. Association Rule Mining
4. Dashboard Visualization

## Run Project

### Install
```bash
pip install -r requirements.txt
```

### Ingestion
```bash
python src/ingestion_kaggle.py
```

### Processing
```bash
python src/preprocess.py
```

### Train FP-Growth
```bash
python src/train_fp_growth.py
```

### Dashboard
```bash
streamlit run src/dashboard.py
```
### Open project on CMD
cd market-basket-analysis
venv\Scripts\activate