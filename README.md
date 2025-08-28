# Top 3 best matching SNOMED code

This package fetches the best matching SNOMED CT code given an ICD code and patient context using DSPy and Ollama.

## Installation modules:
```
pip install ollama
```
```
pip install dspy
```

Clone this repo:

```
pip install -r requirements.txt
ollama run mistral
```
Usage

```bash
from best_snomed.rag import using_dspy

top_matches = using_dspy(hadm_id=12345, icd9_code="25000")
print(top_matches)
```








