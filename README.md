# Top 3 best matching SNOMED code

This package fetches the best matching SNOMED CT code given an ICD code and patient context using DSPy and Ollama.

## Installation modules:
```
pip install ollama
```
```
pip install dspy
```


Usage
Open a new jupyter notebook and import rag module

```bash
import rag

top_matches = rag.using_dspy(hadm_id=1234, icd9code='32455')
print(top_matches)
```









