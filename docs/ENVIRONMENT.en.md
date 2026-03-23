# Python environment, venv, and troubleshooting

[Versão em Português (Brasil)](ENVIRONMENT.pt-BR.md)

## Minimum Python version

This project requires **Python 3.10 or higher**.

## Windows: list installed Python versions

```powershell
py -0p
```

## Create a Python 3.10 virtual environment

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Run tests

```powershell
python -m pytest -v
```
