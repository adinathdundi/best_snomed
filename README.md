# Top 3 best matching SNOMED code

This package fetches the best matching SNOMED CT code given an ICD code and patient context using DSPy and Ollama.

## Installation

Clone this repo:

```bash
pip install -r requirements.txt
ollama run llama3.2
ollama run mistral
ollama run {any other ollama model}
```
Usage

```bash
from structured_rag import using_dspy

top_matches = using_dspy(hadm_id=12345, icd9_code="25000")
print(top_matches)
```




