run:
	streamlit run src/app/main.py

all: setup-git-hooks install check test 

check: check-format check-lint check-types

check-format:
	uv run ruff format . --diff

check-lint:
	uv run ruff check .

check-types:
	uv run mypy .

install: setup-env-variables
	uv lock --locked
	uv sync --locked --group dev --group lint --group test

lint:
	uv run ruff format .
	uv run ruff check . --fix

setup-env-variables:
	cp .streamlit/secrets.toml.example .streamlit/secrets.toml

setup-git-hooks:
	chmod +x hooks/pre-commit
	chmod +x hooks/pre-push
	git config core.hooksPath hooks

test:
	uv run pytest -v --cov=python_project_template --cov-report=xml

.PHONY: all check check-format check-lint install lint test