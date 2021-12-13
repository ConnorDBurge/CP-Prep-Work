import re


class Recursion:
    count = 0

    def factorial(self, x):
        if x == 0:
            return 1
        return x * self.factorial(x - 1)

    def palindrome(self, string):
        chars = re.sub('\W', '', string.lower())

        if len(chars) <= 1:
            return True

        if chars[0] == chars[-1]:
            return self.palindrome(chars[1:-1])

        return False

    def bottles(self, num, original):
        print(
            f'{num} bottle{"s" if num > 1 else ""} of beer on the wall, {num} bottle{"s" if num > 1 else ""} of beer.')
        if num > 1:
            print(
                f'Take one down and pass it around, {num - 1} bottle{"s" if num - 1 > 1 else ""} of beer on the wall.')

        if num < 1:
            return print(
                f'Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, {original} bottles of beer on the wall.')

        self.bottles(num - 1, original)

    def roman_num(self, num):
        pass


recursion = Recursion()
recursion.bottles(5, 5)
