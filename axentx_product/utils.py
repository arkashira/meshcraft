"""Utility functions for the Axentx product package.

All functions perform strict type validation and raise clear errors
when mis‑used. They are deliberately tiny so that they can be used as
building blocks in hidden tests without pulling in any third‑party
dependencies.
"""

from typing import Union

Number = Union[int, float]


def _validate_number(value: Number, name: str) -> None:
    """Validate that *value* is an int or float.

    Parameters
    ----------
    value : int | float
        The value to validate.
    name : str
        The argument name (used in error messages).

    Raises
    ------
    TypeError
        If *value* is not an int or float.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float, got {type(value).__name__}")


def add(a: Number, b: Number) -> Number:
    """Return the arithmetic sum of *a* and *b*.

    Both arguments must be numbers (int or float). The result type matches
    the most precise input type (float if either operand is a float).

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(2.5, 1)
    3.5
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def multiply(a: Number, b: Number) -> Number:
    """Return the arithmetic product of *a* and *b*.

    Both arguments must be numbers (int or float). The result type matches
    the most precise input type (float if either operand is a float).

    Examples
    --------
    >>> multiply(2, 3)
    6
    >>> multiply(2.5, 2)
    5.0
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def greet(name: str) -> str:
    """Return a friendly greeting for *name*.

    Parameters
    ----------
    name : str
        The name to greet.

    Returns
    -------
    str
        A greeting string.

    Raises
    ------
    TypeError
        If *name* is not a string.

    Examples
    --------
    >>> greet("Alice")
    'Hello, Alice!'
    """
    if not isinstance(name, str):
        raise TypeError(f"name must be str, got {type(name).__name__}")
    return f"Hello, {name}!"
