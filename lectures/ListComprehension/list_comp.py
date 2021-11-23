full_list = [num for num in range(0, 100)]
# print(full_list)

odd_list = [num for num in range(0, 100, 2)]
# print(odd_list)

fizz_buzz_list = [num + 1 for num in range(
    0, 100) if num % 5 == 0 and num % 3 == 0]
print(fizz_buzz_list)
