import pytest
from Ejercicio_1_1 import sum_list


def test_sum_works_with_empty_list():
    input_list = []
    result = sum_list(input_list)
    assert result == 0


def test_sum_fails_with_non_numeric_list():
    input_list = ["a", "b", "c"]
    with pytest.raises(TypeError):
        sum_list(input_list)


def test_works_with_negative_numbers():
    input_list = [-1, -5, -9, 7]
    result = sum_list(input_list)
    assert result == -8
