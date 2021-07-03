def show_reverse_letters(string_in: str) -> str:
    n = len(string_in)
    reverse_string = ""
    for i in range(n - 1, -1, -1):
        reverse_string += string_in[i]
    return reverse_string


def make_duckling_names():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter in "OQ":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


def find(word: str, letter: str, index) -> int:
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def count(word: str, letter: str) -> int:
    """
    Returns the number of times letter appears in word
    """
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count
