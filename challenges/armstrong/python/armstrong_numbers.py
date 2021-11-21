# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong = list()  # list to hold armstrong numbers
    for i in numbers:
        # number split into list of digits
        num_list = [int(num) for num in str(i)]
        num_of_digits = len(num_list)  # number of digits in number

        sum = 0
        for digit in num_list:
            sum = sum + (digit ** num_of_digits)

        if sum == i:
            armstrong.append(i)

    return armstrong
