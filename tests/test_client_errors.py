"""Tests for 4xx Client Error status codes."""

from __future__ import annotations

from response_codes import (
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


class TestClientErrorCodes:
    """Test 4xx client error status codes."""

    def test_http_400_bad_request(self) -> None:
        """Test the 400 Bad Request status code."""
        assert HTTP_400_BAD_REQUEST.status_code == 400
        assert HTTP_400_BAD_REQUEST.message == "Bad Request"
        assert HTTP_400_BAD_REQUEST == 400
        assert HTTP_400_BAD_REQUEST == "Bad Request"

    def test_http_401_unauthorized(self) -> None:
        """Test the 401 Unauthorized status code."""
        assert HTTP_401_UNAUTHORIZED.status_code == 401
        assert HTTP_401_UNAUTHORIZED.message == "Unauthorized"
        assert HTTP_401_UNAUTHORIZED == 401
        assert HTTP_401_UNAUTHORIZED == "Unauthorized"

    def test_http_402_payment_required(self) -> None:
        """Test the 402 Payment Required status code."""
        assert HTTP_402_PAYMENT_REQUIRED.status_code == 402
        assert HTTP_402_PAYMENT_REQUIRED.message == "Payment Required"
        assert HTTP_402_PAYMENT_REQUIRED == 402
        assert HTTP_402_PAYMENT_REQUIRED == "Payment Required"

    def test_http_403_forbidden(self) -> None:
        """Test the 403 Forbidden status code."""
        assert HTTP_403_FORBIDDEN.status_code == 403
        assert HTTP_403_FORBIDDEN.message == "Forbidden"
        assert HTTP_403_FORBIDDEN == 403
        assert HTTP_403_FORBIDDEN == "Forbidden"

    def test_http_404_not_found(self) -> None:
        """Test the 404 Not Found status code."""
        assert HTTP_404_NOT_FOUND.status_code == 404
        assert HTTP_404_NOT_FOUND.message == "Not Found"
        assert HTTP_404_NOT_FOUND.description == (
            "The requested resource could not be found on the server."
        )
        assert HTTP_404_NOT_FOUND == 404
        assert HTTP_404_NOT_FOUND == "Not Found"

    def test_http_405_method_not_allowed(self) -> None:
        """Test the 405 Method Not Allowed status code."""
        assert HTTP_405_METHOD_NOT_ALLOWED.status_code == 405
        assert HTTP_405_METHOD_NOT_ALLOWED.message == "Method Not Allowed"
        assert HTTP_405_METHOD_NOT_ALLOWED == 405
        assert HTTP_405_METHOD_NOT_ALLOWED == "Method Not Allowed"

    def test_http_406_not_acceptable(self) -> None:
        """Test the 406 Not Acceptable status code."""
        assert HTTP_406_NOT_ACCEPTABLE.status_code == 406
        assert HTTP_406_NOT_ACCEPTABLE.message == "Not Acceptable"
        assert HTTP_406_NOT_ACCEPTABLE == 406
        assert HTTP_406_NOT_ACCEPTABLE == "Not Acceptable"

    def test_http_407_proxy_authentication_required(self) -> None:
        """Test the 407 Proxy Authentication Required status code."""
        assert HTTP_407_PROXY_AUTHENTICATION_REQUIRED.status_code == 407
        assert (
            HTTP_407_PROXY_AUTHENTICATION_REQUIRED.message
            == "Proxy Authentication Required"
        )
        assert HTTP_407_PROXY_AUTHENTICATION_REQUIRED == 407
        assert (
            HTTP_407_PROXY_AUTHENTICATION_REQUIRED
            == "Proxy Authentication Required"
        )

    def test_http_408_request_timeout(self) -> None:
        """Test the 408 Request Timeout status code."""
        assert HTTP_408_REQUEST_TIMEOUT.status_code == 408
        assert HTTP_408_REQUEST_TIMEOUT.message == "Request Timeout"
        assert HTTP_408_REQUEST_TIMEOUT == 408
        assert HTTP_408_REQUEST_TIMEOUT == "Request Timeout"

    def test_http_409_conflict(self) -> None:
        """Test the 409 Conflict status code."""
        assert HTTP_409_CONFLICT.status_code == 409
        assert HTTP_409_CONFLICT.message == "Conflict"
        assert HTTP_409_CONFLICT == 409
        assert HTTP_409_CONFLICT == "Conflict"

    def test_http_410_gone(self) -> None:
        """Test the 410 Gone status code."""
        assert HTTP_410_GONE.status_code == 410
        assert HTTP_410_GONE.message == "Gone"
        assert HTTP_410_GONE == 410
        assert HTTP_410_GONE == "Gone"

    def test_http_411_length_required(self) -> None:
        """Test the 411 Length Required status code."""
        assert HTTP_411_LENGTH_REQUIRED.status_code == 411
        assert HTTP_411_LENGTH_REQUIRED.message == "Length Required"
        assert HTTP_411_LENGTH_REQUIRED == 411
        assert HTTP_411_LENGTH_REQUIRED == "Length Required"

    def test_http_412_precondition_failed(self) -> None:
        """Test the 412 Precondition Failed status code."""
        assert HTTP_412_PRECONDITION_FAILED.status_code == 412
        assert HTTP_412_PRECONDITION_FAILED.message == "Precondition Failed"
        assert HTTP_412_PRECONDITION_FAILED == 412
        assert HTTP_412_PRECONDITION_FAILED == "Precondition Failed"

    def test_http_413_payload_too_large(self) -> None:
        """Test the 413 Payload Too Large status code."""
        assert HTTP_413_PAYLOAD_TOO_LARGE.status_code == 413
        assert HTTP_413_PAYLOAD_TOO_LARGE.message == "Payload Too Large"
        assert HTTP_413_PAYLOAD_TOO_LARGE == 413
        assert HTTP_413_PAYLOAD_TOO_LARGE == "Payload Too Large"

    def test_http_414_uri_too_long(self) -> None:
        """Test the 414 URI Too Long status code."""
        assert HTTP_414_URI_TOO_LONG.status_code == 414
        assert HTTP_414_URI_TOO_LONG.message == "URI Too Long"
        assert HTTP_414_URI_TOO_LONG == 414
        assert HTTP_414_URI_TOO_LONG == "URI Too Long"

    def test_http_415_unsupported_media_type(self) -> None:
        """Test the 415 Unsupported Media Type status code."""
        assert HTTP_415_UNSUPPORTED_MEDIA_TYPE.status_code == 415
        assert (
            HTTP_415_UNSUPPORTED_MEDIA_TYPE.message == "Unsupported Media Type"
        )
        assert HTTP_415_UNSUPPORTED_MEDIA_TYPE == 415
        assert HTTP_415_UNSUPPORTED_MEDIA_TYPE == "Unsupported Media Type"

    def test_http_416_range_not_satisfiable(self) -> None:
        """Test the 416 Range Not Satisfiable status code."""
        assert HTTP_416_RANGE_NOT_SATISFIABLE.status_code == 416
        assert HTTP_416_RANGE_NOT_SATISFIABLE.message == "Range Not Satisfiable"
        assert HTTP_416_RANGE_NOT_SATISFIABLE == 416
        assert HTTP_416_RANGE_NOT_SATISFIABLE == "Range Not Satisfiable"

    def test_http_417_expectation_failed(self) -> None:
        """Test the 417 Expectation Failed status code."""
        assert HTTP_417_EXPECTATION_FAILED.status_code == 417
        assert HTTP_417_EXPECTATION_FAILED.message == "Expectation Failed"
        assert HTTP_417_EXPECTATION_FAILED == 417
        assert HTTP_417_EXPECTATION_FAILED == "Expectation Failed"

    def test_http_418_im_a_teapot(self) -> None:
        """Test the 418 I'm a teapot status code."""
        assert HTTP_418_IM_A_TEAPOT.status_code == 418
        assert HTTP_418_IM_A_TEAPOT.message == "I'm a teapot"
        assert HTTP_418_IM_A_TEAPOT == 418
        assert HTTP_418_IM_A_TEAPOT == "I'm a teapot"

    def test_http_421_misdirected_request(self) -> None:
        """Test the 421 Misdirected Request status code."""
        assert HTTP_421_MISDIRECTED_REQUEST.status_code == 421
        assert HTTP_421_MISDIRECTED_REQUEST.message == "Misdirected Request"
        assert HTTP_421_MISDIRECTED_REQUEST == 421
        assert HTTP_421_MISDIRECTED_REQUEST == "Misdirected Request"

    def test_http_422_unprocessable_entity(self) -> None:
        """Test the 422 Unprocessable Entity status code."""
        assert HTTP_422_UNPROCESSABLE_ENTITY.status_code == 422
        assert HTTP_422_UNPROCESSABLE_ENTITY.message == "Unprocessable Entity"
        assert HTTP_422_UNPROCESSABLE_ENTITY == 422
        assert HTTP_422_UNPROCESSABLE_ENTITY == "Unprocessable Entity"

    def test_http_423_locked(self) -> None:
        """Test the 423 Locked status code."""
        assert HTTP_423_LOCKED.status_code == 423
        assert HTTP_423_LOCKED.message == "Locked"
        assert HTTP_423_LOCKED == 423
        assert HTTP_423_LOCKED == "Locked"

    def test_http_424_failed_dependency(self) -> None:
        """Test the 424 Failed Dependency status code."""
        assert HTTP_424_FAILED_DEPENDENCY.status_code == 424
        assert HTTP_424_FAILED_DEPENDENCY.message == "Failed Dependency"
        assert HTTP_424_FAILED_DEPENDENCY == 424
        assert HTTP_424_FAILED_DEPENDENCY == "Failed Dependency"

    def test_http_425_too_early(self) -> None:
        """Test the 425 Too Early status code."""
        assert HTTP_425_TOO_EARLY.status_code == 425
        assert HTTP_425_TOO_EARLY.message == "Too Early"
        assert HTTP_425_TOO_EARLY == 425
        assert HTTP_425_TOO_EARLY == "Too Early"

    def test_http_426_upgrade_required(self) -> None:
        """Test the 426 Upgrade Required status code."""
        assert HTTP_426_UPGRADE_REQUIRED.status_code == 426
        assert HTTP_426_UPGRADE_REQUIRED.message == "Upgrade Required"
        assert HTTP_426_UPGRADE_REQUIRED == 426
        assert HTTP_426_UPGRADE_REQUIRED == "Upgrade Required"

    def test_http_428_precondition_required(self) -> None:
        """Test the 428 Precondition Required status code."""
        assert HTTP_428_PRECONDITION_REQUIRED.status_code == 428
        assert HTTP_428_PRECONDITION_REQUIRED.message == "Precondition Required"
        assert HTTP_428_PRECONDITION_REQUIRED == 428
        assert HTTP_428_PRECONDITION_REQUIRED == "Precondition Required"

    def test_http_429_too_many_requests(self) -> None:
        """Test the 429 Too Many Requests status code."""
        assert HTTP_429_TOO_MANY_REQUESTS.status_code == 429
        assert HTTP_429_TOO_MANY_REQUESTS.message == "Too Many Requests"
        assert HTTP_429_TOO_MANY_REQUESTS == 429
        assert HTTP_429_TOO_MANY_REQUESTS == "Too Many Requests"

    def test_http_431_request_header_fields_too_large(self) -> None:
        """Test the 431 Request Header Fields Too Large status code."""
        assert HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE.status_code == 431
        assert (
            HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE.message
            == "Request Header Fields Too Large"
        )
        assert HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE == 431
        assert (
            HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
            == "Request Header Fields Too Large"
        )

    def test_http_451_unavailable_for_legal_reasons(self) -> None:
        """Test the 451 Unavailable For Legal Reasons status code."""
        assert HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS.status_code == 451
        assert (
            HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS.message
            == "Unavailable For Legal Reasons"
        )
        assert HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS == 451
        assert (
            HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
            == "Unavailable For Legal Reasons"
        )
