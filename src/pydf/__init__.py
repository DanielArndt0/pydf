"""Public package interface for pydf.

The package keeps the original project idea intact:
read invoice PDFs, extract a few key fields, export the result to Excel,
and optionally persist records to MySQL.
"""

from .config import DatabaseConfig, ProcessorConfig
from .models import InvoiceRecord, ProcessingResult
from .parser import extract_text_from_pdf, parse_invoice
from .processor import InvoiceProcessor

__all__ = [
    "DatabaseConfig",
    "ProcessorConfig",
    "InvoiceRecord",
    "ProcessingResult",
    "InvoiceProcessor",
    "extract_text_from_pdf",
    "parse_invoice",
]
