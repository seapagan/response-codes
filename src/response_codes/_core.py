"""Core infrastructure for HTTP status code exceptions.

This module contains the metaclass, base exception class, and utility
functions that form the foundation of the response_codes package.
"""

from __future__ import annotations


class HTTPStatusMeta(type):
    """Base meta-class for HTTP status code exceptions.

    This class serves as the meta-class for the base HTTPStatus class.

    Attributes:
        status_code (int): The numeric HTTP status code
        message (str): The standard HTTP status message
        description (str): A detailed description of the status code
    """

    def __init__(
        cls, name: str, bases: tuple[type, ...], namespace: dict[str, object]
    ) -> None:
        """Initialize the HTTP status exception class."""
        super().__init__(name, bases, namespace)
        # Ensure required attributes exist with default values
        if not hasattr(cls, "status_code"):
            cls.status_code = 0
        if not hasattr(cls, "message"):
            cls.message = ""
        if not hasattr(cls, "description"):
            cls.description = ""

    def __int__(cls) -> int:
        """Convert the status code to an integer.

        Returns:
            int: The numeric HTTP status code
        """
        return cls.status_code

    def __str__(cls) -> str:
        """Convert the status code to a string.

        Returns:
            str: The HTTP status message
        """
        return cls.message

    def __eq__(cls, other: object) -> bool:
        """Compare equality with another object.

        Returns True if other is an integer matching the status code or a
        string matching the message.

        Args:
            other: Object to compare with

        Returns:
            bool: True if objects are equal, False otherwise
        """
        if isinstance(other, int):
            return cls.status_code == other
        if isinstance(other, str):
            return cls.message == other
        return False

    def __lt__(cls, other: int) -> bool:
        """Compare if status code is less than another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is less than other, False otherwise
        """
        if isinstance(other, int):
            return cls.status_code < other
        return NotImplemented

    def __le__(cls, other: int) -> bool:
        """Compare if status code is less than or equal to another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is less than or equal to other
        """
        if isinstance(other, int):
            return cls.status_code <= other
        return NotImplemented

    def __gt__(cls, other: int) -> bool:
        """Compare if status code is greater than another integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is greater than other
        """
        if isinstance(other, int):
            return cls.status_code > other
        return NotImplemented

    def __ge__(cls, other: int) -> bool:
        """Compare if status code is greater than or equal to an integer.

        Args:
            other: Integer to compare with

        Returns:
            bool: True if status code is greater than or equal to other
        """
        if isinstance(other, int):
            return cls.status_code >= other
        return NotImplemented

    def __hash__(cls) -> int:
        """Return hash based on the status code.

        Returns:
            int: Hash value based on the status code
        """
        return hash(cls.status_code)


class HTTPStatus(Exception, metaclass=HTTPStatusMeta):
    """Base class for HTTP status code exceptions.

    This class serves as the foundation for all HTTP status code exceptions,
    providing common functionality for status code handling and comparison.

    Attributes:
        status_code (int): The numeric HTTP status code
        message (str): The standard HTTP status message
        description (str): A detailed description of the status code

    Examples:
        >>> status = HTTP_404_NOT_FOUND()
        >>> status.status_code
        404
        >>> status.message
        'Not Found'
    """

    status_code: int = 0
    message: str = ""
    description: str = ""

    def __init__(self) -> None:
        """Initialize the HTTP status exception with a formatted message."""
        super().__init__(self.message)


# Utility function to create custom groups
def create_status_group(
    *status_classes: type[HTTPStatus],
) -> dict[int, type[HTTPStatus]]:
    """Create a custom status group as a dictionary.

    Args:
        *status_classes: Variable number of HTTPStatus subclasses to include
            in the group.

    Returns:
        A dictionary mapping status codes (int) to their corresponding
        HTTPStatus subclasses.
    """
    return {
        status_class.status_code: status_class
        for status_class in status_classes
    }


__all__ = ["HTTPStatus", "HTTPStatusMeta", "create_status_group"]
