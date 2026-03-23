# Architecture overview

[Português do Brasil](ARCHITECTURE.pt-BR.md)

## Goal

The project was turned into a library without abandoning the original flow. The architecture keeps the implementation small and easy to understand.

## Layers

### 1. Configuration layer

- `config.py`
- Holds `ProcessorConfig` and `DatabaseConfig`.
- Used by both the API and the CLI.

### 2. Parsing layer

- `parser.py`
- Reads PDF text from the first page.
- Applies regex extraction for invoice number and date.

### 3. Orchestration layer

- `processor.py`
- Discovers files.
- Coordinates parsing.
- Handles per-file failures without aborting the whole batch.
- Delegates Excel export and optional database persistence.

### 4. Output layer

- `excel.py`
- Converts the records into an `.xlsx` file.

### 5. Persistence layer

- `database.py`
- Manages the MySQL connection and inserts records.

### 6. Entry points

- `cli.py`: terminal entry point.
- `__init__.py`: public package API.
- `legacy.py`: compatibility helper for the original project style.

## Processing flow

```text
CLI or Python API
        |
        v
ProcessorConfig / DatabaseConfig
        |
        v
InvoiceProcessor.process()
        |
        +--> discover PDF files
        +--> parse each PDF
        +--> optionally insert into MySQL
        +--> export records to Excel
        v
ProcessingResult
```

## Design choices

- Keep batch processing resilient: one bad file should not stop the others.
- Keep parsing simple: first page + regex, matching the original project spirit.
- Keep extension points obvious: regex, recursion, database persistence, and public helper functions.
