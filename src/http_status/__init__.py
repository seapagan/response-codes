"""A Python module providing HTTP status code constants and exceptions.

This module defines a comprehensive set of HTTP status codes as exception
classes, allowing for both error handling and status code validation. Each
status code is represented by a class inheriting from HTTPStatus, containing the
numeric code, message, and description.

The module provides status codes in the following categories: - 1xx:
Informational responses (100-102) - 2xx: Success responses (200-208, 226) - 3xx:
Redirection responses (300-308) - 4xx: Client error responses (400-431, 451) -
5xx: Server error responses (500-511)

Each status code class provides:
    - status_code: The numeric HTTP status code
    - message: The standard HTTP status message
    - description: A detailed description of the status code (where applicable)

The module also provides predefined groups of related status codes via the
create_error_group() utility function:
    - HTTP_INFORMATIONAL: 1xx status codes
    - HTTP_SUCCESS: 2xx status codes
    - HTTP_REDIRECTION: 3xx status codes
    - HTTP_CLIENT_ERRORS: Common 4xx status codes
    - HTTP_SERVER_ERRORS: Common 5xx status codes

Example:
    >>> from http_status import HTTP_404_NOT_FOUND
    >>> raise HTTP_404_NOT_FOUND()
    [404] Not Found
    >>> HTTP_404_NOT_FOUND.status_code
    404
    >>> HTTP_404_NOT_FOUND == 404
    True

Attributes:
    HTTP_INFORMATIONAL (dict): Group of 1xx informational status codes
    HTTP_SUCCESS (dict): Group of 2xx success status codes HTTP_REDIRECTION
    (dict): Group of 3xx redirection status codes HTTP_CLIENT_ERRORS (dict):
    Group of common 4xx client error status codes HTTP_SERVER_ERRORS (dict):
    Group of common 5xx server error status codes
"""

from __future__ import annotations


class HTTPStatus(Exception):
    """Base class for HTTP status code exceptions."""

    _status_code: int = 0
    _message: str = ""
    _description: str = ""

    def __init__(self) -> None:
        super().__init__(f"[{self._status_code}] {self._message}")

    @classmethod
    def __int__(cls) -> int:
        return cls._status_code

    @classmethod
    def __str__(cls) -> str:
        return cls._message

    @classmethod
    def __eq__(cls, other: object) -> bool:
        if isinstance(other, int):
            return cls._status_code == other
        if isinstance(other, str):
            return cls._message == other
        return False

    @classmethod
    def __lt__(cls, other: int) -> bool:
        if isinstance(other, int):
            return cls._status_code < other
        return NotImplemented

    @classmethod
    def __le__(cls, other: int) -> bool:
        if isinstance(other, int):
            return cls._status_code <= other
        return NotImplemented

    @classmethod
    def __gt__(cls, other: int) -> bool:
        if isinstance(other, int):
            return cls._status_code > other
        return NotImplemented

    @classmethod
    def __ge__(cls, other: int) -> bool:
        if isinstance(other, int):
            return cls._status_code >= other
        return NotImplemented

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def message(self) -> str:
        return self._message

    @property
    def description(self) -> str:
        return self._description


# Utility function to create custom groups
def create_error_group(
    *status_classes: list[HTTPStatus],
) -> dict[int, HTTPStatus]:
    """Create a custom status group as a dictionary."""
    return {
        status_class.status_code: status_class
        for status_class in status_classes
    }


# 1xx Informational Responses
class HTTP_100_CONTINUE(HTTPStatus):
    error_code = 100
    message = "Continue"
    description = (
        "The server has received the request headers and the client"
        " should proceed to send the request body."
    )


class HTTP_101_SWITCHING_PROTOCOLS(HTTPStatus):
    error_code = 101
    message = "Switching Protocols"
    description = "The requester has asked the server to switch protocols."


class HTTP_102_PROCESSING(HTTPStatus):
    error_code = 102
    message = "Processing"
    description = (
        "The server is processing the request but no response is available yet."
    )


# 2xx Success
class HTTP_200_OK(HTTPStatus):
    _error_code = 200
    _message = "OK"
    _description = ""


class HTTP_201_CREATED(HTTPStatus):
    _error_code = 201
    _message = "Created"
    _description = ""


class HTTP_202_ACCEPTED(HTTPStatus):
    _error_code = 202
    _message = "Accepted"
    _description = ""


class HTTP_203_NON_AUTHORITATIVE_INFORMATION(HTTPStatus):
    _error_code = 203
    _message = "Non-Authoritative Information"
    _description = ""


class HTTP_204_NO_CONTENT(HTTPStatus):
    _error_code = 204
    _message = "No Content"
    _description = ""


class HTTP_205_RESET_CONTENT(HTTPStatus):
    _error_code = 205
    _message = "Reset Content"
    _description = ""


class HTTP_206_PARTIAL_CONTENT(HTTPStatus):
    _error_code = 206
    _message = "Partial Content"
    _description = ""


class HTTP_207_MULTI_STATUS(HTTPStatus):
    _error_code = 207
    _message = "Multi-Status"
    _description = ""


class HTTP_208_ALREADY_REPORTED(HTTPStatus):
    _error_code = 208
    _message = "Already Reported"
    _description = ""


class HTTP_226_IM_USED(HTTPStatus):
    _error_code = 226
    _message = "IM Used"
    _description = ""


# 3xx Redirection
class HTTP_300_MULTIPLE_CHOICES(HTTPStatus):
    _error_code = 300
    _message = "Multiple Choices"
    _description = ""


class HTTP_301_MOVED_PERMANENTLY(HTTPStatus):
    _error_code = 301
    _message = "Moved Permanently"
    _description = ""


class HTTP_302_FOUND(HTTPStatus):
    _error_code = 302
    _message = "Found"
    _description = ""


class HTTP_303_SEE_OTHER(HTTPStatus):
    _error_code = 303
    _message = "See Other"
    _description = ""


class HTTP_304_NOT_MODIFIED(HTTPStatus):
    _error_code = 304
    _message = "Not Modified"
    _description = ""


class HTTP_305_USE_PROXY(HTTPStatus):
    _error_code = 305
    _message = "Use Proxy"
    _description = ""


class HTTP_307_TEMPORARY_REDIRECT(HTTPStatus):
    _error_code = 307
    _message = "Temporary Redirect"
    _description = ""


class HTTP_308_PERMANENT_REDIRECT(HTTPStatus):
    _error_code = 308
    _message = "Permanent Redirect"
    _description = ""


# 4xx Client Errors
class HTTP_400_BAD_REQUEST(HTTPStatus):
    _error_code = 400
    _message = "Bad Request"
    _description = ""


class HTTP_401_UNAUTHORIZED(HTTPStatus):
    _error_code = 401
    _message = "Unauthorized"
    _description = ""


class HTTP_402_PAYMENT_REQUIRED(HTTPStatus):
    _error_code = 402
    _message = "Payment Required"
    _description = ""


class HTTP_403_FORBIDDEN(HTTPStatus):
    _error_code = 403
    _message = "Forbidden"
    _description = ""


class HTTP_404_NOT_FOUND(HTTPStatus):
    _error_code = 404
    _message = "Not Found"
    _description = ""


class HTTP_405_METHOD_NOT_ALLOWED(HTTPStatus):
    _error_code = 405
    _message = "Method Not Allowed"
    _description = ""


class HTTP_406_NOT_ACCEPTABLE(HTTPStatus):
    _error_code = 406
    _message = "Not Acceptable"
    _description = ""


class HTTP_407_PROXY_AUTHENTICATION_REQUIRED(HTTPStatus):
    _error_code = 407
    _message = "Proxy Authentication Required"
    _description = ""


class HTTP_408_REQUEST_TIMEOUT(HTTPStatus):
    _error_code = 408
    _message = "Request Timeout"
    _description = ""


class HTTP_409_CONFLICT(HTTPStatus):
    _error_code = 409
    _message = "Conflict"
    _description = ""


class HTTP_410_GONE(HTTPStatus):
    _error_code = 410
    _message = "Gone"
    _description = ""


class HTTP_411_LENGTH_REQUIRED(HTTPStatus):
    _error_code = 411
    _message = "Length Required"
    _description = ""


class HTTP_412_PRECONDITION_FAILED(HTTPStatus):
    _error_code = 412
    _message = "Precondition Failed"
    _description = ""


class HTTP_413_PAYLOAD_TOO_LARGE(HTTPStatus):
    _error_code = 413
    _message = "Payload Too Large"
    _description = ""


class HTTP_414_URI_TOO_LONG(HTTPStatus):
    _error_code = 414
    _message = "URI Too Long"
    _description = ""


class HTTP_415_UNSUPPORTED_MEDIA_TYPE(HTTPStatus):
    _error_code = 415
    _message = "Unsupported Media Type"
    _description = ""


class HTTP_416_RANGE_NOT_SATISFIABLE(HTTPStatus):
    _error_code = 416
    _message = "Range Not Satisfiable"
    _description = ""


class HTTP_417_EXPECTATION_FAILED(HTTPStatus):
    _error_code = 417
    _message = "Expectation Failed"
    _description = ""


class HTTP_418_IM_A_TEAPOT(HTTPStatus):
    _error_code = 418
    _message = "I'm a teapot"
    _description = ""


class HTTP_421_MISDIRECTED_REQUEST(HTTPStatus):
    _error_code = 421
    _message = "Misdirected Request"
    _description = ""


class HTTP_422_UNPROCESSABLE_ENTITY(HTTPStatus):
    _error_code = 422
    _message = "Unprocessable Entity"
    _description = ""


class HTTP_423_LOCKED(HTTPStatus):
    _error_code = 423
    _message = "Locked"
    _description = ""


class HTTP_424_FAILED_DEPENDENCY(HTTPStatus):
    _error_code = 424
    _message = "Failed Dependency"
    _description = ""


class HTTP_425_TOO_EARLY(HTTPStatus):
    _error_code = 425
    _message = "Too Early"
    _description = ""


class HTTP_426_UPGRADE_REQUIRED(HTTPStatus):
    _error_code = 426
    _message = "Upgrade Required"
    _description = ""


class HTTP_428_PRECONDITION_REQUIRED(HTTPStatus):
    _error_code = 428
    _message = "Precondition Required"
    _description = ""


class HTTP_429_TOO_MANY_REQUESTS(HTTPStatus):
    _error_code = 429
    _message = "Too Many Requests"
    _description = ""


class HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE(HTTPStatus):
    _error_code = 431
    _message = "Request Header Fields Too Large"
    _description = ""


class HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS(HTTPStatus):
    _error_code = 451
    _message = "Unavailable For Legal Reasons"
    _description = ""


# 5xx Server Errors
class HTTP_500_INTERNAL_SERVER_ERROR(HTTPStatus):
    _error_code = 500
    _message = "Internal Server Error"


class HTTP_501_NOT_IMPLEMENTED(HTTPStatus):
    _error_code = 501
    _message = "Not Implemented"


class HTTP_502_BAD_GATEWAY(HTTPStatus):
    _error_code = 502
    _message = "Bad Gateway"


class HTTP_503_SERVICE_UNAVAILABLE(HTTPStatus):
    _error_code = 503
    _message = "Service Unavailable"


class HTTP_504_GATEWAY_TIMEOUT(HTTPStatus):
    _error_code = 504
    _message = "Gateway Timeout"


class HTTP_505_HTTP_VERSION_NOT_SUPPORTED(HTTPStatus):
    _error_code = 505
    _message = "HTTP Version Not Supported"


class HTTP_506_VARIANT_ALSO_NEGOTIATES(HTTPStatus):
    _error_code = 506
    _message = "Variant Also Negotiates"


class HTTP_507_INSUFFICIENT_STORAGE(HTTPStatus):
    _error_code = 507
    _message = "Insufficient Storage"


class HTTP_508_LOOP_DETECTED(HTTPStatus):
    _error_code = 508
    _message = "Loop Detected"


class HTTP_510_NOT_EXTENDED(HTTPStatus):
    _error_code = 510
    _message = "Not Extended"


class HTTP_511_NETWORK_AUTHENTICATION_REQUIRED(HTTPStatus):
    _error_code = 511
    _message = "Network Authentication Required"


# Define relevant error groups
HTTP_INFORMATIONAL = create_error_group(
    HTTP_100_CONTINUE,
    HTTP_101_SWITCHING_PROTOCOLS,
    HTTP_102_PROCESSING,
)

HTTP_SUCCESS = create_error_group(
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    HTTP_204_NO_CONTENT,
    HTTP_205_RESET_CONTENT,
    HTTP_206_PARTIAL_CONTENT,
    HTTP_207_MULTI_STATUS,
    HTTP_208_ALREADY_REPORTED,
    HTTP_226_IM_USED,
)

HTTP_REDIRECTION = create_error_group(
    HTTP_300_MULTIPLE_CHOICES,
    HTTP_301_MOVED_PERMANENTLY,
    HTTP_302_FOUND,
    HTTP_303_SEE_OTHER,
    HTTP_304_NOT_MODIFIED,
    HTTP_305_USE_PROXY,
    HTTP_307_TEMPORARY_REDIRECT,
    HTTP_308_PERMANENT_REDIRECT,
)

HTTP_CLIENT_ERRORS = create_error_group(
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_429_TOO_MANY_REQUESTS,
)

HTTP_SERVER_ERRORS = create_error_group(
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_502_BAD_GATEWAY,
    HTTP_503_SERVICE_UNAVAILABLE,
    HTTP_504_GATEWAY_TIMEOUT,
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
)
