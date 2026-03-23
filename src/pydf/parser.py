from __future__ import annotations

"""PDF parsing helpers.

This module is intentionally small and focused. It reads the first page of the
PDF, extracts text, and applies the configured regular expressions.
"""

import re
from pathlib import Path

import pdfplumber

from .models import InvoiceRecord


def extract_text_from_pdf(file_path: Path) -> str:
    """Extract text from the first page of a PDF file.

    Args:
        file_path: Absolute or relative path to a PDF file.

    Returns:
        The extracted text from the first page.

    Raises:
        ValueError: If the PDF contains no pages.
    """
    with pdfplumber.open(file_path) as pdf:
        if not pdf.pages:
            raise ValueError("PDF has no pages")
        return pdf.pages[0].extract_text() or ""


def parse_invoice(file_path: Path, number_pattern: str, date_pattern: str, completed_status: str) -> InvoiceRecord:
    """Parse a single invoice-like PDF into an :class:`InvoiceRecord`.

    Args:
        file_path: PDF file to inspect.
        number_pattern: Regex with one capturing group for the invoice number.
        date_pattern: Regex with one capturing group for the invoice date.
        completed_status: Status text to use when extraction succeeds.
    """
    pdf_text = extract_text_from_pdf(file_path)

    match_number = re.search(number_pattern, pdf_text)
    match_date = re.search(date_pattern, pdf_text)

    if not match_number:
        raise ValueError("Couldn't find invoice number")
    if not match_date:
        raise ValueError("Couldn't find invoice date")

    return InvoiceRecord(
        invoice_number=match_number.group(1),
        invoice_date=match_date.group(1),
        file_name=file_path.name,
        status=completed_status,
    )
