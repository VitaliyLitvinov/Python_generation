def is_pangram(text):
    list_digit = ''.join(text.split()).lower()
    return len(set(list_digit)) == 26