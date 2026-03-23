# Ambiente Python, venv e troubleshooting

[English version](ENVIRONMENT.en.md)

## Versão mínima do Python

Este projeto requer **Python 3.10 ou superior**.

Se você tentar instalar com uma versão mais antiga, poderá ver algo como:

```text
ERROR: Package 'pydf' requires a different Python: 3.8.5 not in '>=3.10'
```

## Como verificar as versões instaladas no Windows

```powershell
py -0p
```

## Como criar um ambiente virtual com Python 3.10

Na raiz do projeto:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Como confirmar a versão ativa

```powershell
python --version
```

## Como rodar os testes

```powershell
python -m pytest -v
```

## Como testar se o pacote foi instalado

```powershell
python -c "import pydf; print('ok')"
```

## Se o comando da CLI não for reconhecido

Use o modo por módulo:

```powershell
python -m pydf.cli --help
```

## Problemas comuns

### 1. `No module named 'pydf'`

O pacote ainda não foi instalado no ambiente atual.

Resolva com:

```powershell
python -m pip install -e .
```

### 2. `requires a different Python`

Você está usando uma versão abaixo do mínimo exigido.

Crie o venv com Python 3.10 ou superior.

### 3. `pytest` não reconhecido

Use:

```powershell
python -m pytest -v
```

ou instale as dependências de desenvolvimento:

```powershell
python -m pip install -e .[dev]
```
