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


def get_middle_three(string_in: str) -> str:

    """
    Given a string of odd length greater than 7 return a new string made of the middle three characters of a given string.
    """
    num_chars = len(string_in)
    if num_chars < 7:
        return ""
    mid = num_chars // 2
    result = f"{string_in[mid-1:mid+2]}"
    return result


def put_string_in_middle(s1: str, s2: str) -> str:
    """
    Exercise 2: Given two strings, s1 and s2,
    create a new string by appending s2 in the middle of s1
    """
    mid = len(s1) // 2
    return f"{s1[:mid]}{s2}{s1[mid:]}"


def first_middle_last(s1: str, s2: str) -> str:

    """
    Exercise Question 3: Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
    """
    s1_mid = s1[len(s1) // 2]
    s2_mid = s2[len(s2) // 2]
    s1_first = s1[0]
    s2_first = s2[0]

    s1_last = s1[-1]
    s2_last = s2[-1]
    return f"{s1_first}{s2_first}{s1_mid}{s2_mid}{s1_last}{s2_last}"


def put_lowercase_first(input_str: str) -> str:
    """
    Exercise 4: Arrange string characters such that lowercase letters come first
    """
    prefix = ""
    suffix = ""
    for char in input_str:
        if char.islower():
            prefix += char
        else:
            suffix += char
    return prefix + suffix


def count_char_types(input_str: str):
    """
    Exercise 5: Count all lower case, upper case, digits, and special symbols from a given string
    """
    chars = 0
    digits = 0
    symbols = 0

    for ch in input_str:
        if ch.isalpha():
            chars += 1
            continue
        if ch.isdigit():
            digits += 1
            continue
        symbols += 1

    return chars, digits, symbols


def create_string_mix(s1: str, s2: str) -> str:
    """
    Exercise 6: Given two strings, s1 and s2, create a mixed String using the following rules
    Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
    """
    string_mix = ""

    len1 = len(s1)
    len2 = len(s2)
    diff = abs(len1 - len2)
    i = min(len1, len2)
    for idx in range(i):
        string_mix += s1[idx]
        string_mix += s2[len2 - idx - 1]
    if diff == 0:
        return string_mix
    if i == len1:
        string_mix = string_mix + s2[diff - 1 :: -1]
    else:
        string_mix = string_mix + s1[-diff:]
    return string_mix


def balanced_string(s1: str, s2: str) -> bool:

    """
    Exercise 7: String characters balance Test
    We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters’ position doesn’t matter.
    """
    for char in s1:
        if char in s2:
            continue
        else:
            return False
    return True


def count_usa(input_str: str) -> int:
    """
    Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
    """

    temp_str = input_str.lower()
    return temp_str.count("usa")


def find_sum_and_avg_of_digits(str_in: str):
    """
    Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
    """
    curr_number = ""
    nums = []
    last_was_digit = False
    for ch in str_in:
        if ch.isdigit():
            curr_number += ch
            last_was_digit = True
        else:
            if last_was_digit:
                nums.append(int(curr_number))
                curr_number = ""
                last_was_digit = False
    if last_was_digit:
        nums.append(int(curr_number))
    return sum(nums), sum(nums) / len(nums)


def count_char_occurances(str_in: str) -> dict:
    """
    Given an input string, count occurrences of all characters within a string
    """
    result = {}
    compact_str = str_in.replace(" ", "")
    for ch in compact_str:
        if ch in result.keys():
            result[ch] += 1
        else:
            result[ch] = 1

    return result


def split_on_hyhens(str_in: str) -> list:
    """
    Split a given string on hyphens into several substrings and display each substring
    """
    result = str_in.split("-")
    return result


def remove_empty_strings(str_list: list) -> list:
    """
    Remove empty strings from a list of strings
    """
    for s in str_list:
        if s == "":
            str_list.remove(s)
    return str_list


def find_longest_substring(str_in: str) -> int:
    """
    Find the length of the longest substring without repeating
    characters
    """
    start = 0
    end = 0
    result = 0
    charSet = set()
    while end < len(str_in):
        if str_in[end] not in charSet:
            charSet.add(str_in[end])
            end += 1
            result = max(result, len(charSet))
        else:
            charSet.remove(str_in[start])
            start += 1
    return result

