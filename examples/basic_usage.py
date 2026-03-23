"""Basic example for the library API.

Run with:
    python examples/basic_usage.py
"""

from pydf import InvoiceProcessor, ProcessorConfig

# The default regex patterns already match the sample PDFs.
config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="examples/output/basic_usage.xlsx",
)

result = InvoiceProcessor(config).process()

print(f"Processed files: {len(result.records)}")
print(f"Output spreadsheet: {result.output_excel}")

for record in result.records:
    print(record)
