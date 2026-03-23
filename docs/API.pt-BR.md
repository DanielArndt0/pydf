# API pública (Português do Brasil)

[English version](API.en.md)

## Visão geral

A biblioteca foi organizada para que a maior parte do uso passe por poucos pontos de entrada.

## Principais objetos

### `ProcessorConfig`

Objeto principal de configuração.

Campos mais úteis:

- `input_dir`: diretório com PDFs.
- `output_excel`: caminho do Excel final.
- `invoice_number_pattern`: regex para número da fatura.
- `invoice_date_pattern`: regex para data da fatura.
- `worksheet_name`: nome da aba do Excel.
- `status_completed`: texto de sucesso.
- `persist_to_database`: habilita gravação no MySQL.
- `database`: instância de `DatabaseConfig`.
- `recursive`: busca recursiva.

### `DatabaseConfig`

Usado apenas se `persist_to_database=True`.

Campos:

- `host`
- `user`
- `password`
- `database`
- `table`

### `InvoiceProcessor`

Classe principal da biblioteca.

Método mais importante:

- `process() -> ProcessingResult`

### `ProcessingResult`

Resultado consolidado do processamento.

Propriedades:

- `records`
- `output_excel`
- `success_count`
- `error_count`

### `InvoiceRecord`

Representa um PDF processado.

Campos:

- `invoice_number`
- `invoice_date`
- `file_name`
- `status`

## Funções úteis

### `extract_text_from_pdf(file_path)`

Extrai o texto da primeira página do PDF.

### `parse_invoice(file_path, number_pattern, date_pattern, completed_status)`

Processa um único PDF e devolve um `InvoiceRecord`.

## Exemplo direto da API

```python
from pydf import InvoiceProcessor, ProcessorConfig

config = ProcessorConfig(
    input_dir="examples/pdf_invoices",
    output_excel="output/api_usage.xlsx",
)

result = InvoiceProcessor(config).process()
print(result.success_count)
```

## Quando usar a API

Use a API quando:

- você vai integrar o processamento em outro sistema Python;
- precisa manipular o `ProcessingResult` em memória;
- quer customizar o fluxo com mais controle.
