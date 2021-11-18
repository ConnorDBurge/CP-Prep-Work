array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)


def linear_search(value_to_find, array_to_search_through):
    index = 0
    for value in array_to_search_through:
        if value == value_to_find:
            return index
        index += 1
    return None


def global_linear_search(value_to_find, array_to_search_through):
    index = 0
    indices = []
    for value in array_to_search_through:
        if value == value_to_find:
            indices.append(index)
        index += 1
    return indices
