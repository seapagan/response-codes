"""Tests for 5xx Server Error status codes."""

from __future__ import annotations

from response_codes import (
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


class TestServerErrorCodes:
    """Test 5xx server error status codes."""

    def test_http_500_internal_server_error(self) -> None:
        """Test the 500 Internal Server Error status code."""
        assert HTTP_500_INTERNAL_SERVER_ERROR.status_code == 500
        assert HTTP_500_INTERNAL_SERVER_ERROR.message == "Internal Server Error"
        assert HTTP_500_INTERNAL_SERVER_ERROR.description == (
            "The server encountered an unexpected condition that "
            "prevented fulfilling the request."
        )
        assert HTTP_500_INTERNAL_SERVER_ERROR == 500
        assert HTTP_500_INTERNAL_SERVER_ERROR == "Internal Server Error"

    def test_http_501_not_implemented(self) -> None:
        """Test the 501 Not Implemented status code."""
        assert HTTP_501_NOT_IMPLEMENTED.status_code == 501
        assert HTTP_501_NOT_IMPLEMENTED.message == "Not Implemented"
        assert HTTP_501_NOT_IMPLEMENTED == 501
        assert HTTP_501_NOT_IMPLEMENTED == "Not Implemented"

    def test_http_502_bad_gateway(self) -> None:
        """Test the 502 Bad Gateway status code."""
        assert HTTP_502_BAD_GATEWAY.status_code == 502
        assert HTTP_502_BAD_GATEWAY.message == "Bad Gateway"
        assert HTTP_502_BAD_GATEWAY == 502
        assert HTTP_502_BAD_GATEWAY == "Bad Gateway"

    def test_http_503_service_unavailable(self) -> None:
        """Test the 503 Service Unavailable status code."""
        assert HTTP_503_SERVICE_UNAVAILABLE.status_code == 503
        assert HTTP_503_SERVICE_UNAVAILABLE.message == "Service Unavailable"
        assert HTTP_503_SERVICE_UNAVAILABLE == 503
        assert HTTP_503_SERVICE_UNAVAILABLE == "Service Unavailable"

    def test_http_504_gateway_timeout(self) -> None:
        """Test the 504 Gateway Timeout status code."""
        assert HTTP_504_GATEWAY_TIMEOUT.status_code == 504
        assert HTTP_504_GATEWAY_TIMEOUT.message == "Gateway Timeout"
        assert HTTP_504_GATEWAY_TIMEOUT == 504
        assert HTTP_504_GATEWAY_TIMEOUT == "Gateway Timeout"

    def test_http_505_http_version_not_supported(self) -> None:
        """Test the 505 HTTP Version Not Supported status code."""
        assert HTTP_505_HTTP_VERSION_NOT_SUPPORTED.status_code == 505
        assert (
            HTTP_505_HTTP_VERSION_NOT_SUPPORTED.message
            == "HTTP Version Not Supported"
        )
        assert HTTP_505_HTTP_VERSION_NOT_SUPPORTED == 505
        assert (
            HTTP_505_HTTP_VERSION_NOT_SUPPORTED == "HTTP Version Not Supported"
        )

    def test_http_506_variant_also_negotiates(self) -> None:
        """Test the 506 Variant Also Negotiates status code."""
        assert HTTP_506_VARIANT_ALSO_NEGOTIATES.status_code == 506
        assert (
            HTTP_506_VARIANT_ALSO_NEGOTIATES.message
            == "Variant Also Negotiates"
        )
        assert HTTP_506_VARIANT_ALSO_NEGOTIATES == 506
        assert HTTP_506_VARIANT_ALSO_NEGOTIATES == "Variant Also Negotiates"

    def test_http_507_insufficient_storage(self) -> None:
        """Test the 507 Insufficient Storage status code."""
        assert HTTP_507_INSUFFICIENT_STORAGE.status_code == 507
        assert HTTP_507_INSUFFICIENT_STORAGE.message == "Insufficient Storage"
        assert HTTP_507_INSUFFICIENT_STORAGE == 507
        assert HTTP_507_INSUFFICIENT_STORAGE == "Insufficient Storage"

    def test_http_508_loop_detected(self) -> None:
        """Test the 508 Loop Detected status code."""
        assert HTTP_508_LOOP_DETECTED.status_code == 508
        assert HTTP_508_LOOP_DETECTED.message == "Loop Detected"
        assert HTTP_508_LOOP_DETECTED == 508
        assert HTTP_508_LOOP_DETECTED == "Loop Detected"

    def test_http_510_not_extended(self) -> None:
        """Test the 510 Not Extended status code."""
        assert HTTP_510_NOT_EXTENDED.status_code == 510
        assert HTTP_510_NOT_EXTENDED.message == "Not Extended"
        assert HTTP_510_NOT_EXTENDED == 510
        assert HTTP_510_NOT_EXTENDED == "Not Extended"

    def test_http_511_network_authentication_required(self) -> None:
        """Test the 511 Network Authentication Required status code."""
        assert HTTP_511_NETWORK_AUTHENTICATION_REQUIRED.status_code == 511
        assert (
            HTTP_511_NETWORK_AUTHENTICATION_REQUIRED.message
            == "Network Authentication Required"
        )
        assert HTTP_511_NETWORK_AUTHENTICATION_REQUIRED == 511
        assert (
            HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
            == "Network Authentication Required"
        )
