from collections import defaultdict


def char_count(str):
    counts = defaultdict(int)  # default is an int
    letters = [char for char in str if char != ' ']  # list of characters
    for char in letters:
        counts[char] += 1  # one is default value
    return counts  # returns final dict object
