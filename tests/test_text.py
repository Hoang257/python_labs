import pytest
import sys, os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "in_data, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("       ", ""),
        ("123  456", "123 456"),
        ("Много\t\t\tтабов", "много табов"),
    ],
)
def test_normalize(in_data, expected):
    assert normalize(in_data) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("    ", []),
        ("!!!", []),
        ("a-b-c", ["a-b-c"]),
        ("кириллица and english", ["кириллица", "and", "english"]),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["word"], {"word": 1}),
        (["word", "Word", "WORD"], {"word": 1, "Word": 1, "WORD": 1}),
        (["word", "word", "word"], {"word": 3}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq_dict, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({}, 1, []),
        ({"c": 3, "b": 3, "v": 3}, 3, [("b", 3), ("c", 3), ("v", 3)]),
        ({"a": 1, "b": 1}, 5, [("a", 1), ("b", 1)]),
        ({"a": 3, "b": 3, "c": 2}, 2, [("a", 3), ("b", 3)]),
    ],
)
def test_top_n(freq_dict, n, expected):
    assert top_n(freq_dict, n) == expected
