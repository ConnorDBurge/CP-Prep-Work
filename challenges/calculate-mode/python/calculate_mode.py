from collections import defaultdict


def calculate_mode(array):
    mode = list()
    counts = defaultdict(int)
    max = 0

    for i in array:  # track each count and max count
        counts[i] += 1
        max = counts[i] if counts[i] > max else max

    for k, v in counts.items():  # add modes to list
        if v == max:
            mode.append(k)

    return mode
