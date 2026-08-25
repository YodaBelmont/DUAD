import pytest
from Eiercicio_1_3 import count_lower_upper


def test_does_not_work_with_an_integer():
    input_data = 1
    with pytest.raises(TypeError):
        count_lower_upper(input_data)


def test_does_not_work_with_blank_string():
    input_data = ""
    with pytest.raises(TypeError):
        count_lower_upper(input_data)


def test_works_with_large_string():
    input_string = """The Domain Expansion by Kinji Hakari in Jujutsu Kaisen, call Inactive Death Bet,
                    does not have a direct hit attack (sure). Instead,
                    transform combat into one machine pachinko (a Japanese game of chance) where Hakari bets his destiny.
                    If you're lucky, you get immortality and unlimited cursed energy for a few minutes.
                    """
    result = count_lower_upper(input_string)
    assert result == print(f"Upper letters: {14} Lower letters: {240} Spaces: {50}")
