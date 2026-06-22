import pytest
from axentx_product import add, multiply, greet


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-5, 5, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-1, 5, -5),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_greet():
    assert greet("World") == "Hello, World!"


def test_type_errors():
    with pytest.raises(TypeError):
        add("1", 2)
    with pytest.raises(TypeError):
        multiply(3, "4")
    with pytest.raises(TypeError):
        greet(123)
