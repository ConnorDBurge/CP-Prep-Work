import re


def palindrome(word):
    chars = [char for char in str(word).lower() if re.match('[a-z0-9]', char)]
    while len(chars) > 1:
        if chars[0] != chars[-1]:
            return False
        else:
            chars.pop(0)
            chars.pop(-1)
    return True
