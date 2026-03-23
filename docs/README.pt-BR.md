# Documentação em Português (Brasil)

[English version](README.en.md)

## Visão geral

A `pydf` é uma biblioteca Python criada a partir do projeto original, mantendo a mesma ideia principal: ler PDFs de faturas, extrair número e data da fatura, gerar uma planilha Excel e, opcionalmente, persistir os dados em MySQL.

Esta versão também inclui uma CLI, exemplos comentados e workflows recomendados para GitHub Actions.

## Comece por aqui

- [README principal](../README.md)
- [Guia da CLI](CLI.pt-BR.md)
- [Guia da API pública](API.pt-BR.md)
- [Arquitetura](ARCHITECTURE.pt-BR.md)
- [CI/CD e Releases](CI-CD.pt-BR.md)
- [Ambiente Python, venv e troubleshooting](ENVIRONMENT.pt-BR.md)
- [Exemplos](../examples/README.md)

## Instalação

```bash
pip install -e .
```

Com dependências de desenvolvimento:

```bash
pip install -e .[dev]
```

## Formas de uso

### 1. Via CLI

```bash
pydf examples/pdf_invoices --output output/invoices.xlsx
```

### 2. Via Python

```python
from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="output/invoices.xlsx",
)

result = InvoiceProcessor(config).process()
print(result.output_excel)
```
