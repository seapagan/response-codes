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
"""

from __future__ import annotations


class HTTPStatusMeta(type):
    """Base meta-class for HTTP status code exceptions.

    This class serves as the meta-class for the base HTTPStatus class.

    Attributes:
        status_code (int): The numeric HTTP status code
        message (str): The standard HTTP status message
        description (str): A detailed description of the status code
    """

    def __init__(
        cls, name: str, bases: tuple[type, ...], namespace: dict[str, object]
    ) -> None:
        """Initialize the HTTP status exception class."""
        super().__init__(name, bases, namespace)
        # Ensure required attributes exist with default values
        if not hasattr(cls, "status_code"):
            cls.status_code = 0
        if not hasattr(cls, "message"):
            cls.message = ""
        if not hasattr(cls, "description"):
            cls.description = ""

    def __int__(cls) -> int:
        """Convert the status code to an integer.

        Returns:
            int: The numeric HTTP status code
        """
        return cls.status_code

    def __str__(cls) -> str:
        """Convert the status code to a string.

        Returns:
            str: The HTTP status message
        """
        return cls.message

    def __eq__(cls, other: object) -> bool:
        """Compare equality with another object.

        Returns True if other is an integer matching the status code or a string
        matching the message.

        Args:
            other: Object to compare with

        Returns:
            bool: True if objects are equal, False otherwise
        """
        if isinstance(other, int):
            return cls.status_code == other
        if isinstance(other, str):
            return cls.message == other
        return False

    def __lt__(cls, other: int) -> bool:
        """Compare if status code is less than another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is less than other, False otherwise
        """
        if isinstance(other, int):
            return cls.status_code < other
        return NotImplemented

    def __le__(cls, other: int) -> bool:
        """Compare if status code is less than or equal to another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is less than or equal to other
        """
        if isinstance(other, int):
            return cls.status_code <= other
        return NotImplemented

    def __gt__(cls, other: int) -> bool:
        """Compare if status code is greater than another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is greater than other
        """
        if isinstance(other, int):
            return cls.status_code > other
        return NotImplemented

    def __ge__(cls, other: int) -> bool:
        """Compare if status code is greater than or equal to another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is greater than or equal to other
        """
        if isinstance(other, int):
            return cls.status_code >= other
        return NotImplemented


class HTTPStatus(Exception, metaclass=HTTPStatusMeta):
    """Base class for HTTP status code exceptions.

    This class serves as the foundation for all HTTP status code exceptions,
    providing common functionality for status code handling and comparison.

    Attributes:
        status_code (int): The numeric HTTP status code
        message (str): The standard HTTP status message
        description (str): A detailed description of the status code

    Examples:
        >>> status = HTTP_404_NOT_FOUND()
        >>> status.status_code
        404
        >>> status.message
        'Not Found'
    """

    status_code: int = 0
    message: str = ""
    description: str = ""

    def __init__(self) -> None:
        """Initialize the HTTP status exception with a formatted message."""
        super().__init__(self.message)


# Utility function to create custom groups
def create_status_group(
    *status_classes: type[HTTPStatus],
) -> dict[int, type[HTTPStatus]]:
    """Create a custom status group as a dictionary."""
    return {
        status_class.status_code: status_class
        for status_class in status_classes
    }


# 1xx Informational Responses
class HTTP_100_CONTINUE(HTTPStatus):
    """100 Continue response status code.

    Indicates that the initial part of a request has been received and has not
    yet been rejected by the server. The server intends to send a final response
    after the request has been fully received and acted upon.
    """

    status_code = 100
    message = "Continue"
    description = (
        "The server has received the request headers and the client"
        " should proceed to send the request body."
    )


class HTTP_101_SWITCHING_PROTOCOLS(HTTPStatus):
    """101 Switching Protocols response status code.

    Indicates the server understands and is willing to comply with the client's
    request, via the Upgrade header field, for a change in the application
    protocol being used on this connection.
    """

    status_code = 101
    message = "Switching Protocols"
    description = "The requester has asked the server to switch protocols."


class HTTP_102_PROCESSING(HTTPStatus):
    """102 Processing response status code.

    Indicates that the server has received and is processing the request, but no
    response is available yet. This prevents the client from timing out and
    assuming the request was lost.
    """

    status_code = 102
    message = "Processing"
    description = (
        "The server is processing the request but no response is available yet."
    )


# 2xx Success
class HTTP_200_OK(HTTPStatus):
    """200 OK response status code.

    Indicates that the request has succeeded. The payload sent in a 200 response
    depends on the request method.
    """

    status_code = 200
    message = "OK"
    description = (
        "The request has succeeded and the response contains the "
        "requested data."
    )


class HTTP_201_CREATED(HTTPStatus):
    """201 Created response status code.

    Indicates that the request has been fulfilled and has resulted in one or
    more
    new resources being created.
    """

    status_code = 201
    message = "Created"
    description = (
        "The request has succeeded and a new resource has been created."
    )


class HTTP_202_ACCEPTED(HTTPStatus):
    """202 Accepted response status code.

    Indicates that the request has been accepted for processing, but the
    processing has not been completed. The request might or might not eventually
    be acted upon.
    """

    status_code = 202
    message = "Accepted"
    description = (
        "The request has been accepted for processing but has not "
        "been completed."
    )


class HTTP_203_NON_AUTHORITATIVE_INFORMATION(HTTPStatus):
    """203 Non-Authoritative Information response status code.

    Indicates that the request was successful but the enclosed payload has been
    modified by a transforming proxy from that of the origin server's 200 OK
    response.
    """

    status_code = 203
    message = "Non-Authoritative Information"
    description = (
        "The response has been transformed by a proxy from the "
        "origin server's response."
    )


class HTTP_204_NO_CONTENT(HTTPStatus):
    """204 No Content response status code.

    Indicates that the server has successfully fulfilled the request and that
    there is no additional content to send in the response payload body.
    """

    status_code = 204
    message = "No Content"
    description = (
        "The request succeeded but there is no content to send in the response."
    )


class HTTP_205_RESET_CONTENT(HTTPStatus):
    """205 Reset Content response status code.

    Indicates that the server has fulfilled the request and desires that the
    user agent reset the "document view" that caused the request to be sent.
    """

    status_code = 205
    message = "Reset Content"
    description = (
        "The client should reset the document view that caused this request."
    )


class HTTP_206_PARTIAL_CONTENT(HTTPStatus):
    """206 Partial Content response status code.

    Indicates that the server is successfully fulfilling a range request for the
    target resource by transferring one or more parts of the selected
    representation.
    """

    status_code = 206
    message = "Partial Content"
    description = (
        "The server is delivering only part of the resource due "
        "to a range header sent by the client."
    )


class HTTP_207_MULTI_STATUS(HTTPStatus):
    """207 Multi-Status response status code.

    Provides status for multiple independent operations in a single response.
    Typically used with WebDAV.
    """

    status_code = 207
    message = "Multi-Status"
    description = "Multiple status codes might be appropriate for the response."


class HTTP_208_ALREADY_REPORTED(HTTPStatus):
    """208 Already Reported response status code.

    Used inside a DAV: propstat response element to avoid enumerating the
    internal members of multiple bindings to the same collection repeatedly.
    """

    status_code = 208
    message = "Already Reported"
    description = (
        "The members of a DAV binding have already been enumerated "
        "in a preceding part of the response."
    )


class HTTP_226_IM_USED(HTTPStatus):
    """226 IM Used response status code.

    The server has fulfilled a GET request for the resource, and the response is
    a representation of the result of one or more instance-manipulations applied
    to the current instance.
    """

    status_code = 226
    message = "IM Used"
    description = (
        "The server has fulfilled a GET request for the "
        "resource using an instance manipulation."
    )


# 3xx Redirection
class HTTP_300_MULTIPLE_CHOICES(HTTPStatus):
    """300 Multiple Choices response status code.

    Indicates that the target resource has more than one representation, each
    with its own more specific identifier, and information about the
    alternatives is being provided so that the user can select a preferred
    representation.
    """

    status_code = 300
    message = "Multiple Choices"
    description = (
        "The requested resource has multiple representations available."
    )


class HTTP_301_MOVED_PERMANENTLY(HTTPStatus):
    """301 Moved Permanently response status code.

    Indicates that the target resource has been assigned a new permanent URI and
    any future references to this resource ought to use one of the enclosed
    URIs.
    """

    status_code = 301
    message = "Moved Permanently"
    description = (
        "The requested resource has been permanently moved to a new URL."
    )


class HTTP_302_FOUND(HTTPStatus):
    """302 Found response status code.

    Indicates that the target resource resides temporarily under a different
    URI. Since the redirection might be altered on occasion, the client ought to
    continue to use the effective request URI for future requests.
    """

    status_code = 302
    message = "Found"
    description = (
        "The requested resource temporarily resides under a different URL."
    )


class HTTP_303_SEE_OTHER(HTTPStatus):
    """303 See Other response status code.

    Indicates that the server is redirecting the user agent to a different
    resource, as indicated by a URI in the Location header field, which is
    intended to provide an indirect response to the original request.
    """

    status_code = 303
    message = "See Other"
    description = (
        "The response to the request can be found under a different URL."
    )


class HTTP_304_NOT_MODIFIED(HTTPStatus):
    """304 Not Modified response status code.

    Indicates that a conditional GET or HEAD request has been received and would
    have resulted in a 200 OK response if it were not for the fact that the
    condition evaluated to false.
    """

    status_code = 304
    message = "Not Modified"
    description = "The resource has not been modified since the last request."


class HTTP_305_USE_PROXY(HTTPStatus):
    """305 Use Proxy response status code.

    Deprecated status code that indicated that the requested resource must be
    accessed through the proxy given by the Location header field.
    """

    status_code = 305
    message = "Use Proxy"
    description = (
        "The requested resource must be accessed through the specified proxy."
    )


class HTTP_307_TEMPORARY_REDIRECT(HTTPStatus):
    """307 Temporary Redirect response status code.

    Indicates that the target resource resides temporarily under a different URI
    and the user agent MUST NOT change the request method if it performs an
    automatic redirection to that URI.
    """

    status_code = 307
    message = "Temporary Redirect"
    description = (
        "The requested resource temporarily resides under a different URL."
    )


class HTTP_308_PERMANENT_REDIRECT(HTTPStatus):
    """308 Permanent Redirect response status code.

    Indicates that the target resource has been assigned a new permanent URI and
    any future references should use one of the enclosed URIs. The user agent
    MUST NOT change the request method.
    """

    status_code = 308
    message = "Permanent Redirect"
    description = (
        "The requested resource has been permanently moved to another URL."
    )


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

    Reserved for future use. The original intention was that this code might be
    used as part of some form of digital cash or micropayment scheme.
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

    Indicates that the server did not receive a complete request message within
    the time that it was prepared to wait.
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

    Indicates that the source or destination resource of a method is locked and
    the method cannot be completed.
    """

    status_code = 423
    message = "Locked"
    description = "The requested resource is locked and cannot be accessed."


class HTTP_424_FAILED_DEPENDENCY(HTTPStatus):
    """424 Failed Dependency response status code.

    Indicates that the method could not be performed on the resource because the
    requested action depended on another action and that action failed.
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

    Indicates that the server is denying access to the resource as a consequence
    of a legal demand.
    """

    status_code = 451
    message = "Unavailable For Legal Reasons"
    description = "The server is denying access due to legal reasons."


# 5xx Server Errors
class HTTP_500_INTERNAL_SERVER_ERROR(HTTPStatus):
    """500 Internal Server Error response status code.

    Indicates that the server encountered an unexpected condition that prevented
    it from fulfilling the request.
    """

    status_code = 500
    message = "Internal Server Error"
    description = (
        "The server encountered an unexpected condition that "
        "prevented fulfilling the request."
    )


class HTTP_501_NOT_IMPLEMENTED(HTTPStatus):
    """501 Not Implemented response status code.

    Indicates that the server does not support the functionality required to
    fulfill the request.
    """

    status_code = 501
    message = "Not Implemented"
    description = (
        "The server does not support the functionality required "
        "to fulfill the request."
    )


class HTTP_502_BAD_GATEWAY(HTTPStatus):
    """502 Bad Gateway response status code.

    Indicates that the server, while acting as a gateway or proxy, received an
    invalid response from an inbound server it accessed while attempting to
    fulfill the request.
    """

    status_code = 502
    message = "Bad Gateway"
    description = (
        "The server received an invalid response from the upstream server."
    )


class HTTP_503_SERVICE_UNAVAILABLE(HTTPStatus):
    """503 Service Unavailable response status code.

    Indicates that the server is currently unable to handle the request due to a
    temporary overload or scheduled maintenance.
    """

    status_code = 503
    message = "Service Unavailable"
    description = "The server is temporarily unable to handle the request."


class HTTP_504_GATEWAY_TIMEOUT(HTTPStatus):
    """504 Gateway Timeout response status code.

    Indicates that the server, while acting as a gateway or proxy, did not
    receive a timely response from an upstream server it needed to access in
    order to complete the request.
    """

    status_code = 504
    message = "Gateway Timeout"
    description = (
        "The gateway server did not receive a timely response "
        "from the upstream server."
    )


class HTTP_505_HTTP_VERSION_NOT_SUPPORTED(HTTPStatus):
    """505 HTTP Version Not Supported response status code.

    Indicates that the server does not support, or refuses to support, the major
    version of HTTP that was used in the request message.
    """

    status_code = 505
    message = "HTTP Version Not Supported"
    description = (
        "The server does not support the HTTP protocol version "
        "used in the request."
    )


class HTTP_506_VARIANT_ALSO_NEGOTIATES(HTTPStatus):
    """506 Variant Also Negotiates response status code.

    Indicates that the server has an internal configuration error: the chosen
    variant resource is configured to engage in transparent content negotiation
    itself.
    """

    status_code = 506
    message = "Variant Also Negotiates"
    description = "The server has a configuration error in content negotiation."


class HTTP_507_INSUFFICIENT_STORAGE(HTTPStatus):
    """507 Insufficient Storage response status code.

    Indicates that the server is unable to store the representation needed to
    complete the request.
    """

    status_code = 507
    message = "Insufficient Storage"
    description = (
        "The server is unable to store the representation needed "
        "to complete the request."
    )


class HTTP_508_LOOP_DETECTED(HTTPStatus):
    """508 Loop Detected response status code.

    Indicates that the server terminated an operation because it encountered an
    infinite loop while processing a request.
    """

    status_code = 508
    message = "Loop Detected"
    description = (
        "The server detected an infinite loop while processing the request."
    )


class HTTP_510_NOT_EXTENDED(HTTPStatus):
    """510 Not Extended response status code.

    Indicates that further extensions to the request are required for the server
    to fulfill it.
    """

    status_code = 510
    message = "Not Extended"
    description = (
        "Further extensions to the request are required for the "
        "server to fulfill it."
    )


class HTTP_511_NETWORK_AUTHENTICATION_REQUIRED(HTTPStatus):
    """511 Network Authentication Required response status code.

    Indicates that the client needs to authenticate to gain network access. This
    status code is not generated by origin servers but by intercepting proxies.
    """

    status_code = 511
    message = "Network Authentication Required"
    description = "The client needs to authenticate to gain network access."


# Define relevant error groups
HTTP_INFORMATIONAL = create_status_group(
    HTTP_100_CONTINUE,
    HTTP_101_SWITCHING_PROTOCOLS,
    HTTP_102_PROCESSING,
)

HTTP_SUCCESS = create_status_group(
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

HTTP_REDIRECTION = create_status_group(
    HTTP_300_MULTIPLE_CHOICES,
    HTTP_301_MOVED_PERMANENTLY,
    HTTP_302_FOUND,
    HTTP_303_SEE_OTHER,
    HTTP_304_NOT_MODIFIED,
    HTTP_305_USE_PROXY,
    HTTP_307_TEMPORARY_REDIRECT,
    HTTP_308_PERMANENT_REDIRECT,
)

HTTP_CLIENT_ERRORS = create_status_group(
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_408_REQUEST_TIMEOUT,
    HTTP_429_TOO_MANY_REQUESTS,
)

HTTP_SERVER_ERRORS = create_status_group(
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_502_BAD_GATEWAY,
    HTTP_503_SERVICE_UNAVAILABLE,
    HTTP_504_GATEWAY_TIMEOUT,
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
)
