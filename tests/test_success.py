"""Tests for 2xx Success status codes."""

from __future__ import annotations

from response_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    HTTP_204_NO_CONTENT,
    HTTP_205_RESET_CONTENT,
    HTTP_206_PARTIAL_CONTENT,
    HTTP_207_MULTI_STATUS,
    HTTP_208_ALREADY_REPORTED,
    HTTP_226_IM_USED,
)


class TestSuccessCodes:
    """Test 2xx success status codes."""

    def test_http_200_ok(self) -> None:
        """Test the 200 OK status code."""
        assert HTTP_200_OK.status_code == 200
        assert HTTP_200_OK.message == "OK"
        assert HTTP_200_OK.description == (
            "The request has succeeded and the response contains the "
            "requested data."
        )
        assert HTTP_200_OK == 200
        assert HTTP_200_OK == "OK"

    def test_http_201_created(self) -> None:
        """Test the 201 Created status code."""
        assert HTTP_201_CREATED.status_code == 201
        assert HTTP_201_CREATED.message == "Created"
        assert HTTP_201_CREATED == 201
        assert HTTP_201_CREATED == "Created"

    def test_http_202_accepted(self) -> None:
        """Test the 202 Accepted status code."""
        assert HTTP_202_ACCEPTED.status_code == 202
        assert HTTP_202_ACCEPTED.message == "Accepted"
        assert HTTP_202_ACCEPTED == 202
        assert HTTP_202_ACCEPTED == "Accepted"

    def test_http_203_non_authoritative_information(self) -> None:
        """Test the 203 Non-Authoritative Information status code."""
        assert HTTP_203_NON_AUTHORITATIVE_INFORMATION.status_code == 203
        assert (
            HTTP_203_NON_AUTHORITATIVE_INFORMATION.message
            == "Non-Authoritative Information"
        )
        assert HTTP_203_NON_AUTHORITATIVE_INFORMATION == 203
        assert (
            HTTP_203_NON_AUTHORITATIVE_INFORMATION
            == "Non-Authoritative Information"
        )

    def test_http_204_no_content(self) -> None:
        """Test the 204 No Content status code."""
        assert HTTP_204_NO_CONTENT.status_code == 204
        assert HTTP_204_NO_CONTENT.message == "No Content"
        assert HTTP_204_NO_CONTENT == 204
        assert HTTP_204_NO_CONTENT == "No Content"

    def test_http_205_reset_content(self) -> None:
        """Test the 205 Reset Content status code."""
        assert HTTP_205_RESET_CONTENT.status_code == 205
        assert HTTP_205_RESET_CONTENT.message == "Reset Content"
        assert HTTP_205_RESET_CONTENT == 205
        assert HTTP_205_RESET_CONTENT == "Reset Content"

    def test_http_206_partial_content(self) -> None:
        """Test the 206 Partial Content status code."""
        assert HTTP_206_PARTIAL_CONTENT.status_code == 206
        assert HTTP_206_PARTIAL_CONTENT.message == "Partial Content"
        assert HTTP_206_PARTIAL_CONTENT == 206
        assert HTTP_206_PARTIAL_CONTENT == "Partial Content"

    def test_http_207_multi_status(self) -> None:
        """Test the 207 Multi-Status status code."""
        assert HTTP_207_MULTI_STATUS.status_code == 207
        assert HTTP_207_MULTI_STATUS.message == "Multi-Status"
        assert HTTP_207_MULTI_STATUS == 207
        assert HTTP_207_MULTI_STATUS == "Multi-Status"

    def test_http_208_already_reported(self) -> None:
        """Test the 208 Already Reported status code."""
        assert HTTP_208_ALREADY_REPORTED.status_code == 208
        assert HTTP_208_ALREADY_REPORTED.message == "Already Reported"
        assert HTTP_208_ALREADY_REPORTED == 208
        assert HTTP_208_ALREADY_REPORTED == "Already Reported"

    def test_http_226_im_used(self) -> None:
        """Test the 226 IM Used status code."""
        assert HTTP_226_IM_USED.status_code == 226
        assert HTTP_226_IM_USED.message == "IM Used"
        assert HTTP_226_IM_USED == 226
        assert HTTP_226_IM_USED == "IM Used"
