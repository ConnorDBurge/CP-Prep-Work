operations = 0


def linear_search(target, arr):
    for elem in arr:
        global operations
        operations += 1
        if elem == target:
            return True
    return False


arr_10 = [x for x in range(10)]
arr_100 = [x for x in range(100)]
arr_1000 = [x for x in range(1000)]
arr_10000 = [x for x in range(10000)]

# linear_search(10, arr_10)
# linear_search(100, arr_100)
# linear_search(1000, arr_1000)
linear_search(10000, arr_10000)
print('Num of operations:', operations)
