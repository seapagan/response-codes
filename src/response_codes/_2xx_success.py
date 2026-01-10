"""2xx Success HTTP status codes.

This module contains HTTP status code exceptions for successful responses
(200-208, 226).
"""

from ._core import HTTPStatus


# 2xx Success
class HTTP_200_OK(HTTPStatus):
    """200 OK response status code.

    Indicates that the request has succeeded. The payload sent in a 200
    response depends on the request method.
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
    more new resources being created.
    """

    status_code = 201
    message = "Created"
    description = (
        "The request has succeeded and a new resource has been created."
    )


class HTTP_202_ACCEPTED(HTTPStatus):
    """202 Accepted response status code.

    Indicates that the request has been accepted for processing, but the
    processing has not been completed. The request might or might not
    eventually be acted upon.
    """

    status_code = 202
    message = "Accepted"
    description = (
        "The request has been accepted for processing but has not "
        "been completed."
    )


class HTTP_203_NON_AUTHORITATIVE_INFORMATION(HTTPStatus):
    """203 Non-Authoritative Information response status code.

    Indicates that the request was successful but the enclosed payload has
    been modified by a transforming proxy from that of the origin server's 200
    OK response.
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

    Indicates that the server is successfully fulfilling a range request for
    the target resource by transferring one or more parts of the selected
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

    The server has fulfilled a GET request for the resource, and the response
    is a representation of the result of one or more instance-manipulations
    applied to the current instance.
    """

    status_code = 226
    message = "IM Used"
    description = (
        "The server has fulfilled a GET request for the "
        "resource using an instance manipulation."
    )


__all__ = [
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
]
