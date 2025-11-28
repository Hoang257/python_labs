import pytest
from src.lab03.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "in_data, expected",
    [
        "ПрИвЕт\nМИр\t",
        "ёжик, Ёлка",
        "Hello\r\nWorld",
        "  двойные   пробелы  ",
    ]
    )
def test_normalize(in_data, expected):
    assert normalize(in_data) == expected 