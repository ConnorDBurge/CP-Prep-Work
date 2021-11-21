def credit_check(string):
    result = 'The number is invalid!'

    credit_numbers = to_list(string)
    two_list = times_two(credit_numbers)
    final_list = sum_gt_9(two_list)
    sum = sum_all(final_list)

    if sum % 10 == 0:
        return 'The number is valid!'

    return result


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
