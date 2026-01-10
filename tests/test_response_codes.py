"""Tests for the http_codes module."""

from __future__ import annotations

import pytest

from response_codes import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_CLIENT_ERRORS,
    HTTP_INFORMATIONAL,
    HTTP_REDIRECTION,
    HTTP_SERVER_ERRORS,
    HTTP_SUCCESS,
    HTTPStatus,
)


class TestHTTPStatusBase:
    """Test the base HTTPStatus class functionality."""

    def test_status_code_int_conversion(self) -> None:
        """Test converting status code to integer."""
        assert HTTP_404_NOT_FOUND.status_code == 404

    def test_status_message_str_conversion(self) -> None:
        """Test converting status message to string."""
        assert HTTP_404_NOT_FOUND.message == "Not Found"

    def test_equality_with_int(self) -> None:
        """Test equality comparison with integer."""
        assert HTTP_404_NOT_FOUND.status_code == 404
        assert HTTP_200_OK.status_code == 200
        assert HTTP_500_INTERNAL_SERVER_ERROR.status_code == 500

    def test_equality_with_str(self) -> None:
        """Test equality comparison with string."""
        assert HTTP_404_NOT_FOUND.message == "Not Found"
        assert HTTP_200_OK.message == "OK"
        assert HTTP_500_INTERNAL_SERVER_ERROR.message == "Internal Server Error"

    def test_equality_with_other_types(self) -> None:
        """Test equality comparison with non-int/non-str types."""
        assert (HTTP_404_NOT_FOUND == [404]) is False
        assert (HTTP_404_NOT_FOUND == {"code": 404}) is False
        assert (HTTP_404_NOT_FOUND == (404,)) is False
        assert (HTTP_200_OK == 200.0) is False

    def test_inequality(self) -> None:
        """Test inequality comparisons."""
        assert HTTP_404_NOT_FOUND.status_code != 200
        assert HTTP_404_NOT_FOUND.message != "OK"
        assert HTTP_404_NOT_FOUND.status_code != HTTP_200_OK.status_code

    def test_less_than_comparison(self) -> None:
        """Test less than comparison with integer."""
        assert HTTP_200_OK < 404
        assert not (HTTP_404_NOT_FOUND < 200)

    def test_less_than_or_equal_comparison(self) -> None:
        """Test less than or equal comparison with integer."""
        assert HTTP_200_OK <= 404
        assert HTTP_200_OK <= 200
        assert not (HTTP_404_NOT_FOUND <= 200)

    def test_greater_than_comparison(self) -> None:
        """Test greater than comparison with integer."""
        assert HTTP_404_NOT_FOUND > 200
        assert not (HTTP_200_OK > 404)

    def test_greater_than_or_equal_comparison(self) -> None:
        """Test greater than or equal comparison with integer."""
        assert HTTP_404_NOT_FOUND >= 200
        assert HTTP_404_NOT_FOUND >= 404
        assert not (HTTP_200_OK >= 404)

    def test_comparison_with_non_int(self) -> None:
        """Test comparison operations with non-integer types raise TypeError."""
        # These operations trigger the NotImplemented return, which Python
        # converts to TypeError
        with pytest.raises(TypeError):
            _ = HTTP_404_NOT_FOUND < "404"  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_404_NOT_FOUND <= "404"  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_404_NOT_FOUND > "404"  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_404_NOT_FOUND >= "404"  # type: ignore

        # Test with various non-integer types
        with pytest.raises(TypeError):
            _ = HTTP_200_OK < [200]  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_200_OK <= None  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_200_OK > {"code": 200}  # type: ignore
        with pytest.raises(TypeError):
            _ = HTTP_200_OK >= 200.0  # type: ignore

    def test_hash(self) -> None:
        """Test that status codes can be hashed."""
        assert hash(HTTP_404_NOT_FOUND) == hash(404)
        assert hash(HTTP_200_OK) == hash(200)
        assert hash(HTTP_500_INTERNAL_SERVER_ERROR) == hash(500)

        # Test that status codes can be used in sets and as dict keys
        status_set = {HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_404_NOT_FOUND}
        assert len(status_set) == 2

        status_dict = {
            HTTP_404_NOT_FOUND: "not found",
            HTTP_200_OK: "ok",
        }
        assert status_dict[HTTP_404_NOT_FOUND] == "not found"


class TestHTTPStatusGroups:
    """Test the HTTP status code groups."""

    def test_informational_group(self) -> None:
        """Test the informational status code group."""
        assert all(100 <= code <= 102 for code in HTTP_INFORMATIONAL)
        assert len(HTTP_INFORMATIONAL) == 3

    def test_success_group(self) -> None:
        """Test the success status code group."""
        assert all(200 <= code <= 226 for code in HTTP_SUCCESS)
        assert len(HTTP_SUCCESS) == 10

    def test_redirection_group(self) -> None:
        """Test the redirection status code group."""
        assert all(300 <= code <= 308 for code in HTTP_REDIRECTION)
        assert len(HTTP_REDIRECTION) == 8

    def test_client_errors_group(self) -> None:
        """Test the client errors status code group."""
        assert all(400 <= code <= 429 for code in HTTP_CLIENT_ERRORS)
        assert len(HTTP_CLIENT_ERRORS) == 7

    def test_server_errors_group(self) -> None:
        """Test the server errors status code group."""
        assert all(500 <= code <= 511 for code in HTTP_SERVER_ERRORS)
        assert len(HTTP_SERVER_ERRORS) == 6


class TestHTTPStatusExceptions:
    """Test the HTTP status code exceptions."""

    def test_exception_message_format(self) -> None:
        """Test the format of exception messages."""
        with pytest.raises(HTTP_404_NOT_FOUND) as exc_info:
            raise HTTP_404_NOT_FOUND
        assert str(exc_info.value) == "Not Found"

    def test_exception_attributes(self) -> None:
        """Test the attributes of status code exceptions."""
        status = HTTP_404_NOT_FOUND()
        assert status.status_code == 404
        assert status.message == "Not Found"
        assert status.description == (
            "The requested resource could not be found on the server."
        )

    def test_exception_inheritance(self) -> None:
        """Test that status codes inherit from HTTPStatus and Exception."""
        status = HTTP_404_NOT_FOUND()
        assert isinstance(status, HTTPStatus)
        assert isinstance(status, Exception)


class TestImplicitConversions:
    """Ensure that implicit conversions work as expected."""

    def test_implicit_conversion(self) -> None:
        """Test for implicit conversions."""
        assert HTTP_200_OK == 200
        assert HTTP_200_OK == "OK"

    def test_int_conversion(self) -> None:
        """Test converting status code to int using int()."""
        assert int(HTTP_404_NOT_FOUND) == 404
        assert int(HTTP_200_OK) == 200
        assert int(HTTP_500_INTERNAL_SERVER_ERROR) == 500

    def test_str_conversion(self) -> None:
        """Test converting status code to str using str()."""
        assert str(HTTP_404_NOT_FOUND) == "Not Found"
        assert str(HTTP_200_OK) == "OK"
        assert str(HTTP_500_INTERNAL_SERVER_ERROR) == "Internal Server Error"


class TestSpecificStatusCodes:
    """Test specific HTTP status codes."""

    def test_404_not_found(self) -> None:
        """Test the 404 Not Found status code."""
        assert HTTP_404_NOT_FOUND.status_code == 404
        assert HTTP_404_NOT_FOUND.message == "Not Found"
        assert HTTP_404_NOT_FOUND.description == (
            "The requested resource could not be found on the server."
        )

    def test_200_ok(self) -> None:
        """Test the 200 OK status code."""
        assert HTTP_200_OK.status_code == 200
        assert HTTP_200_OK.message == "OK"
        assert HTTP_200_OK.description == (
            "The request has succeeded and the response contains the "
            "requested data."
        )

    def test_500_internal_server_error(self) -> None:
        """Test the 500 Internal Server Error status code."""
        assert HTTP_500_INTERNAL_SERVER_ERROR.status_code == 500
        assert HTTP_500_INTERNAL_SERVER_ERROR.message == "Internal Server Error"
        assert HTTP_500_INTERNAL_SERVER_ERROR.description == (
            "The server encountered an unexpected condition that "
            "prevented fulfilling the request."
        )


class TestMetaclassDefaults:
    """Test metaclass default attribute initialization."""

    def test_metaclass_initializes_missing_attributes(self) -> None:
        """Test that metaclass sets default values for missing attributes."""
        # Import at runtime to avoid mypy issues with the metaclass
        from response_codes import HTTPStatusMeta  # noqa: PLC0415

        # Create a minimal class without defining the standard attributes
        class MinimalStatus(Exception, metaclass=HTTPStatusMeta):
            """Test class with no attributes defined."""

        # Verify that the metaclass initialized the default attributes
        assert MinimalStatus.status_code == 0
        assert MinimalStatus.message == ""
        assert MinimalStatus.description == ""

        # Verify basic functionality still works
        assert int(MinimalStatus) == 0
        assert str(MinimalStatus) == ""
        assert MinimalStatus == 0
