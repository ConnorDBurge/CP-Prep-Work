def pad(array, min_size, value=None):
    padded = array

    if min_size <= len(array):
        return padded

    for i in range(0, min_size):
        try:
            array[i] = array[i]
        except IndexError:
            array.append(value)

    return padded
