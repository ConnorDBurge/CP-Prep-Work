# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong = list()  # list to hold armstrong numbers
    for num in numbers:
        # number split into list of digits
        num_list = [int(num) for num in str(num)]
        exponent = len(num_list)  # number of digits in number

        sum = 0
        for digit in num_list:
            sum = sum + (digit ** exponent)

        if sum == num:
            armstrong.append(num)

    return armstrong
