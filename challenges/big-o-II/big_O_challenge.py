# Explain, optimize, and benchmark your python code here.
import statistics
import time


def binary_search_10(target=9, arr=list(range(1, 10)), iterations=0):
    iterations += 1
    try:
        mid = len(arr) // 2  # mid index
        mid_value = arr[mid]  # mid value
        if target > mid_value:
            return binary_search_10(target, arr[mid:], iterations)
        elif target < mid_value:
            return binary_search_10(target, arr[:mid], iterations)
        else:
            return iterations
    except RecursionError:
        return iterations


def binary_search_100(target=99, arr=list(range(1, 100)), iterations=0):
    iterations += 1
    try:
        mid = len(arr) // 2  # mid index
        mid_value = arr[mid]  # mid value
        if target > mid_value:
            return binary_search_100(target, arr[mid:], iterations)
        elif target < mid_value:
            return binary_search_100(target, arr[:mid], iterations)
        else:
            return iterations
    except RecursionError:
        return iterations


def linear_search_10(target=9, arr=list(range(1, 10))):
    iterations = 0
    for value in arr:
        iterations += 1
        if target == value:
            return iterations
    else:
        return iterations


def linear_search_100(target=99, arr=list(range(1, 100))):
    iterations = 0
    for value in arr:
        iterations += 1
        if target == value:
            return iterations
    else:
        return iterations


# Reporting

functions = binary_search_10, binary_search_100, linear_search_10, linear_search_100

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
    for i in range(500):  # adjust accordingly so whole thing takes a few sec
        t0 = time.time()
        func()
        t1 = time.time()
        times[func.__name__].append((t1 - t0) * 1000)
    print(f'{func.__name__:>18} |', func(), 'iterations')

# alexcha8879@gmail.com
