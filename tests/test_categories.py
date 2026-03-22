"""Tests for HTTP status category helpers (is_* functions)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

import pytest

from response_codes import (
    HTTP_103_EARLY_HINTS,
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
    is_client_error,
    is_informational,
    is_redirection,
    is_server_error,
    is_success,
)


class TestStatusCategories:
    """Tests for HTTP status category helpers."""

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (99, False),
            (100, True),
            (101, True),
            (102, True),
            (103, True),
            (104, True),
            (199, True),
            (200, False),
        ],
    )
    def test_is_informational_int_bounds(
        self, code: int, expected: object
    ) -> None:
        """Return True only for values in the 100-199 range."""
        assert is_informational(code) is expected

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (199, False),
            (200, True),
            (201, True),
            (202, True),
            (203, True),
            (226, True),
            (250, True),
            (299, True),
            (300, False),
        ],
    )
    def test_is_success_int_bounds(self, code: int, expected: object) -> None:
        """Return True only for values in the 200-299 range."""
        assert is_success(code) is expected

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (299, False),
            (300, True),
            (301, True),
            (302, True),
            (307, True),
            (308, True),
            (306, True),
            (399, True),
            (400, False),
        ],
    )
    def test_is_redirection_int_bounds(
        self, code: int, expected: object
    ) -> None:
        """Return True only for values in the 300-399 range."""
        assert is_redirection(code) is expected

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (399, False),
            (400, True),
            (401, True),
            (402, True),
            (403, True),
            (404, True),
            (405, True),
            (408, True),
            (422, True),
            (429, True),
            (499, True),
            (500, False),
        ],
    )
    def test_is_client_error_int_bounds(
        self, code: int, expected: object
    ) -> None:
        """Return True only for values in the 400-499 range."""
        assert is_client_error(code) is expected

    @pytest.mark.parametrize(
        ("code", "expected"),
        [
            (499, False),
            (500, True),
            (501, True),
            (502, True),
            (503, True),
            (504, True),
            (509, True),
            (511, True),
            (599, True),
            (600, False),
        ],
    )
    def test_is_server_error_int_bounds(
        self, code: int, expected: object
    ) -> None:
        """Return True only for values in the 500-599 range."""
        assert is_server_error(code) is expected

    @pytest.mark.parametrize(
        ("predicate", "value"),
        [
            (is_informational, HTTP_103_EARLY_HINTS),
            (is_success, HTTP_200_OK),
            (is_success, HTTP_200_OK()),
            (is_client_error, HTTP_422_UNPROCESSABLE_ENTITY),
            (is_client_error, HTTP_422_UNPROCESSABLE_ENTITY()),
            (is_server_error, HTTP_500_INTERNAL_SERVER_ERROR()),
        ],
    )
    def test_is_accepts_status_classes_and_instances(
        self, predicate: Callable[[object], bool], value: object
    ) -> None:
        """Accept HTTPStatus subclasses and instances as input."""
        assert predicate(value) is True

    @pytest.mark.parametrize(
        ("predicate", "value"),
        [
            (is_informational, "404"),
            (is_success, None),
            (is_client_error, []),
            (is_server_error, 3.14),
            (is_redirection, True),
        ],
    )
    def test_invalid_types_raise_typeerror(
        self, predicate: Callable[[object], bool], value: object
    ) -> None:
        """Raise TypeError for unsupported input types."""
        with pytest.raises(TypeError):
            predicate(value)
