def binary_search(target, arr):
    try:
        mid = len(arr) // 2  # mid index
        mid_value = arr[mid]  # mid value
        if target > mid_value:
            return binary_search(target, arr[mid:])
        elif target < mid_value:
            return binary_search(target, arr[:mid])
        else:
            return True
    except RecursionError:
        return False


print(binary_search(14, [-2, 3, 4, 7, 8, 9, 11, 13]))
