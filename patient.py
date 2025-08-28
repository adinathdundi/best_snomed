import pandas as pd
from dataloader import admission_df, prescription_df, labtest_df, cpt_events_df, gender_df


def fetch_patient_context(hadm_id: int):
    """
    Extract patient context for a given admission ID.
    Includes gender, primary diagnosis, prescribed drugs, lab test results, CPT events.
    """
    gender = gender_df.loc[admission_df['HADM_ID'] == hadm_id]['GENDER'].values[0]
    primary_diagnosis = admission_df.loc[admission_df['HADM_ID'] == hadm_id]['DIAGNOSIS'].values[0]

    prescribed_drugs = prescription_df.loc[prescription_df['HADM_ID'] == hadm_id]['DRUG'].tolist()
    
    labtest_string = ', '.join(
        f"{row['LABEL']}: {'Normal' if pd.isna(row['FLAG']) else row['FLAG']}"
        for _, row in labtest_df[labtest_df['HADM_ID'] == hadm_id].iterrows()
    )   
    
    cpt_events = ', '.join(cpt_events_df[cpt_events_df['HADM_ID'] == hadm_id]['SUBSECTIONHEADER'].tolist())

    return [gender, primary_diagnosis, prescribed_drugs, labtest_string, cpt_events]
