def factorial(num):
    if not isinstance(num, int):
        return None
    elif num < 0:
        return None
    elif num == 0:
        return 1

    return num * factorial(num - 1)
