import pandas as pd
from datetime import datetime
from io import StringIO


def duration_elapsed(t1: str, t2: str, fmt: str = "%Y-%m-%d %H:%M:%S"):
    """Return the time difference t2 - t1."""
    start = datetime.strptime(t1, fmt)
    end = datetime.strptime(t2, fmt)
    return end - start


def calculate_age(dob: str, admission_time: str) -> str:
    """Calculate age in years from DOB to admission time."""
    delta = duration_elapsed(dob, admission_time)
    years = delta.days // 365
    return f"{years} years"


def fetch_snomed_candidates(icd: str) -> pd.DataFrame:
    """
    Fetch SNOMED codes for a given ICD code.

    Args:
        icd (str): The ICD code to search for.
        snomed_file (str): Path to the SNOMED mapping file.

    Returns:
        (pd.DataFrame, str): DataFrame with SNOMED candidates and ICD name
    """
    with open('data\ICD9CM_SNOMED_MAP_1TOM_202412.txt', "r") as file:
        content = file.read()
    
    df = pd.read_csv(StringIO(content), sep="\t")
    df['ICD_CODE'] = df['ICD_CODE'].str.replace(".", "")

    snomed_lst = [f"{int(cid):d}" for cid in df[df['ICD_CODE'] == icd]['SNOMED_CID'].tolist()]
    icd_name = df[df['ICD_CODE'] == icd]['ICD_NAME']
    snomed_fsn = df[df['ICD_CODE'] == icd]['SNOMED_FSN'].tolist()

    snomed_df = pd.DataFrame({
        'SNOMED_CID': snomed_lst,
        'SNOMED_FSN': snomed_fsn
    })

    return snomed_df, icd_name.iloc[0]  if not icd_name.empty else "Unknown ICD"
