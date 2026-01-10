"""Tests for HTTP status code groups."""

from __future__ import annotations

from response_codes import (
    HTTP_CLIENT_ERRORS,
    HTTP_INFORMATIONAL,
    HTTP_REDIRECTION,
    HTTP_SERVER_ERRORS,
    HTTP_SUCCESS,
)


class TestHTTPStatusGroups:
    """Test the HTTP status code groups."""

    def test_http_informational_group(self) -> None:
        """Test the informational status code group."""
        assert all(100 <= code <= 102 for code in HTTP_INFORMATIONAL)
        assert len(HTTP_INFORMATIONAL) == 3

    def test_http_success_group(self) -> None:
        """Test the success status code group."""
        assert all(200 <= code <= 226 for code in HTTP_SUCCESS)
        assert len(HTTP_SUCCESS) == 10

    def test_http_redirection_group(self) -> None:
        """Test the redirection status code group."""
        assert all(300 <= code <= 308 for code in HTTP_REDIRECTION)
        assert len(HTTP_REDIRECTION) == 8

    def test_http_client_errors_group(self) -> None:
        """Test the client errors status code group."""
        assert all(400 <= code <= 429 for code in HTTP_CLIENT_ERRORS)
        assert len(HTTP_CLIENT_ERRORS) == 7

    def test_http_server_errors_group(self) -> None:
        """Test the server errors status code group."""
        assert all(500 <= code <= 511 for code in HTTP_SERVER_ERRORS)
        assert len(HTTP_SERVER_ERRORS) == 6
