# return a list object
# should contain 100 elements
# 'Fizz' output for multiples of 3
# 'Buzz' output for multiples of 5
# 'Fizzbuzz' output for multiples of 3 and 5
# otherwise output the number

# loop through number '1-100'
# determine output
# add output to list
# finally, return list

def fizz_buzz():
    return fizz_buzz_n(100)


def fizz_buzz_n(n):
    fizz_buzz_list = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append('Fizzbuzz')
        elif i % 3 == 0:
            fizz_buzz_list.append('Fizz')
        elif i % 5 == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(i)

    return fizz_buzz_list


def fizz_buzz_generic_n(
        n,
        multiple_of_three,
        multiple_of_five,
        multiple_of_both):

    fizz_buzz_list = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append(multiple_of_both)
        elif i % 3 == 0:
            fizz_buzz_list.append(multiple_of_three)
        elif i % 5 == 0:
            fizz_buzz_list.append(multiple_of_five)
        else:
            fizz_buzz_list.append(i)

    return fizz_buzz_list
