operations = 0


def binary_search(target, arr):
    try:
        global operations
        operations += 1
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


arr_10 = [x for x in range(10)]
arr_100 = [x for x in range(100)]
arr_1000 = [x for x in range(1000)]
arr_10000 = [x for x in range(10000)]

# bin  ary_search(10, arr_10)
# bin  ary_search(100, arr_100)
# bin  ary_search(1000, arr_1000)
binary_search(9999, arr_10000)
print('Num of operations:', operations)
