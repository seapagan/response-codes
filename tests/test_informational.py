"""Tests for 1xx Informational status codes."""

from __future__ import annotations

from response_codes import (
    HTTP_100_CONTINUE,
    HTTP_101_SWITCHING_PROTOCOLS,
    HTTP_102_PROCESSING,
)


class TestInformationalCodes:
    """Test 1xx informational status codes."""

    def test_http_100_continue(self) -> None:
        """Test the 100 Continue status code."""
        assert HTTP_100_CONTINUE.status_code == 100
        assert HTTP_100_CONTINUE.message == "Continue"
        assert HTTP_100_CONTINUE == 100
        assert HTTP_100_CONTINUE == "Continue"

    def test_http_101_switching_protocols(self) -> None:
        """Test the 101 Switching Protocols status code."""
        assert HTTP_101_SWITCHING_PROTOCOLS.status_code == 101
        assert HTTP_101_SWITCHING_PROTOCOLS.message == "Switching Protocols"
        assert HTTP_101_SWITCHING_PROTOCOLS == 101
        assert HTTP_101_SWITCHING_PROTOCOLS == "Switching Protocols"

    def test_http_102_processing(self) -> None:
        """Test the 102 Processing status code."""
        assert HTTP_102_PROCESSING.status_code == 102
        assert HTTP_102_PROCESSING.message == "Processing"
        assert HTTP_102_PROCESSING == 102
        assert HTTP_102_PROCESSING == "Processing"
