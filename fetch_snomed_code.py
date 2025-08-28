import dspy
import pandas as pd
import patient
import utils

class SNOMEDMatcher(dspy.Signature):
    """Match ICD to the best SNOMED candidates given patient history."""
    
    # Patient context (procedures, medications, labs, etc.)
    context: list = dspy.InputField(desc="Filtered patient history relevant to the admission")
    
    # ICD name + SNOMED candidates dataframe
    question: dict = dspy.InputField(desc="Dictionary with 'icd_name' string and 'snomed_candidates' dataframe")
    
    # Output: Top 3 SNOMED codes
    answer: list = dspy.OutputField(desc="Top 3 SNOMED codes most relevant to the ICD and patient context")


class RAG(dspy.Module):
    def __init__(self):
        super().__init__()
        self.snomed_mapper = dspy.ChainOfThought(SNOMEDMatcher)

    def forward(self, full_context, icd_name, snomed_candidates: pd.DataFrame, **kwargs):
        """
        icd_name: str
        snomed_candidates: pd.DataFrame with columns ['SNOMED_CID', 'SNOMED_FSN']
        full_context: list of patient history items
        """
        question = {
            "icd_name": icd_name,
            "snomed_candidates": snomed_candidates
        }
        
        result = self.snomed_mapper(context=full_context, question=question)
        
        top_matches = result.answer[:3] if isinstance(result.answer, list) else [result.answer]
        return top_matches

dspy.configure(lm=dspy.LM("ollama_chat/mistral", api_base="http://localhost:11434"))

# Initialize RAG globally so users can call `using_dspy`
rag = RAG()


def using_dspy(hadm_id: int, icd: str):
    """
    Main entry point for users.
    
    Args:
        hadm_id (int): Admission ID
        icd (str): ICD code
        fetch_snomed_candidates (func): function to fetch SNOMED candidates
        fetch_patient_context (func): function to fetch patient context
    
    Returns:
        list: Top 3 SNOMED matches
    """
    snomed_candidates, icd_name = utils.fetch_snomed_candidates(icd=icd)
    patient_context = patient.fetch_patient_context(hadm_id=hadm_id)

    top_matches = rag(
        full_context=patient_context,
        icd_name=icd_name,
        snomed_candidates=snomed_candidates
    )

    return top_matches

