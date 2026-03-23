from __future__ import annotations

"""Lightweight data structures returned by the library."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class InvoiceRecord:
    """Represents the outcome of parsing a single PDF file."""

    invoice_number: str
    invoice_date: str
    file_name: str
    status: str


@dataclass(slots=True)
class ProcessingResult:
    """Aggregated result produced by :meth:`pydf.InvoiceProcessor.process`."""

    records: list[InvoiceRecord] = field(default_factory=list)
    output_excel: Optional[Path] = None

    @property
    def success_count(self) -> int:
        """Return how many records finished with the configured success status."""
        return sum(1 for record in self.records if record.status == "Completed")

    @property
    def error_count(self) -> int:
        """Return how many records finished with an error-like status."""
        return len(self.records) - self.success_count
