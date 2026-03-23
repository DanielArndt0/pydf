# CLI

[Versão em Português do Brasil](CLI.pt-BR.md)

## What it is

The CLI exposes the library through the `pydf` terminal command.

Use it when you want to process PDFs without writing Python code.

## Installation for CLI usage

### Local development mode

```bash
pip install -e .
```

This registers the `pydf` command in the current Python environment.

### Package build

```bash
python -m build
```

## How to run it

### General help

```bash
pydf --help
```

### Minimum example

```bash
pydf examples/pdf_invoices
```

### Explicit Excel output path

```bash
pydf examples/pdf_invoices --output output/invoices.xlsx
```

### Recursive search

```bash
pydf examples --recursive
```

### Custom regex

```bash
pydf invoices   --invoice-number-pattern "INVOICE #(\d+)"   --invoice-date-pattern "(?:DATE|DATE OF ISSUE):?\s*(\d{2}/\d{2}/\d{4})"
```

### MySQL persistence

```bash
pydf examples/pdf_invoices   --persist-to-database   --db-host localhost   --db-user root   --db-password ""   --db-name process_invoices   --db-table invoice_records
```

## Flags and arguments

### Positional argument

- `input_dir`: directory containing PDFs. Defaults to `pdf_invoices`.

### Main flags

- `--output`: output `.xlsx` path.
- `--invoice-number-pattern`: invoice number regex.
- `--invoice-date-pattern`: invoice date regex.
- `--recursive`: search subdirectories.
- `--persist-to-database`: enable MySQL persistence.
- `--db-host`: MySQL host.
- `--db-user`: MySQL user.
- `--db-password`: MySQL password.
- `--db-name`: database name.
- `--db-table`: table name.
- `--version`: show CLI version.
- `--help`: show help.

## Expected output

At the end of the execution, the CLI prints:

- number of processed files;
- number of successes;
- number of errors;
- final generated Excel path.

## When to use the CLI instead of the API

Use the CLI when:

- you only need to run a quick batch job;
- you want to automate execution in shell scripts or CI;
- you do not need to integrate the result into another Python application.
