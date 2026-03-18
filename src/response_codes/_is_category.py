"""Helpers for checking HTTP status categories by predefined groups."""

from __future__ import annotations

from typing import Union

from ._core import HTTPStatus

StatusValue = Union[int, type[HTTPStatus], HTTPStatus]

_INFORMATIONAL_MIN, _INFORMATIONAL_MAX = 100, 199
_SUCCESS_MIN, _SUCCESS_MAX = 200, 299
_REDIRECTION_MIN, _REDIRECTION_MAX = 300, 399
_CLIENT_ERROR_MIN, _CLIENT_ERROR_MAX = 400, 499
_SERVER_ERROR_MIN, _SERVER_ERROR_MAX = 500, 599


def _get_status_code(value: StatusValue) -> int:
    """Extract numeric status code from an int/class/instance.

    Args:
        value: The input status value.

    Returns:
        The numeric HTTP status code.

    Raises:
        TypeError: If `value` is not an supported int/class/instance.
    """
    error_message = "value must be int or HTTPStatus"

    # Note: `bool` is a subclass of `int`, but it's not a valid status code.
    if isinstance(value, bool):
        raise TypeError(error_message)

    if isinstance(value, int):
        return value

    if isinstance(value, HTTPStatus):
        return value.status_code

    if isinstance(value, type) and issubclass(value, HTTPStatus):
        return value.status_code

    raise TypeError(error_message)


def is_informational(value: StatusValue) -> bool:
    """Return True if `value` is in the informational 1xx range."""
    code = _get_status_code(value)
    return _INFORMATIONAL_MIN <= code <= _INFORMATIONAL_MAX


def is_success(value: StatusValue) -> bool:
    """Return True if `value` is in the success 2xx range."""
    code = _get_status_code(value)
    return _SUCCESS_MIN <= code <= _SUCCESS_MAX


def is_redirection(value: StatusValue) -> bool:
    """Return True if `value` is in the redirection 3xx range."""
    code = _get_status_code(value)
    return _REDIRECTION_MIN <= code <= _REDIRECTION_MAX


def is_client_error(value: StatusValue) -> bool:
    """Return True if `value` is in the client error 4xx range."""
    code = _get_status_code(value)
    return _CLIENT_ERROR_MIN <= code <= _CLIENT_ERROR_MAX


def is_server_error(value: StatusValue) -> bool:
    """Return True if `value` is in the server error 5xx range."""
    code = _get_status_code(value)
    return _SERVER_ERROR_MIN <= code <= _SERVER_ERROR_MAX


__all__ = [
    "is_client_error",
    "is_informational",
    "is_redirection",
    "is_server_error",
    "is_success",
]
