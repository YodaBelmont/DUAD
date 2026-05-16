import pytest
from Ejercicio_1_4 import alphabetic_string


def test_works_with_small_string():
    input_string = "Hello"
    result = alphabetic_string(input_string)
    assert result == "Hello"


def test_does_not_work_with_integers():
    input_integer = 5
    with pytest.raises(AttributeError):
        alphabetic_string(input_integer)


def test_work_with_empty_string():
    input_string = ""
    result = alphabetic_string(input_string)
    assert result == ""
