# Configuration file for the project

# Data paths
DATA_PATHS = {
    'admissions': '../datasets/admissions_202208161605.csv',
    'patients': '../datasets/patients_202208161605.csv',
    'diagnoses_icd': '../datasets/diagnoses_icd_202208161605.csv',
    'labevents': '../datasets/labevents_202208161605.csv',
    'd_labitems': '../datasets/d_labitems_202208161605.csv',
    'procedures_icd': '../datasets/procedures_icd_202208161605.csv',
    'cptevents': '../datasets/cptevents_202208161605.csv',
    'drgcodes': '../datasets/drgcodes_202208161605.csv'
}

# Heart failure ICD codes
HEART_FAILURE_CODES = [
    '39891','40201','40211','40291','40401','40403','40411','40413',
    '40491','40493','4280','4281','42820','42821','42822','42823',
    '42830','42831','42832','42833','42840','42841','42842','42843','4289'
]

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_FOLDS = 5