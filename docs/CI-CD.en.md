# CI/CD and Releases

[Versão em Português (Brasil)](CI-CD.pt-BR.md)

## Goal

This repository is configured for the following flow:

- on **every push** and **every pull request**: run tests and validate the build
- on a **manually published release**: generate distribution artifacts and attach them to the GitHub release

## Included workflows

### 1. CI

File: `.github/workflows/ci.yml`

Runs:

- checkout
- Python 3.10 and 3.11 setup
- editable install with development dependencies
- `pytest`
- `python -m build`

### 2. Release

File: `.github/workflows/release.yml`

Runs:

- checkout
- Python 3.10 setup
- build dependencies install
- `sdist` and `wheel` generation in `dist/`
- upload of `dist/*` to the GitHub release

It runs on:

- `release.published`

It also skips pre-releases.
