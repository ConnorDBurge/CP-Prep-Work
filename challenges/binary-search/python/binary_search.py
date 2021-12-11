def binary_search(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # make sure to round it down
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search(4, [-2, 3, 4, 7, 8, 9, 11, 13]))
