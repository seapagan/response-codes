"""4xx Client Error HTTP status codes.

This module contains HTTP status code exceptions for client error responses
(400-431, 451).
"""

from ._core import HTTPStatus


# 4xx Client Errors
class HTTP_400_BAD_REQUEST(HTTPStatus):
    """400 Bad Request response status code.

    Indicates that the server cannot or will not process the request due to
    something that is perceived to be a client error (e.g., malformed request
    syntax, invalid request message framing, or deceptive request routing).
    """

    status_code = 400
    message = "Bad Request"
    description = "The server cannot process the request due to a client error."


class HTTP_401_UNAUTHORIZED(HTTPStatus):
    """401 Unauthorized response status code.

    Indicates that the request has not been applied because it lacks valid
    authentication credentials for the target resource.
    """

    status_code = 401
    message = "Unauthorized"
    description = "The request requires user authentication."


class HTTP_402_PAYMENT_REQUIRED(HTTPStatus):
    """402 Payment Required response status code.

    Reserved for future use. The original intention was that this code might
    be used as part of some form of digital cash or micropayment scheme.
    """

    status_code = 402
    message = "Payment Required"
    description = "Reserved for future use in digital payment systems."


class HTTP_403_FORBIDDEN(HTTPStatus):
    """403 Forbidden response status code.

    Indicates that the server understood the request but refuses to authorize
    it. Unlike 401 Unauthorized, authenticating will make no difference.
    """

    status_code = 403
    message = "Forbidden"
    description = (
        "The server understood the request but refuses to authorize it."
    )


class HTTP_404_NOT_FOUND(HTTPStatus):
    """404 Not Found response status code.

    Indicates that the server cannot find the requested resource. Links that
    lead to a 404 page are often called broken or dead links.
    """

    status_code = 404
    message = "Not Found"
    description = "The requested resource could not be found on the server."


class HTTP_405_METHOD_NOT_ALLOWED(HTTPStatus):
    """405 Method Not Allowed response status code.

    Indicates that the method received in the request-line is known by the
    origin server but not supported by the target resource.
    """

    status_code = 405
    message = "Method Not Allowed"
    description = (
        "The request method is not supported for the requested resource."
    )


class HTTP_406_NOT_ACCEPTABLE(HTTPStatus):
    """406 Not Acceptable response status code.

    Indicates that the target resource does not have a current representation
    that would be acceptable to the user agent, according to the proactive
    negotiation header fields received in the request.
    """

    status_code = 406
    message = "Not Acceptable"
    description = (
        "The requested resource cannot generate content acceptable "
        "to the client."
    )


class HTTP_407_PROXY_AUTHENTICATION_REQUIRED(HTTPStatus):
    """407 Proxy Authentication Required response status code.

    Similar to 401 Unauthorized, but it indicates that the client needs to
    authenticate itself in order to use a proxy.
    """

    status_code = 407
    message = "Proxy Authentication Required"
    description = "Authentication with the proxy server is required."


class HTTP_408_REQUEST_TIMEOUT(HTTPStatus):
    """408 Request Timeout response status code.

    Indicates that the server did not receive a complete request message
    within the time that it was prepared to wait.
    """

    status_code = 408
    message = "Request Timeout"
    description = "The server timed out waiting for the request."


class HTTP_409_CONFLICT(HTTPStatus):
    """409 Conflict response status code.

    Indicates that the request conflicts with the current state of the target
    resource.
    """

    status_code = 409
    message = "Conflict"
    description = "The request conflicts with the current state of the server."


class HTTP_410_GONE(HTTPStatus):
    """410 Gone response status code.

    Indicates that access to the target resource is no longer available at the
    origin server and that this condition is likely to be permanent.
    """

    status_code = 410
    message = "Gone"
    description = (
        "The requested resource is no longer available and will "
        "not be available again."
    )


class HTTP_411_LENGTH_REQUIRED(HTTPStatus):
    """411 Length Required response status code.

    Indicates that the server refuses to accept the request without a defined
    Content-Length header field.
    """

    status_code = 411
    message = "Length Required"
    description = "The request did not specify the length of its content."


class HTTP_412_PRECONDITION_FAILED(HTTPStatus):
    """412 Precondition Failed response status code.

    Indicates that one or more conditions given in the request header fields
    evaluated to false when tested on the server.
    """

    status_code = 412
    message = "Precondition Failed"
    description = (
        "Server does not meet one of the preconditions specified "
        "in the request headers."
    )


class HTTP_413_PAYLOAD_TOO_LARGE(HTTPStatus):
    """413 Payload Too Large response status code.

    Indicates that the server is refusing to process a request because the
    request payload is larger than the server is willing or able to process.
    """

    status_code = 413
    message = "Payload Too Large"
    description = (
        "The request payload is larger than the server is willing "
        "or able to process."
    )


class HTTP_414_URI_TOO_LONG(HTTPStatus):
    """414 URI Too Long response status code.

    Indicates that the server is refusing to service the request because the
    request-target is longer than the server is willing to interpret.
    """

    status_code = 414
    message = "URI Too Long"
    description = (
        "The URI requested by the client is longer than the server can process."
    )


class HTTP_415_UNSUPPORTED_MEDIA_TYPE(HTTPStatus):
    """415 Unsupported Media Type response status code.

    Indicates that the server is refusing to service the request because the
    payload format is in an unsupported format.
    """

    status_code = 415
    message = "Unsupported Media Type"
    description = (
        "The server does not support the media type transmitted in the request."
    )


class HTTP_416_RANGE_NOT_SATISFIABLE(HTTPStatus):
    """416 Range Not Satisfiable response status code.

    Indicates that none of the ranges in the request's Range header field
    overlap the current extent of the selected resource.
    """

    status_code = 416
    message = "Range Not Satisfiable"
    description = (
        "The client has asked for a portion of the file that "
        "lies beyond its end."
    )


class HTTP_417_EXPECTATION_FAILED(HTTPStatus):
    """417 Expectation Failed response status code.

    Indicates that the expectation given in the request's Expect header field
    could not be met by at least one of the inbound servers.
    """

    status_code = 417
    message = "Expectation Failed"
    description = (
        "The server cannot meet the requirements of the Expect "
        "request-header field."
    )


class HTTP_418_IM_A_TEAPOT(HTTPStatus):
    """418 I'm a teapot response status code.

    Any attempt to brew coffee with a teapot should result in this error code.
    This code is an April Fools joke from 1998.
    """

    status_code = 418
    message = "I'm a teapot"
    description = "The server refuses to brew coffee because it is a teapot."


class HTTP_421_MISDIRECTED_REQUEST(HTTPStatus):
    """421 Misdirected Request response status code.

    Indicates that the request was directed at a server that is not able to
    produce a response.
    """

    status_code = 421
    message = "Misdirected Request"
    description = (
        "The request was directed at a server that cannot produce a response."
    )


class HTTP_422_UNPROCESSABLE_ENTITY(HTTPStatus):
    """422 Unprocessable Entity response status code.

    Indicates that the server understands the content type of the request
    entity, and the syntax of the request entity is correct, but was unable to
    process the contained instructions.
    """

    status_code = 422
    message = "Unprocessable Entity"
    description = (
        "The request was well-formed but has semantic errors that "
        "prevent processing."
    )


class HTTP_423_LOCKED(HTTPStatus):
    """423 Locked response status code.

    Indicates that the source or destination resource of a method is locked
    and the method cannot be completed.
    """

    status_code = 423
    message = "Locked"
    description = "The requested resource is locked and cannot be accessed."


class HTTP_424_FAILED_DEPENDENCY(HTTPStatus):
    """424 Failed Dependency response status code.

    Indicates that the method could not be performed on the resource because
    the requested action depended on another action and that action failed.
    """

    status_code = 424
    message = "Failed Dependency"
    description = "The request failed due to failure of a previous request."


class HTTP_425_TOO_EARLY(HTTPStatus):
    """425 Too Early response status code.

    Indicates that the server is unwilling to risk processing a request that
    might be replayed, which creates the potential for a replay attack.
    """

    status_code = 425
    message = "Too Early"
    description = (
        "The server is unwilling to risk processing a request "
        "that might be replayed."
    )


class HTTP_426_UPGRADE_REQUIRED(HTTPStatus):
    """426 Upgrade Required response status code.

    Indicates that the server refuses to perform the request using the current
    protocol but might be willing to do so after the client upgrades to a
    different protocol.
    """

    status_code = 426
    message = "Upgrade Required"
    description = (
        "The client should switch to a different protocol "
        "specified in the Upgrade header."
    )


class HTTP_428_PRECONDITION_REQUIRED(HTTPStatus):
    """428 Precondition Required response status code.

    Indicates that the origin server requires the request to be conditional to
    prevent the 'lost update' problem.
    """

    status_code = 428
    message = "Precondition Required"
    description = "The origin server requires the request to be conditional."


class HTTP_429_TOO_MANY_REQUESTS(HTTPStatus):
    """429 Too Many Requests response status code.

    Indicates the user has sent too many requests in a given amount of time
    ("rate limiting").
    """

    status_code = 429
    message = "Too Many Requests"
    description = (
        "The user has sent too many requests in a given amount of time."
    )


class HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE(HTTPStatus):
    """431 Request Header Fields Too Large response status code.

    Indicates that the server is unwilling to process the request because its
    header fields are too large.
    """

    status_code = 431
    message = "Request Header Fields Too Large"
    description = (
        "The server is unwilling to process the request because "
        "its header fields are too large."
    )


class HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS(HTTPStatus):
    """451 Unavailable For Legal Reasons response status code.

    Indicates that the server is denying access to the resource as a
    consequence of a legal demand.
    """

    status_code = 451
    message = "Unavailable For Legal Reasons"
    description = "The server is denying access due to legal reasons."


__all__ = [
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
]
