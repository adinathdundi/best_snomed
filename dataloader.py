import pandas as pd
from pathlib import Path

# Base directory
DATA_DIR = Path("data")


def load_csv(file_name: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    file_path = file_name
    return pd.read_csv(file_path)


# Preload common datasets
admission_df = load_csv("admissions.csv")
cpt_events_df = load_csv("cptevents.csv")
labtest_df = load_csv("labevents.csv")
prescription_df = load_csv("prescriptions.csv")
gender_df = load_csv("gender.csv")
