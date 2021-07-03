import pytest
from stringstuff import show_reverse_letters, find, count


@pytest.mark.parametrize(
    "string_in, expected",
    [
        ("fox", "xof"),
        ("snow", "wons"),
        ("working", "gnikrow"),
    ],
)
def test_show_reverse_letters(string_in, expected):
    actual = show_reverse_letters(string_in)
    assert actual == expected


@pytest.mark.parametrize(
    "word, letter, index, expected",
    [
        ("poster", "o", 0, 1),
        ("superman", "p", 3, -1),
        ("psuperman", "p", 0, 0),
        ("psuperman", "p", 2, 3),
    ],
)
def test_find(word, letter, index, expected):
    actual = find(word, letter, index)
    assert actual == expected


@pytest.mark.parametrize(
    "word, letter, expected",
    [
        ("banana", "a", 3),
        ("spiderman", "q", 0),
    ],
)
def test_count(word, letter, expected):
    actual = count(word, letter)
    assert actual == expected
