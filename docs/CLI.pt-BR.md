# CLI (Português do Brasil)

[English version](CLI.en.md)

## O que é

A CLI expõe a biblioteca no terminal por meio do comando `pydf`.

Ela serve para quem quer processar PDFs sem escrever código Python.

## Como instalar para usar a CLI

### Modo local de desenvolvimento

```bash
pip install -e .
```

Isso registra o comando `pydf` no ambiente Python atual.

### Build de pacote

```bash
python -m build
```

## Como executar

### Ajuda geral

```bash
pydf --help
```

### Exemplo mínimo

```bash
pydf examples/pdf_invoices
```

### Definindo o Excel de saída

```bash
pydf examples/pdf_invoices --output output/invoices.xlsx
```

### Busca recursiva

```bash
pydf examples --recursive
```

### Com regex customizada

```bash
pydf invoices   --invoice-number-pattern "INVOICE #(\d+)"   --invoice-date-pattern "(?:DATE|DATE OF ISSUE):?\s*(\d{2}/\d{2}/\d{4})"
```

### Com MySQL

```bash
pydf examples/pdf_invoices   --persist-to-database   --db-host localhost   --db-user root   --db-password ""   --db-name process_invoices   --db-table invoice_records
```

## Flags e argumentos

### Argumento posicional

- `input_dir`: pasta com PDFs. Se omitido, usa `pdf_invoices`.

### Flags principais

- `--output`: caminho do arquivo `.xlsx`.
- `--invoice-number-pattern`: regex do número da fatura.
- `--invoice-date-pattern`: regex da data da fatura.
- `--recursive`: busca em subpastas.
- `--persist-to-database`: ativa persistência em MySQL.
- `--db-host`: host do MySQL.
- `--db-user`: usuário do MySQL.
- `--db-password`: senha do MySQL.
- `--db-name`: nome do banco.
- `--db-table`: nome da tabela.
- `--version`: mostra a versão da CLI.
- `--help`: mostra a ajuda.

## Saída esperada

Ao final da execução, a CLI mostra:

- quantidade de arquivos processados;
- quantidade de sucessos;
- quantidade de erros;
- caminho final do Excel gerado.

## Quando usar CLI em vez da API

Use a CLI quando:

- você só quer rodar um lote rapidamente;
- vai automatizar isso em scripts `.bat`, shell script ou CI;
- não precisa integrar o resultado em outra aplicação Python.
