# Top 3 best matching SNOMED code

This package fetches the best matching SNOMED CT code given an ICD code and patient context using DSPy and Ollama.

## Installation modules:
```
pip install ollama
```
```
pip install dspy
```
For Ollama, you need to import an LLM found here -> https://ollama.com/search
For running a model:
```
ollama run mistral
```
Usage
Open a new jupyter notebook and import fetch_snomed_code module

```
import fetch_snomed_code as sct

top_matches = sct.using_dspy(hadm_id=125726, icd9code='99672')
print(top_matches)
```

Output

```
[{'code': '408546009',
  'name': 'Coronary artery bypass graft occlusion (disorder)'},
 {'code': '132111000119107',
  'name': 'Acute deep venous thrombosis of lower limb due to cardiac device'},
 {'code': '234211005', 'name': 'Pacemaker electrode displacement (disorder)'}]
```












