# Thoughtful Package Sorter

Python implementation of `sort(width, height, length, mass)` that classifies packages into **STANDARD**, **SPECIAL**, or **REJECTED** based on volume/dimensions and mass.

## Rules Recap
- **Bulky** if volume `>= 1,000,000 cm³` **or** any dimension `>= 150 cm`.
- **Heavy** if mass `>= 20 kg`.
- **Stacks**:
  - `REJECTED`: both heavy **and** bulky
  - `SPECIAL`: either heavy **or** bulky (but not both)
  - `STANDARD`: neither

## Quick Start (local)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip pytest
pytest -q
```

Run a small demo:

```bash
python sort.py
```

