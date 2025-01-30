def is_palindrome(text):
    text = [i.lower() for i in text if i.isalpha()]
    return True if text == text[::-1] else False
