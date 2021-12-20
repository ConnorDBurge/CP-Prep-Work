# O(1)          Constant Time
# O(log n)      Logarithmic Time
# O(n)          Linear Time
# O(n log n)    Log-Linear Time
# O(n^2)        Quadratic Time
# O(2^n)        Exponential Time

data = [4, 7, 6, 9, 24, 2, 9, 5, 6, 16, 1]


def constant_time(data, idx):  # O(1)
    return data[idx]


def linear_time(data, item):  # O(n)
    for elem in data:
        if item > elem:
            return elem


def quadratic_time(data):  # O(n^2)
    for d1 in data:
        for d2 in data:
            if d1 == d2:
                return True
    else:
        return False


def two_for_loops(data1, data2):  # O(2n) => O(n)
    for elem in data1:
        pass
    for elem in data2:
        pass
    return


def two_for_loops(data1, data2):  # O(n * n) => O(n^2)
    for elem in data2:  # O(n)
        idx = dat2.index(elem)  # O(n)
    return
