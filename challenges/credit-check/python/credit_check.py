def credit_check(string):
    credit_numbers = to_list(string)  # converts string to list of digits
    two_list = times_two(credit_numbers)  # doubles each digit in list
    final_list = sum_gt_9(two_list)  # numbers > 9 sum of its own digits
    sum = sum_all(final_list)  # get sum  of numbers in list

    if sum % 10 == 0:  # check validity
        return 'The number is valid!'

    return 'The number is invalid!'


def to_list(credit_card_numbers):
    digitList = [int(digit) for digit in credit_card_numbers]
    return digitList


def times_two(digit_list):
    credit_numbers = list()
    for i, num in enumerate(reversed(digit_list)):
        if i % 2 == 0:
            credit_numbers.insert(0, num)
        else:
            credit_numbers.insert(0, num * 2)
    return credit_numbers


def split_digits_sum(number):
    digitList = [int(digit) for digit in str(number)]
    sum = 0
    for digit in digitList:
        sum = sum + digit
    return sum


def sum_gt_9(array):
    final_list = list()
    for num in array:
        if num > 9:
            final_list.append(split_digits_sum(num))
        else:
            final_list.append(num)
    return final_list


def sum_all(array):
    sum = 0
    for num in array:
        sum = sum + num
    return sum
