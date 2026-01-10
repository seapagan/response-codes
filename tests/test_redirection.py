"""Tests for 3xx Redirection status codes."""

from __future__ import annotations

from response_codes import (
    HTTP_300_MULTIPLE_CHOICES,
    HTTP_301_MOVED_PERMANENTLY,
    HTTP_302_FOUND,
    HTTP_303_SEE_OTHER,
    HTTP_304_NOT_MODIFIED,
    HTTP_305_USE_PROXY,
    HTTP_307_TEMPORARY_REDIRECT,
    HTTP_308_PERMANENT_REDIRECT,
)


class TestRedirectionCodes:
    """Test 3xx redirection status codes."""

    def test_http_300_multiple_choices(self) -> None:
        """Test the 300 Multiple Choices status code."""
        assert HTTP_300_MULTIPLE_CHOICES.status_code == 300
        assert HTTP_300_MULTIPLE_CHOICES.message == "Multiple Choices"
        assert HTTP_300_MULTIPLE_CHOICES == 300
        assert HTTP_300_MULTIPLE_CHOICES == "Multiple Choices"

    def test_http_301_moved_permanently(self) -> None:
        """Test the 301 Moved Permanently status code."""
        assert HTTP_301_MOVED_PERMANENTLY.status_code == 301
        assert HTTP_301_MOVED_PERMANENTLY.message == "Moved Permanently"
        assert HTTP_301_MOVED_PERMANENTLY == 301
        assert HTTP_301_MOVED_PERMANENTLY == "Moved Permanently"

    def test_http_302_found(self) -> None:
        """Test the 302 Found status code."""
        assert HTTP_302_FOUND.status_code == 302
        assert HTTP_302_FOUND.message == "Found"
        assert HTTP_302_FOUND == 302
        assert HTTP_302_FOUND == "Found"

    def test_http_303_see_other(self) -> None:
        """Test the 303 See Other status code."""
        assert HTTP_303_SEE_OTHER.status_code == 303
        assert HTTP_303_SEE_OTHER.message == "See Other"
        assert HTTP_303_SEE_OTHER == 303
        assert HTTP_303_SEE_OTHER == "See Other"

    def test_http_304_not_modified(self) -> None:
        """Test the 304 Not Modified status code."""
        assert HTTP_304_NOT_MODIFIED.status_code == 304
        assert HTTP_304_NOT_MODIFIED.message == "Not Modified"
        assert HTTP_304_NOT_MODIFIED == 304
        assert HTTP_304_NOT_MODIFIED == "Not Modified"

    def test_http_305_use_proxy(self) -> None:
        """Test the 305 Use Proxy status code."""
        assert HTTP_305_USE_PROXY.status_code == 305
        assert HTTP_305_USE_PROXY.message == "Use Proxy"
        assert HTTP_305_USE_PROXY == 305
        assert HTTP_305_USE_PROXY == "Use Proxy"

    def test_http_307_temporary_redirect(self) -> None:
        """Test the 307 Temporary Redirect status code."""
        assert HTTP_307_TEMPORARY_REDIRECT.status_code == 307
        assert HTTP_307_TEMPORARY_REDIRECT.message == "Temporary Redirect"
        assert HTTP_307_TEMPORARY_REDIRECT == 307
        assert HTTP_307_TEMPORARY_REDIRECT == "Temporary Redirect"

    def test_http_308_permanent_redirect(self) -> None:
        """Test the 308 Permanent Redirect status code."""
        assert HTTP_308_PERMANENT_REDIRECT.status_code == 308
        assert HTTP_308_PERMANENT_REDIRECT.message == "Permanent Redirect"
        assert HTTP_308_PERMANENT_REDIRECT == 308
        assert HTTP_308_PERMANENT_REDIRECT == "Permanent Redirect"
