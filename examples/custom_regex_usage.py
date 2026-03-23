"""Example showing how to customize regex patterns.

Use this when your PDFs have a different wording than the sample invoices.
"""

from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="examples/output/custom_regex_usage.xlsx",
    # These are examples only. Adjust them to your own PDF layout.
    invoice_number_pattern=r"INVOICE #(\d+)",
    invoice_date_pattern=r"(?:DATE|DATE OF ISSUE):?\s*(\d{2}/\d{2}/\d{4})",
)

result = InvoiceProcessor(config).process()
print(result.output_excel)
