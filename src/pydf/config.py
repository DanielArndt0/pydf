from __future__ import annotations

"""Configuration models used by the public API and the CLI."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class DatabaseConfig:
    """Connection settings for the optional MySQL persistence layer.

    Attributes:
        host: MySQL server hostname.
        user: MySQL username.
        password: MySQL password.
        database: Target database name.
        table: Target table name.
    """

    host: str = "localhost"
    user: str = "root"
    password: str = ""
    database: str = "process_invoices"
    table: str = "invoice_records"


@dataclass(slots=True)
class ProcessorConfig:
    """Main configuration object used by :class:`pydf.InvoiceProcessor`.

    The defaults intentionally stay close to the original project so the
    migration from script to library remains straightforward.
    """

    input_dir: Path | str = "pdf_invoices"
    output_excel: Optional[Path | str] = None
    invoice_number_pattern: str = r"INVOICE #(\d+)"
    invoice_date_pattern: str = r"(?:DATE|DATE OF ISSUE):?\s*(\d{2}/\d{2}/\d{4})"
    worksheet_name: str = "Invoice Imports"
    status_completed: str = "Completed"
    persist_to_database: bool = False
    database: Optional[DatabaseConfig] = None
    recursive: bool = False
    supported_extensions: tuple[str, ...] = field(default_factory=lambda: (".pdf",))

    def resolved_input_dir(self) -> Path:
        """Return the absolute input directory path."""
        return Path(self.input_dir).expanduser().resolve()
