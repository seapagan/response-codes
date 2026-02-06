"""Tests for the core HTTPStatus metaclass and utilities."""

from __future__ import annotations

import pytest

from response_codes import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
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

    def test_reflexive_class_equality(self) -> None:
        """Test class equality is reflexive."""
        not_found = HTTP_404_NOT_FOUND
        ok = HTTP_200_OK
        assert not_found == HTTP_404_NOT_FOUND
        assert ok == HTTP_200_OK

    def test_class_to_class_inequality(self) -> None:
        """Test different status classes are not equal."""
        assert HTTP_404_NOT_FOUND != HTTP_200_OK
        assert HTTP_500_INTERNAL_SERVER_ERROR != HTTP_404_NOT_FOUND

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
