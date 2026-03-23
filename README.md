# Pydf

[Documentação PT-BR](docs/README.pt-BR.md) | [English docs](docs/README.en.md)

A `pydf` é uma biblioteca Python leve para leitura de PDFs de faturas, extração de metadados com regex, exportação para Excel e persistência opcional em MySQL.

Esta versão reorganiza o projeto original como biblioteca e CLI, sem fugir da ideia central do script: **PDF -> extração -> Excel -> MySQL opcional**.

## Visão rápida

- Biblioteca Python reutilizável
- CLI simples para uso no terminal
- Regex configurável para número e data da fatura
- Exportação para `.xlsx`
- Persistência opcional em MySQL
- Documentação em PT-BR e inglês
- Workflows de CI e release para GitHub Actions

## Requisitos

- Python **3.10 ou superior**
- `pip`
- Recomendado: ambiente virtual (`venv`)

## Instalação local

Na raiz do projeto:

```bash
pip install -e .
```

Instalação com dependências de desenvolvimento:

```bash
pip install -e .[dev]
```

## Instalação da CLI via GitHub

Como o GitHub não oferece um registry Python suportado para `pip` no GitHub Packages, a forma recomendada para instalar a CLI a partir do GitHub é usar o próprio repositório Git.

### Instalar da branch padrão

```bash
pip install "git+https://github.com/DanielArndt0/pydf.git"
```

### Instalar de uma tag ou release específica

```bash
pip install "git+https://github.com/DanielArndt0/pydf.git@v1.0.0"
```

Depois disso, a CLI fica disponível como:

```bash
pydf --help
```

## Primeiros passos com venv no Windows

Se você tiver mais de uma versão do Python instalada, confira as versões disponíveis:

```powershell
py -0p
```

Crie e ative um ambiente virtual com Python 3.10:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Como executar a CLI

```bash
pydf --help
pydf examples/pdf_invoices --output output/invoices.xlsx
```

## Como usar como biblioteca

```python
from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="output/invoices.xlsx",
)

result = InvoiceProcessor(config).process()

print(result.output_excel)
for record in result.records:
    print(record.file_name, record.invoice_number, record.invoice_date, record.status)
```

## Rodando testes

```bash
pytest -v
```

Se o ambiente ainda não estiver preparado:

```bash
pip install -e .[dev]
pytest -v
```

## Build local

```bash
python -m build
```

## CI e releases no GitHub

Este repositório inclui dois workflows:

- `ci.yml`: roda testes e build em todo push e pull request
- `release.yml`: gera os artefatos e anexa `dist/*` a uma release publicada manualmente

Documentação detalhada:

- [Guia principal da documentação](docs/README.pt-BR.md)
- [Guia da CLI](docs/CLI.pt-BR.md)
- [Guia da API](docs/API.pt-BR.md)
- [Arquitetura](docs/ARCHITECTURE.pt-BR.md)
- [CI/CD e Releases](docs/CI-CD.pt-BR.md)
- [Ambiente Python, venv e troubleshooting](docs/ENVIRONMENT.pt-BR.md)
- [Exemplos](examples/README.md)

