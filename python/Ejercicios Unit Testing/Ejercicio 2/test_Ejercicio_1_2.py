import pytest
from Ejercicio_1_2 import slice_string


def test_does_not_work_with_an_integer():
    input_data = 1
    with pytest.raises(TypeError):
        slice_string(input_data)


def test_does_not_work_with_blank_string():
    input_data = ""
    with pytest.raises(TypeError):
        slice_string(input_data)


def test_does_not_work_with_empty_list():
    input_data = []
    with pytest.raises(TypeError):
        slice_string(input_data)
