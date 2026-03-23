from pathlib import Path

from pydf import InvoiceProcessor, ProcessorConfig


def test_process_sample_pdfs(tmp_path: Path):
    config = ProcessorConfig(
        input_dir="examples/pdf_invoices",
        output_excel=tmp_path / "output.xlsx",
    )
    result = InvoiceProcessor(config).process()

    assert len(result.records) == 4
    assert result.output_excel.exists()
