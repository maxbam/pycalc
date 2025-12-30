# pycalc

A simple calculator application built to demonstrate professional Python project setup and CI/CD workflows.

## About

This is a practice project designed to:

- Test Continuous Integration (CI) workflows in GitHub.
- Demonstrate how to set up a professional Python project structure.
- Showcase modern Python tooling including `uv` for dependency management, `ruff` for linting/formatting, and `pytest` for testing.

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

### Installation

Clone the repository and sync the environment:

```bash
git clone https://github.com/maxbam/pycalc.git
cd pycalc
uv sync
```

### Running Tests

```bash
uv run pytest
```
