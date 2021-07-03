def show_reverse_letters(string_in: str) -> str:
    n = len(string_in)
    reverse_string = ""
    for i in range(n - 1, -1,-1):
        reverse_string += string_in[i]
    return reverse_string

