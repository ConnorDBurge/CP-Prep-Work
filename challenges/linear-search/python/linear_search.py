def linear_search(value_to_find, array_to_search_through):
    index_list = linear_search_helper(
        value_to_find, array_to_search_through, True)
    if index_list == []:
        return None
    return index_list[0]


def global_linear_search(value_to_find, array_to_search_through):
    return linear_search_helper(value_to_find, array_to_search_through, False)


def linear_search_helper(value_to_find, array_to_search_through, find_first_index):
    index = 0
    indices = []
    for value in array_to_search_through:
        if value == value_to_find:
            indices.append(index)
            if find_first_index:
                return indices
        index += 1
    return indices
