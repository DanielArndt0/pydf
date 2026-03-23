from __future__ import annotations

"""Processing pipeline orchestration."""

from datetime import datetime
from pathlib import Path
from typing import Iterator

from .config import ProcessorConfig
from .database import insert_record, mysql_connection
from .excel import export_records_to_excel
from .models import InvoiceRecord, ProcessingResult
from .parser import parse_invoice


class InvoiceProcessor:
    """High-level processing service.

    Typical flow:
        1. Discover PDF files in the configured input directory.
        2. Parse each file with regex-based extraction.
        3. Optionally persist the results to MySQL.
        4. Export all records to an Excel workbook.
    """

    def __init__(self, config: ProcessorConfig | None = None):
        self.config = config or ProcessorConfig()

    def process(self) -> ProcessingResult:
        """Run the full pipeline and return the aggregated result."""
        files = list(self._iter_files())
        if not files:
            raise FileNotFoundError("No PDF files found in the input directory")

        records: list[InvoiceRecord] = []
        db_connection = None

        if self.config.persist_to_database:
            if not self.config.database:
                raise ValueError("database config is required when persist_to_database=True")
            db_context = mysql_connection(self.config.database)
            db_connection = db_context.__enter__()
        else:
            db_context = None

        try:
            for file_path in files:
                try:
                    record = parse_invoice(
                        file_path=file_path,
                        number_pattern=self.config.invoice_number_pattern,
                        date_pattern=self.config.invoice_date_pattern,
                        completed_status=self.config.status_completed,
                    )
                except Exception as exc:
                    # Keep the batch running even if one file fails,
                    # which mirrors the practical behavior of the original script.
                    record = InvoiceRecord(
                        invoice_number="N/A",
                        invoice_date="N/A",
                        file_name=file_path.name,
                        status=f"Exception: {exc}",
                    )

                records.append(record)

                if db_connection is not None and self.config.database is not None:
                    insert_record(db_connection, self.config.database, record)
        finally:
            if db_context is not None:
                db_context.__exit__(None, None, None)

        output_excel = Path(self.config.output_excel) if self.config.output_excel else self._default_output_name()
        output_excel = export_records_to_excel(records, output_excel, self.config.worksheet_name)
        return ProcessingResult(records=records, output_excel=output_excel)

    def _iter_files(self) -> Iterator[Path]:
        """Yield supported files from the configured input directory."""
        input_dir = self.config.resolved_input_dir()
        if self.config.recursive:
            for file_path in input_dir.rglob('*'):
                if file_path.suffix.lower() in self.config.supported_extensions:
                    yield file_path
        else:
            for file_path in input_dir.iterdir():
                if file_path.is_file() and file_path.suffix.lower() in self.config.supported_extensions:
                    yield file_path

    @staticmethod
    def _default_output_name() -> Path:
        """Build the default timestamped Excel file name."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        return Path(f'Invoices - {timestamp}.xlsx')
