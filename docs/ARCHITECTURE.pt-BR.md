# Visão geral da arquitetura

[English version](ARCHITECTURE.md)

## Objetivo

O projeto foi transformado em biblioteca sem abandonar o fluxo original. A arquitetura procura manter a implementação pequena e fácil de entender.

## Camadas

### 1. Camada de configuração

- `config.py`
- Contém `ProcessorConfig` e `DatabaseConfig`.
- É usada tanto pela API quanto pela CLI.

### 2. Camada de parsing

- `parser.py`
- Lê o texto da primeira página do PDF.
- Aplica regex para extrair número e data.

### 3. Camada de orquestração

- `processor.py`
- Descobre os arquivos.
- Coordena o parsing.
- Trata falhas por arquivo sem abortar o lote inteiro.
- Delega exportação para Excel e persistência opcional em banco.

### 4. Camada de saída

- `excel.py`
- Converte os registros em um arquivo `.xlsx`.

### 5. Camada de persistência

- `database.py`
- Gerencia conexão MySQL e inserção dos registros.

### 6. Pontos de entrada

- `cli.py`: entrada via terminal.
- `__init__.py`: API pública do pacote.
- `legacy.py`: helper de compatibilidade com o estilo do projeto original.

## Fluxo de processamento

```text
CLI ou API Python
        |
        v
ProcessorConfig / DatabaseConfig
        |
        v
InvoiceProcessor.process()
        |
        +--> descobrir PDFs
        +--> processar cada PDF
        +--> opcionalmente inserir no MySQL
        +--> exportar registros para Excel
        v
ProcessingResult
```

## Escolhas de design

- O processamento em lote continua resiliente: um arquivo ruim não derruba os demais.
- O parsing continua simples: primeira página + regex, preservando o espírito do projeto original.
- Os pontos de extensão ficam claros: regex, recursão, persistência em banco e funções públicas auxiliares.
