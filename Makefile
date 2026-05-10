.PHONY: install run lint format clean test help

help:
	@echo "Available commands:"
	@echo "  install   Install dependencies"
	@echo "  run       Run the game"
	@echo "  lint      Run linting checks"
	@echo "  format    Format code"
	@echo "  clean     Clean up temporary files"
	@echo "  test      Run tests"

install:
	pip install -e .

run:
	python src/main.py

lint:
	ruff check .

format:
	ruff format .

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache build dist *.egg-info

test:
	pytest
