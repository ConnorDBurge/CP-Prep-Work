from collections import defaultdict


def char_count(str):
    counts = defaultdict(int)
    letters = [char for char in str if char != ' ']
    for char in letters:
        counts[char] += 1
    return counts
