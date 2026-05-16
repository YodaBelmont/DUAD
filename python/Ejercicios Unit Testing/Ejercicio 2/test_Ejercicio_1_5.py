import pytest
from Ejercicio_1_5 import is_prime, sort_list


def test_does_not_work_with_string():
    input_string = "a"
    with pytest.raises(TypeError):
        is_prime(input_string)


def test_fails_with_non_list_argument():
    input_data = 5
    with pytest.raises(TypeError):
        sort_list(input_data)


def test_works_with_medium_size_list():
    input_list = [5, 40, 2, 7, 15, 65, 91, 4, 11, 17, 19, 3, 56, 28, 94, 85]
    result = sort_list(input_list)
    assert result == [5, 2, 7, 11, 17, 19, 3]
