# CLAUDE.md - Datasette Metasearch Reference

## Build/Test Commands
```bash
# Setup development environment
python3 -mvenv venv
source venv/bin/activate
pip install -e '.[test]'

# Run all tests
pytest

# Run specific test
pytest tests/test_cli.py::test_basic
pytest -xvs tests/test_plugin.py::test_search

# Run in development
datasette install datasette-metasearch
datasette

# Indexing command
datasette-metasearch index <db_path> <config.yml>
```

## Code Style Guidelines
- **Formatting**: Use Black-compatible formatting
- **Imports**: Group standard library, then third-party, then local imports
- **TypeHints**: Not currently used in codebase
- **Naming**: Snake case for variables/functions, CamelCase for classes
- **Error Handling**: Use try/except with specific exceptions
- **Documentation**: Document functions and classes with docstrings
- **Testing**: Write pytest tests for new functionality

## Project Structure
- Plugin uses Datasette hooks API with a `/beta` endpoint
- CLI tool for indexing with `datasette-metasearch` command