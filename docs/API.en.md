# Public API

[Versão em Português do Brasil](API.pt-BR.md)

## Overview

The library was organized so most integrations go through a few simple entry points.

## Main objects

### `ProcessorConfig`

Main configuration object.

Most useful fields:

- `input_dir`: directory containing PDFs.
- `output_excel`: final Excel path.
- `invoice_number_pattern`: invoice number regex.
- `invoice_date_pattern`: invoice date regex.
- `worksheet_name`: Excel sheet name.
- `status_completed`: success status text.
- `persist_to_database`: enables MySQL persistence.
- `database`: `DatabaseConfig` instance.
- `recursive`: recursive search.

### `DatabaseConfig`

Used only when `persist_to_database=True`.

Fields:

- `host`
- `user`
- `password`
- `database`
- `table`

### `InvoiceProcessor`

Main library class.

Most important method:

- `process() -> ProcessingResult`

### `ProcessingResult`

Consolidated processing result.

Properties:

- `records`
- `output_excel`
- `success_count`
- `error_count`

### `InvoiceRecord`

Represents one processed PDF.

Fields:

- `invoice_number`
- `invoice_date`
- `file_name`
- `status`

## Useful functions

### `extract_text_from_pdf(file_path)`

Extracts text from the first page of the PDF.

### `parse_invoice(file_path, number_pattern, date_pattern, completed_status)`

Processes a single PDF and returns an `InvoiceRecord`.

## Direct API example

```python
from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="output/api_usage.xlsx",
)

result = InvoiceProcessor(config).process()
print(result.success_count)
```

## When to use the API

Use the API when:

- you want to integrate processing into another Python system;
- you need to inspect the `ProcessingResult` in memory;
- you want more control over customization.
