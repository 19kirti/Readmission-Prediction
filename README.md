# Heart Failure Readmission Prediction

## Project Overview
This project aims to predict 30-day readmission risk for heart failure patients using the MIMIC-III dataset. Early identification of high-risk patients can enable targeted interventions to reduce readmissions and improve patient outcomes.

## Dataset
The project uses the MIMIC-III clinical database containing:
- Patient demographics
- Laboratory results
- Diagnosis codes
- Procedure codes
- Admission details

## Project Structure
```
READMISSION PREDICTION FOR HEART FAILURE/
├── datasets/              # Raw and processed data
├── notebooks/            # Jupyter notebooks for analysis
├── models/              # Trained models and results
├── src/                 # Utility functions
├── config/              # Configuration files
└── requirements.txt     # Python dependencies
```

## Methodology
1. **Data Exploration**: Understand data distribution and quality
2. **Data Preprocessing**: Handle missing values, outliers, and feature engineering
3. **Feature Selection**: Identify most predictive features
4. **Model Training**: Train multiple ML models with hyperparameter tuning
5. **Model Evaluation**: Comprehensive performance assessment

## Key Features
- Demographic information (age, gender, ethnicity)
- Clinical measurements (lab results, vital signs)
- Hospitalization details (length of stay, admission type)
- Medical procedures and diagnoses

## Models Implemented
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run notebooks in sequence (01 to 05)
3. Check model performance in the models directory

## Results
The best model achieves [ROC-AUC] on the test set, enabling identification of high-risk patients for targeted interventions.


## Running the Project

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run notebooks in order:**
   - `01_data_exploration.ipynb`
   - `02_data_preprocessing.ipynb`
   - `03_feature_engineering.ipynb`
   - `04_model_training.ipynb`
   - `05_model_evaluation.ipynb`

3. **Check results:**
   - Model performance metrics in `models/` directory
   - Feature importance plots
   - Business impact analysis
