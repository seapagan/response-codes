"""3xx Redirection HTTP status codes.

This module contains HTTP status code exceptions for redirection responses
(300-308).
"""

from ._core import HTTPStatus


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

    Indicates that the target resource has been assigned a new permanent URI
    and any future references to this resource ought to use one of the
    enclosed URIs.
    """

    status_code = 301
    message = "Moved Permanently"
    description = (
        "The requested resource has been permanently moved to a new URL."
    )


class HTTP_302_FOUND(HTTPStatus):
    """302 Found response status code.

    Indicates that the target resource resides temporarily under a different
    URI. Since the redirection might be altered on occasion, the client ought
    to continue to use the effective request URI for future requests.
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

    Indicates that a conditional GET or HEAD request has been received and
    would have resulted in a 200 OK response if it were not for the fact that
    the condition evaluated to false.
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

    Indicates that the target resource resides temporarily under a different
    URI and the user agent MUST NOT change the request method if it performs
    an automatic redirection to that URI.
    """

    status_code = 307
    message = "Temporary Redirect"
    description = (
        "The requested resource temporarily resides under a different URL."
    )


class HTTP_308_PERMANENT_REDIRECT(HTTPStatus):
    """308 Permanent Redirect response status code.

    Indicates that the target resource has been assigned a new permanent URI
    and any future references should use one of the enclosed URIs. The user
    agent MUST NOT change the request method.
    """

    status_code = 308
    message = "Permanent Redirect"
    description = (
        "The requested resource has been permanently moved to another URL."
    )


__all__ = [
    "HTTP_300_MULTIPLE_CHOICES",
    "HTTP_301_MOVED_PERMANENTLY",
    "HTTP_302_FOUND",
    "HTTP_303_SEE_OTHER",
    "HTTP_304_NOT_MODIFIED",
    "HTTP_305_USE_PROXY",
    "HTTP_307_TEMPORARY_REDIRECT",
    "HTTP_308_PERMANENT_REDIRECT",
]
