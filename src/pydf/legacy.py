from __future__ import annotations

"""Compatibility helpers for users migrating from the original script."""

from .config import DatabaseConfig, ProcessorConfig
from .processor import InvoiceProcessor


def run_legacy_flow() -> None:
    """Run a configuration close to the original project behavior."""
    config = ProcessorConfig(
        input_dir="pdf_invoices",
        persist_to_database=True,
        database=DatabaseConfig(
            host="localhost",
            user="root",
            password="",
            database="process_invoices",
            table="invoice_records",
        ),
    )
    InvoiceProcessor(config).process()
