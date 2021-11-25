def pad(array, min_size, value=None):
    padded = array
    while(len(padded) < min_size):
        padded.append(value)
    return padded
