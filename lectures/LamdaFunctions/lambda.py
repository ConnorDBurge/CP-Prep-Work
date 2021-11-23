import functools

# Map function returns a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled = list(map(lambda num: num * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10, 12, 14, 16]


# Filter function returns a list
names = [
    'Alex Saunders',
    'Andrew Whitford',
    'Courtney Hussein',
    'Don Kelly',
    'Eric Burgher',
    'Jack Scott'
]
last_names = list(
    filter(lambda full_name: full_name.lower().split()[-1][0] == 's', names))
print(last_names)  # ['Alex Saunders', 'Jack Scott']


# Reduce function returns a single value
my_list = [1, 3, 5, 7, 8, 9, 13]
sum_of_list = functools.reduce(lambda num1, num2: num1 + num2, my_list)
print(sum_of_list)  # 46
