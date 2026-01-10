"""A Python module providing HTTP status code constants and exceptions.

This module defines a comprehensive set of HTTP status codes as exception
classes, allowing for both error handling and status code validation. Each
status code is represented by a class inheriting from HTTPStatus, containing
the numeric code, message, and description.

The module provides status codes in the following categories:
    - 1xx: Informational responses (100-102)
    - 2xx: Success responses (200-208, 226)
    - 3xx: Redirection responses (300-308)
    - 4xx: Client error responses (400-431, 451)
    - 5xx: Server error responses (500-511)

Each status code class provides:
    - status_code: The numeric HTTP status code
    - message: The standard HTTP status message
    - description: A detailed description of the status code (where
      applicable)

The module also provides predefined groups of related status codes via the
create_status_group() utility function:
    - HTTP_INFORMATIONAL: 1xx status codes
    - HTTP_SUCCESS: 2xx status codes
    - HTTP_REDIRECTION: 3xx status codes
    - HTTP_CLIENT_ERRORS: Common 4xx status codes
    - HTTP_SERVER_ERRORS: Common 5xx status codes
"""

# 1xx Informational responses
from ._1xx_informational import (
    HTTP_100_CONTINUE,
    HTTP_101_SWITCHING_PROTOCOLS,
    HTTP_102_PROCESSING,
)

# 2xx Success responses
from ._2xx_success import (
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

# 3xx Redirection responses
from ._3xx_redirection import (
    HTTP_300_MULTIPLE_CHOICES,
    HTTP_301_MOVED_PERMANENTLY,
    HTTP_302_FOUND,
    HTTP_303_SEE_OTHER,
    HTTP_304_NOT_MODIFIED,
    HTTP_305_USE_PROXY,
    HTTP_307_TEMPORARY_REDIRECT,
    HTTP_308_PERMANENT_REDIRECT,
)

# 4xx Client error responses
from ._4xx_client_errors import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_402_PAYMENT_REQUIRED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_409_CONFLICT,
    HTTP_410_GONE,
    HTTP_411_LENGTH_REQUIRED,
    HTTP_412_PRECONDITION_FAILED,
    HTTP_413_PAYLOAD_TOO_LARGE,
    HTTP_414_URI_TOO_LONG,
    HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    HTTP_416_RANGE_NOT_SATISFIABLE,
    HTTP_417_EXPECTATION_FAILED,
    HTTP_418_IM_A_TEAPOT,
    HTTP_421_MISDIRECTED_REQUEST,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_423_LOCKED,
    HTTP_424_FAILED_DEPENDENCY,
    HTTP_425_TOO_EARLY,
    HTTP_426_UPGRADE_REQUIRED,
    HTTP_428_PRECONDITION_REQUIRED,
    HTTP_429_TOO_MANY_REQUESTS,
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE,
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
)

# 5xx Server error responses
from ._5xx_server_errors import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_502_BAD_GATEWAY,
    HTTP_503_SERVICE_UNAVAILABLE,
    HTTP_504_GATEWAY_TIMEOUT,
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED,
    HTTP_506_VARIANT_ALSO_NEGOTIATES,
    HTTP_507_INSUFFICIENT_STORAGE,
    HTTP_508_LOOP_DETECTED,
    HTTP_510_NOT_EXTENDED,
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
)

# Core infrastructure
from ._core import HTTPStatus, HTTPStatusMeta, create_status_group

# Predefined status code groups
from ._groups import (
    HTTP_CLIENT_ERRORS,
    HTTP_INFORMATIONAL,
    HTTP_REDIRECTION,
    HTTP_SERVER_ERRORS,
    HTTP_SUCCESS,
)

__all__ = [
    # Core classes and utilities
    "HTTPStatus",
    "HTTPStatusMeta",
    "create_status_group",
    # 1xx Informational
    "HTTP_100_CONTINUE",
    "HTTP_101_SWITCHING_PROTOCOLS",
    "HTTP_102_PROCESSING",
    # 2xx Success
    "HTTP_200_OK",
    "HTTP_201_CREATED",
    "HTTP_202_ACCEPTED",
    "HTTP_203_NON_AUTHORITATIVE_INFORMATION",
    "HTTP_204_NO_CONTENT",
    "HTTP_205_RESET_CONTENT",
    "HTTP_206_PARTIAL_CONTENT",
    "HTTP_207_MULTI_STATUS",
    "HTTP_208_ALREADY_REPORTED",
    "HTTP_226_IM_USED",
    # 3xx Redirection
    "HTTP_300_MULTIPLE_CHOICES",
    "HTTP_301_MOVED_PERMANENTLY",
    "HTTP_302_FOUND",
    "HTTP_303_SEE_OTHER",
    "HTTP_304_NOT_MODIFIED",
    "HTTP_305_USE_PROXY",
    "HTTP_307_TEMPORARY_REDIRECT",
    "HTTP_308_PERMANENT_REDIRECT",
    # 4xx Client Errors
    "HTTP_400_BAD_REQUEST",
    "HTTP_401_UNAUTHORIZED",
    "HTTP_402_PAYMENT_REQUIRED",
    "HTTP_403_FORBIDDEN",
    "HTTP_404_NOT_FOUND",
    "HTTP_405_METHOD_NOT_ALLOWED",
    "HTTP_406_NOT_ACCEPTABLE",
    "HTTP_407_PROXY_AUTHENTICATION_REQUIRED",
    "HTTP_408_REQUEST_TIMEOUT",
    "HTTP_409_CONFLICT",
    "HTTP_410_GONE",
    "HTTP_411_LENGTH_REQUIRED",
    "HTTP_412_PRECONDITION_FAILED",
    "HTTP_413_PAYLOAD_TOO_LARGE",
    "HTTP_414_URI_TOO_LONG",
    "HTTP_415_UNSUPPORTED_MEDIA_TYPE",
    "HTTP_416_RANGE_NOT_SATISFIABLE",
    "HTTP_417_EXPECTATION_FAILED",
    "HTTP_418_IM_A_TEAPOT",
    "HTTP_421_MISDIRECTED_REQUEST",
    "HTTP_422_UNPROCESSABLE_ENTITY",
    "HTTP_423_LOCKED",
    "HTTP_424_FAILED_DEPENDENCY",
    "HTTP_425_TOO_EARLY",
    "HTTP_426_UPGRADE_REQUIRED",
    "HTTP_428_PRECONDITION_REQUIRED",
    "HTTP_429_TOO_MANY_REQUESTS",
    "HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE",
    "HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS",
    # 5xx Server Errors
    "HTTP_500_INTERNAL_SERVER_ERROR",
    "HTTP_501_NOT_IMPLEMENTED",
    "HTTP_502_BAD_GATEWAY",
    "HTTP_503_SERVICE_UNAVAILABLE",
    "HTTP_504_GATEWAY_TIMEOUT",
    "HTTP_505_HTTP_VERSION_NOT_SUPPORTED",
    "HTTP_506_VARIANT_ALSO_NEGOTIATES",
    "HTTP_507_INSUFFICIENT_STORAGE",
    "HTTP_508_LOOP_DETECTED",
    "HTTP_510_NOT_EXTENDED",
    "HTTP_511_NETWORK_AUTHENTICATION_REQUIRED",
    # Predefined groups
    "HTTP_INFORMATIONAL",
    "HTTP_SUCCESS",
    "HTTP_REDIRECTION",
    "HTTP_CLIENT_ERRORS",
    "HTTP_SERVER_ERRORS",
]
