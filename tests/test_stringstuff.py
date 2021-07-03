import pytest
from stringstuff import show_reverse_letters


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
