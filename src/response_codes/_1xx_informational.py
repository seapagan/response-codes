"""1xx Informational HTTP status codes.

This module contains HTTP status code exceptions for informational responses
(100-102).
"""

from ._core import HTTPStatus


# 1xx Informational Responses
class HTTP_100_CONTINUE(HTTPStatus):
    """100 Continue response status code.

    Indicates that the initial part of a request has been received and has not
    yet been rejected by the server. The server intends to send a final
    response after the request has been fully received and acted upon.
    """

    status_code = 100
    message = "Continue"
    description = (
        "The server has received the request headers and the client"
        " should proceed to send the request body."
    )


class HTTP_101_SWITCHING_PROTOCOLS(HTTPStatus):
    """101 Switching Protocols response status code.

    Indicates the server understands and is willing to comply with the
    client's request, via the Upgrade header field, for a change in the
    application protocol being used on this connection.
    """

    status_code = 101
    message = "Switching Protocols"
    description = "The requester has asked the server to switch protocols."


class HTTP_102_PROCESSING(HTTPStatus):
    """102 Processing response status code.

    Indicates that the server has received and is processing the request, but
    no response is available yet. This prevents the client from timing out and
    assuming the request was lost.
    """

    status_code = 102
    message = "Processing"
    description = (
        "The server is processing the request but no response is available yet."
    )


class HTTP_103_EARLY_HINTS(HTTPStatus):
    """103 Early Hints response status code.

    Indicates to the client that the server is likely to send a final response
    with the headers included in the informational response. This allows the
    client to begin preloading resources while the server is still preparing
    the final response.
    """

    status_code = 103
    message = "Early Hints"
    description = (
        "The server is likely to send a final response with the included "
        "headers, allowing the client to preload resources."
    )


__all__ = [
    "HTTP_100_CONTINUE",
    "HTTP_101_SWITCHING_PROTOCOLS",
    "HTTP_102_PROCESSING",
    "HTTP_103_EARLY_HINTS",
]
