import pytest
from stringstuff import (
    balanced_string,
    count_char_occurances,
    count_char_types,
    count_usa,
    create_string_mix,
    find_longest_substring,
    find_max_character,
    find_sum_and_avg_of_digits,
    first_middle_last,
    put_lowercase_first,
    put_string_in_middle,
    remove_empty_strings,
    show_reverse_letters,
    find,
    count,
    get_middle_three,
    split_on_hyhens,
    pig_latin,
)


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


@pytest.mark.parametrize(
    "string_in, expected",
    [
        ("JhonDiPeta", "DiP"),
        ("JaSonAy", "Son"),
        ("fish", ""),
    ],
)
def test_get_middle_three(string_in, expected):
    actual = get_middle_three(string_in)
    assert actual == expected


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("Ault", "Kelly", "AuKellylt"),
        ("Help", "fishing", "Hefishinglp"),
    ],
)
def test_put_string_in_middle(s1, s2, expected):
    actual = put_string_in_middle(s1, s2)
    assert actual == expected


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("America", "Japan", "AJrpan"),
        ("Forrester", "Bicycle", "FBeyre"),
    ],
)
def test_first_middle_last(s1, s2, expected):
    actual = first_middle_last(s1, s2)
    assert actual == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("TheQuickBrownFox", "heuickrownoxTQBF"),
        ("PyNaTive", "yaivePNT"),
    ],
)
def test_put_lowercase_first(input_str, expected):
    actual = put_lowercase_first(input_str)
    assert actual == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("P@#yn26at^&i5ve", (8, 3, 4)),
    ],
)
def test_count_char_types(input_str, expected):
    actual = count_char_types(input_str)
    assert actual == expected


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("Gossamer", "fisher", "Groeshssaimfer"),
        ("fisher", "Gossamner", "friesnhmearssoG"),
        ("Abc", "Xyz", "AzbycX"),
    ],
)
def test_create_string_mix(s1, s2, expected):
    actual = create_string_mix(s1, s2)
    assert actual == expected


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("Yn", "PYnative", True),
        ("Yn", "Basketball", False),
        ("bY", "Basketball", False),
    ],
)
def test_balanced_string(s1, s2, expected):
    actual = balanced_string(s1, s2)
    assert actual == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Welcome to USA. usa awesome, isn't it?", 2),
        ("Weusalcome to USA. usa awesome, isn't it?", 3),
    ],
)
def test_count_usa(input_str, expected):
    actual = count_usa(input_str)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("Math=75, English=85, Science=90", (250, 250 / 3)),
        ("Math=75, English=85, Science=90 Frogs", (250, 250 / 3)),
    ],
)
def test_find_sum_and_avg_of_digits(str_in, expected):
    actual = find_sum_and_avg_of_digits(str_in)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("apple", {"a": 1, "p": 2, "l": 1, "e": 1}),
        (
            "boris had a baby inch",
            {
                "b": 3,
                "o": 1,
                "i": 2,
                "r": 1,
                "s": 1,
                "h": 2,
                "a": 3,
                "d": 1,
                "y": 1,
                "n": 1,
                "c": 1,
            },
        ),
    ],
)
def test_count_char_occurances(str_in, expected):
    actual = count_char_occurances(str_in)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("this-is-a-test-string", ["this", "is", "a", "test", "string"]),
    ],
)
def test_split_on_hyphens(str_in, expected):
    actual = split_on_hyhens(str_in)
    assert actual == expected


@pytest.mark.parametrize(
    "str_list, expected",
    [
        (
            ["this", "", "test", "", "should", "", "work"],
            ["this", "test", "should", "work"],
        ),
    ],
)
def test_remove_empty_strings(str_list, expected):
    actual = remove_empty_strings(str_list)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("abcabcbbb", 3),
        ("bbbbbb", 1),
        ("pwwkew", 3),
        ("au", 2),
        ("dvdf", 3),
    ],
)
def test_find_longest_substring(str_in, expected):
    actual = find_longest_substring(str_in)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("hello world", "ellohay orldway"),
        ("disco ball", "iscoday allbay"),
    ],
)
def test_pig_latin(str_in, expected):
    actual = pig_latin(str_in)
    assert actual == expected


@pytest.mark.parametrize(
    "str_in, expected",
    [
        ("basketball book", "b"),
        ("forrest gump", "r"),
        ("the return of the jedi", "e"),
    ],
)
def test_find_max_character(str_in, expected):
    actual = find_max_character(str_in)
    assert actual == expected
