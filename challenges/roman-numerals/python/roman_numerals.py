decToRomanModern = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
]


def to_roman(num):
    romanStr = ''  # empty string to append to

    for obj in decToRomanModern:  # iterate through each list
        decimal = obj[0]  # store decimal
        roman = obj[1]  # store roman

        even_div = num // decimal  # get floored division of num / decimal

        for i in range(even_div):
            romanStr += roman  # append the roman value the even divisible amount of times

        num = num % decimal  # get remaining value to for next iteration

        if num == 0:  # if num has reached 0, we are done
            break

    return romanStr  # return roman numeral representation of num
