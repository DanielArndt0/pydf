# CI/CD e Releases

[English version](CI-CD.en.md)

## Objetivo

Este repositório foi configurado para o seguinte fluxo:

- em **todo push** e **todo pull request**: rodar testes e validar o build
- em **release publicada manualmente**: gerar os artefatos de distribuição e anexá-los à release do GitHub

Esse modelo evita publicação automática a cada commit e combina melhor com um projeto que será distribuído principalmente por GitHub e releases.

## Workflows incluídos

### 1. CI

Arquivo: `.github/workflows/ci.yml`

Executa:

- checkout do código
- setup do Python 3.10 e 3.11
- instalação do projeto com dependências de desenvolvimento
- execução do `pytest`
- execução de `python -m build`

Esse workflow roda em:

- `push` para `main` e `master`
- `pull_request`

### 2. Release

Arquivo: `.github/workflows/release.yml`

Executa:

- checkout do código
- setup do Python 3.10
- instalação de dependências de build
- geração de `sdist` e `wheel` em `dist/`
- upload dos artefatos da pasta `dist/` para a release do GitHub

Esse workflow roda em:

- `release.published`

Além disso, ele ignora `pre-release`.

## Como criar uma release estável

1. Atualize a versão em `pyproject.toml`
2. Faça commit das alterações
3. Envie para o GitHub
4. Crie uma tag, por exemplo `v1.0.0`
5. Publique uma release manual estável no GitHub usando essa tag

Quando a release for publicada, o workflow `release.yml` será executado e anexará os arquivos gerados em `dist/`.

## O que este repositório não faz

Este projeto **não publica em GitHub Packages como índice Python para `pip`**, porque esse tipo de registry não é suportado para pacotes Python.

Para este caso, as opções documentadas são:

- instalar direto do GitHub com `pip install "git+https://..."`
- baixar o `.whl` da release e instalar com `pip install arquivo.whl`

## Instalação da CLI a partir do GitHub

### Pela branch padrão

```bash
pip install "git+https://github.com/DanielArndt0/pydf.git"
```

### Por tag ou release

```bash
pip install "git+https://github.com/DanielArndt0/pydf.git@v1.0.0"
```

## Validação local antes de subir

```bash
pip install -e .[dev]
pytest -v
python -m build
```
