import re

# Does a string contain a phone number?


def has_phone_number(input_string):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return re.search(pattern, input_string)

# Get a phone number back from a string


def get_phone_number(input_string):
    pattern = r'\d{3}-\d{3}-\d{4}'
    numbers = re.findall(pattern, input_string)
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers


# Gets and returns all phone numbers from an inputted string
def get_all_phone_numbers(input_string):
    pattern = r'\d{3}-\d{3}-\d{4}'
    numbers = re.findall(pattern, input_string)
    return numbers


# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    string = re.sub(r'(\d{3})-', 'XXX-', input_string)
    return string


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    pattern = r'\(?\d{3}[-.)\s]?\s?\d{3}[-.]?\d{4}'
    numbers = re.findall(pattern, input_string)
    modified = []
    for number in numbers:
        string = ''
        digits = re.findall(r'\d', number)
        i = 0
        for digit in digits:
            string += digit
            i += 1
            if i % 3 == 0:
                string += '-'
        last_digit = string[-1]
        last_string = re.sub(r'-\d$', '', string)
        last_string += last_digit
        modified.append(last_string)
    final_string = ''
    for i, num in enumerate(modified):
        if i != len(modified) - 1:
            final_string += f'{num}, '
        else:
            final_string += f'{num}'
    return final_string
