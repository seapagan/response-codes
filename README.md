# HTTP Response Codes

A comprehensive Python library providing HTTP status code constants and exceptions.

[![PyPI version](https://badge.fury.io/py/http-response-codes.svg)](https://badge.fury.io/py/http-response-codes)
[![Python Support](https://img.shields.io/pypi/pyversions/http-response-codes.svg)](https://pypi.org/project/http-response-codes/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

NOTE: This library is still in development and has little actual usage or real
use-cases so far. Indeed, the module api may change considerably - i'll have it
locked down in the next few days. Uploading to PyPI now just to reserve the name
and possibly get some early adopters/feedback

## Overview

`http-response-codes` is a Python library that provides a comprehensive set of
HTTP status codes as exception classes. Each status code is represented by a
class that inherits from `HTTPStatus`, containing the numeric code, message, and
description.

The module covers all standard HTTP status codes in the following categories:

- 1xx: Informational responses (100-102)
- 2xx: Success responses (200-208, 226)
- 3xx: Redirection responses (300-308)
- 4xx: Client error responses (400-431, 451)
- 5xx: Server error responses (500-511)

## Installation

```bash
pip install http-response-codes
```

Or using `uv`:

```bash
uv add http-response-codes
```

## Features

- Complete coverage of HTTP status codes
- Each status code is a proper Python exception class
- Type hints included
- Predefined groups of related status codes
- Intuitive comparison operations
- Detailed descriptions for each status code
- Zero dependencies

## Usage

### Basic Usage

```python
from response_codes import HTTP_404_NOT_FOUND

# Raise as an exception
raise HTTP_404_NOT_FOUND()

# Access status code properties
print(HTTP_404_NOT_FOUND.status_code)  # 404
print(HTTP_404_NOT_FOUND.message)      # "Not Found"
print(HTTP_404_NOT_FOUND.description)  # Detailed description

# Compare with integers
assert HTTP_404_NOT_FOUND == 404
```

### Using Status Code Groups

```python
from response_codes import (
    HTTP_INFORMATIONAL,
    HTTP_SUCCESS,
    HTTP_REDIRECTION,
    HTTP_CLIENT_ERRORS,
    HTTP_SERVER_ERRORS,
)

# Check if a status code is in a group
status_code = 404
if status_code in HTTP_CLIENT_ERRORS:
    print("This is a client error!")
```

## Development

This project uses modern Python tooling:

- `uv` for dependency management
- `ruff` for linting and formatting
- `mypy` for type checking
- `pytest` for testing
- `pre-commit` for git hooks

### Setup Development Environment

Clone the repository:

```bash
git clone https://github.com/seapagan/response-codes.git
cd response-codes
```

Install development dependencies:

```bash
uv sync
```

Install pre-commit hooks:

```bash
pre-commit install
```

### Running Tests

```bash
poe test # or simply run 'pytest'
```

Or in watch mode:

```bash
poe test:watch
```

### Code Quality Checks

```bash
# Run all pre-commit checks
poe pre

# Run mypy type checking
poe mypy

# Run ruff linting
poe ruff

# Run ruff formatting
poe format
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created and maintained by [Grant Ramsay](https://github.com/seapagan)
