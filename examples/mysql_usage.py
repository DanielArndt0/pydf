"""Example showing how to enable MySQL persistence.

Before running this example, create the database/table and review your credentials.
"""

from pydf import DatabaseConfig, InvoiceProcessor, ProcessorConfig

# Update these credentials before using against a real database.
db_config = DatabaseConfig(
    host="localhost",
    user="root",
    password="",
    database="process_invoices",
    table="invoice_records",
)

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="examples/output/mysql_usage.xlsx",
    persist_to_database=True,
    database=db_config,
)

result = InvoiceProcessor(config).process()
print(result.output_excel)
