# Assignment — Part 7
---

## How to Run

### 1. Install Requirements
```bash
pip install -r requirements

python main.py
```
---
### Logic
- If data extracted from llm thus no errors
- If missing values then fallback to rule based (if >3 errors then whole text fallback to rule based else partial i.e only missing values)
