import string
import re


class Cipher:

    def __init__(self, string, shift_amount):
        self.string = string
        self.shift_amount = shift_amount

    def caesar_cipher(self):
        cipher = ''  # output
        alphabet = list(string.ascii_lowercase)  # a - z
        for char in self.string:  # for each char in string
            if re.match('[a-zA-Z]', char):  # if letter
                # index of letter in alphabet
                index = alphabet.index(char.lower())
                # move index by shift_amount
                cipher_index = index + self.shift_amount
                # add -26 if shift_amount is less than 0
                cipher_index += 0 if self.shift_amount < 0 else -26
                # append correct case letter to cipher
                if char.isupper():
                    cipher += alphabet[cipher_index].upper()
                else:
                    cipher += alphabet[cipher_index]
            else:  # add non-letters to cipher
                cipher += char
        return cipher  # return final cipher string
