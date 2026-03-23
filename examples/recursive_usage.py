"""Example showing recursive file discovery."""

from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples",
    output_excel="examples/output/recursive_usage.xlsx",
    recursive=True,
)

result = InvoiceProcessor(config).process()
print(f"Files found: {len(result.records)}")
