# Bananagrams

In this version of Bananagrams, you must type words as fastly as possible to steal them from the opponents. The player with the most letters at the end of the game wins.

TODO add more content to readme.

---

# Development

## Installation

### Linter

First, install the linter:
[Trunk](https://docs.trunk.io/check/cli/install-trunk)

### Frontend (peel)

```sh
cd peel.
npm install
```

### Backend (flesh)

```sh
cd flesh
pyenv local 3.12
python -m venv venv && . venv/bin/activate && pip install -r requirements.txt
```

## Execution

### Frontend (peel)

```sh
cd peel
npm run start
```

### Backend (flesh)

```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
