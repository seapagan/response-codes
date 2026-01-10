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
- **Class-level comparisons** without instantiation required
- Rich comparison operators (`==`, `<`, `<=`, `>`, `>=`)
- Compare with both integers and strings
- Type conversion support (`int()`, `str()`)
- Hashable - use as dictionary keys or in sets
- Type hints included
- Predefined groups of related status codes
- Detailed descriptions for each status code
- Zero dependencies

## Usage

### Basic Usage

```python
from response_codes import HTTP_404_NOT_FOUND

# Raise as an exception
raise HTTP_404_NOT_FOUND()

# Access status code properties (no instantiation needed!)
print(HTTP_404_NOT_FOUND.status_code)  # 404
print(HTTP_404_NOT_FOUND.message)      # "Not Found"
print(HTTP_404_NOT_FOUND.description)  # Detailed description

# Compare directly with integers (class-level magic!)
assert HTTP_404_NOT_FOUND == 404
assert HTTP_404_NOT_FOUND == "Not Found"
```

> [!NOTE]
> Thanks to metaclass magic, you can compare status codes and access their
> properties directly on the class - no need to instantiate!

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

### Advanced Comparison Features

The library uses a metaclass to enable powerful comparison operations
directly on the status code classes (no instantiation required):

#### Compare with Integers or Strings

```python
from response_codes import HTTP_404_NOT_FOUND, HTTP_200_OK

# Integer comparison
if HTTP_404_NOT_FOUND == 404:
    print("It's a 404!")

# String comparison
if HTTP_200_OK == "OK":
    print("Request succeeded")

# Rich comparisons for range checking
if 400 <= HTTP_404_NOT_FOUND < 500:
    print("Client error")

if HTTP_500_INTERNAL_SERVER_ERROR >= 500:
    print("Server error")
```

#### Type Conversions

```python
from response_codes import HTTP_404_NOT_FOUND

# Convert to integer
status_code = int(HTTP_404_NOT_FOUND)  # 404

# Convert to string
status_msg = str(HTTP_404_NOT_FOUND)   # "Not Found"
```

#### Use in Collections

Status codes are hashable and can be used as dictionary keys or in sets:

```python
from response_codes import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

# As dictionary keys
handlers = {
    HTTP_200_OK: handle_success,
    HTTP_404_NOT_FOUND: handle_not_found,
    HTTP_500_INTERNAL_SERVER_ERROR: handle_error,
}

# In sets
critical_errors = {
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
}
```

### Real-World Examples

#### Flask/FastAPI Response Handling

```python
from flask import jsonify
from response_codes import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    user = db.get_user(user_id)

    if not user:
        return (
            jsonify({"error": str(HTTP_404_NOT_FOUND)}),
            int(HTTP_404_NOT_FOUND)
        )

    return jsonify(user), int(HTTP_200_OK)
```

#### Exception Handling with Detailed Information

```python
from response_codes import HTTP_404_NOT_FOUND, HTTPStatus

try:
    resource = fetch_resource(resource_id)
    if not resource:
        raise HTTP_404_NOT_FOUND()
except HTTP_404_NOT_FOUND as e:
    logger.error(f"{e.status_code} - {e.message}: {e.description}")
    return {"error": e.message}, e.status_code
except HTTPStatus as e:
    # Catch any HTTP status exception
    logger.error(f"HTTP Error {e.status_code}: {e.message}")
    return {"error": e.message}, e.status_code
```

#### Status Code Validation and Range Checking

```python
from response_codes import HTTP_CLIENT_ERRORS

def handle_api_response(status_code):
    # Check if status code is in client error range
    if status_code in HTTP_CLIENT_ERRORS:
        retry_request()

    # Check status code ranges using comparisons
    if 200 <= status_code < 300:
        return "Success"
    elif 300 <= status_code < 400:
        return "Redirection"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
```

#### Custom Error Groups

```python
from response_codes import (
    create_status_group,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

# Create custom groups for your application
AUTH_ERRORS = create_status_group(
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

def requires_auth(status_code):
    return status_code in AUTH_ERRORS
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
prek install
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
