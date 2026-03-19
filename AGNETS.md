# AGENTS.md - Guidelines for Agentic Coding

This document provides guidelines for agents working in this repository.

## Project Overview

This is a Binder template repository for running robotics research Jupyter Notebooks on Binderhub. The project consists of:
- Jupyter notebooks (`.ipynb` files) in the `notebooks/` directory
- Python utility code in `notebooks/utils.py`
- Docker-based development environment in `binder/`

## Build/Lint/Test Commands

### Development Environment (Docker)

```bash
# Build and run docker image locally
docker compose -f ./binder/docker-compose.yml up --build

# Stop and remove container
docker compose -f ./binder/docker-compose.yml down
```

### Python Package Management

```bash
# Install dependencies
pip install -r requirements.txt

# Add new dependency (update requirements.txt manually)
# Then rebuild Docker image to apply changes
```

### Testing

**No formal test framework is currently configured.** To add tests:

```bash
# Install pytest
pip install pytest

# Run all tests
pytest

# Run a single test file
pytest tests/test_example.py

# Run a specific test function
pytest tests/test_example.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"
```

### Linting/Type Checking (Recommended Additions)

To enforce code quality, consider adding these tools:

```bash
# Install linting tools
pip install flake8 black mypy

# Run flake8 (linting)
flake8 .

# Run black (formatting) - checks only
black --check .

# Run black - auto-format
black .

# Run mypy (type checking)
mypy .
```

## Code Style Guidelines

### Imports

Organize imports in the following order (separated by blank lines):
1. Standard library imports (`os`, `sys`, `json`, etc.)
2. Third-party imports (`ipywidgets`, `sidecar`, etc.)
3. Local application imports

```python
import os
import sys

import ipywidgets as widgets
from sidecar import Sidecar

from . import local_module
```

### Formatting

- Use **4 spaces** for indentation (PEP 8 default)
- Maximum line length: **100 characters** (recommended)
- Use blank lines sparingly to group related code
- No trailing whitespace

### Types

- Use type hints for function signatures (Python 3.9+):
  ```python
  def function(arg1: str, arg2: int) -> bool:
      ...
  ```
- Document complex types in docstrings when type hints are insufficient

### Naming Conventions

- **Functions/variables**: `snake_case` (e.g., `my_function`, `my_variable`)
- **Classes**: `PascalCase` (e.g., `MyClass`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MY_CONSTANT`)
- **Private methods/attributes**: prefix with underscore (e.g., `_private_method`)
- Use descriptive, verbose names (`display_desktop` not `disp`)

### Docstrings

Use Google-style or NumPy-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """Short description of what the function does.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of what is returned.

    Raises:
        ValueError: When something specific happens.
    """
```

### Error Handling

- Use specific exception types (e.g., `KeyError`, `ValueError`)
- Catch exceptions only when you can handle them meaningfully
- Provide context in error messages

```python
try:
    value = os.environ["VARIABLE"]
except KeyError:
    value = "default_value"  # Provide fallback
```

### Jupyter Notebooks

- Keep notebooks in the `notebooks/` directory
- Clear outputs before committing (or use `.gitignore` for `.ipynb_checkpoints/`)
- Use descriptive cell titles when possible

## Project Structure

```
/home/repo
├── AGENTS.md              # This file
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
├── binder/
│   ├── Dockerfile         # Docker image definition
│   ├── docker-compose.yml # Local development setup
│   └── entrypoint.sh      # Container entry point
└── notebooks/
    ├── utils.py           # Python utility functions
    └── *.ipynb            # Jupyter notebooks
```

## Best Practices

1. **Never commit secrets** - Do not add `.env`, credentials, or API keys to version control
2. **Use virtual environments** - For local development, use `venv` or `conda`
3. **Write tests** - Add unit tests in a `tests/` directory when adding new code
4. **Document complex logic** - Add comments for non-obvious code sections
5. **Run linting before commits** - Ensure code passes `flake8` and `black --check`

## Cursor/Copilot Rules

No custom Cursor or Copilot rules are configured for this project.