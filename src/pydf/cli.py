from __future__ import annotations

"""Command-line interface for pydf."""

import argparse

from .config import DatabaseConfig, ProcessorConfig
from .processor import InvoiceProcessor

VERSION = "1.0.0"


def build_parser() -> argparse.ArgumentParser:
    """Create and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="pydf",
        description=(
            "Process invoice PDFs, extract invoice number and date, "
            "export results to Excel, and optionally persist records to MySQL."
        ),
        epilog="""
Examples:
  pydf
  pydf examples/pdf_invoices
  pydf examples/pdf_invoices --output out/invoices.xlsx
  pydf invoices --recursive
  pydf invoices --invoice-number-pattern "Invoice No\\. (\\d+)"
  pydf invoices --persist-to-database --db-host localhost --db-user root --db-name process_invoices
""".strip(),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "input_dir",
        nargs="?",
        default="pdf_invoices",
        help="Directory containing PDF files (default: %(default)s).",
    )

    parser.add_argument(
        "--output",
        dest="output_excel",
        metavar="PATH",
        help=(
            "Path to the output .xlsx file. "
            "If omitted, a timestamped file name will be generated."
        ),
    )

    parser.add_argument(
        "--invoice-number-pattern",
        default=r"INVOICE #(\d+)",
        metavar="REGEX",
        help="Regex with one capture group for the invoice number.",
    )

    parser.add_argument(
        "--invoice-date-pattern",
        default=r"(?:DATE|DATE OF ISSUE):?\s*(\d{2}/\d{2}/\d{4})",
        metavar="REGEX",
        help="Regex with one capture group for the invoice date.",
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Search for PDF files recursively in subdirectories.",
    )

    parser.add_argument(
        "--persist-to-database",
        action="store_true",
        help="Persist processed records to MySQL in addition to generating the Excel file.",
    )

    parser.add_argument(
        "--db-host",
        default="localhost",
        metavar="HOST",
        help="MySQL host (default: %(default)s).",
    )

    parser.add_argument(
        "--db-user",
        default="root",
        metavar="USER",
        help="MySQL user (default: %(default)s).",
    )

    parser.add_argument(
        "--db-password",
        default="",
        metavar="PASSWORD",
        help="MySQL password (default: empty).",
    )

    parser.add_argument(
        "--db-name",
        default="process_invoices",
        metavar="NAME",
        help="MySQL database name (default: %(default)s).",
    )

    parser.add_argument(
        "--db-table",
        default="invoice_records",
        metavar="TABLE",
        help="MySQL target table name (default: %(default)s).",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )

    return parser


def build_database_config(args: argparse.Namespace) -> DatabaseConfig | None:
    """Build database configuration if persistence is enabled."""
    if not args.persist_to_database:
        return None

    return DatabaseConfig(
        host=args.db_host,
        user=args.db_user,
        password=args.db_password,
        database=args.db_name,
        table=args.db_table,
    )


def main() -> None:
    """Run the CLI."""
    parser = build_parser()
    args = parser.parse_args()

    config = ProcessorConfig(
        input_dir=args.input_dir,
        output_excel=args.output_excel,
        invoice_number_pattern=args.invoice_number_pattern,
        invoice_date_pattern=args.invoice_date_pattern,
        persist_to_database=args.persist_to_database,
        database=build_database_config(args),
        recursive=args.recursive,
    )

    result = InvoiceProcessor(config).process()

    print("\nPyDF processing completed")
    print("-" * 28)
    print(f"Processed files : {len(result.records)}")
    print(f"Success         : {result.success_count}")
    print(f"Errors          : {result.error_count}")
    print(f"Excel output    : {result.output_excel}")


if __name__ == "__main__":
    main()