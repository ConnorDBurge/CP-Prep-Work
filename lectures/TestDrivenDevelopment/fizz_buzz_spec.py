import unittest  # imports the Unit Test library
from fizz_buzz import fizz_buzz, fizz_buzz_n, fizz_buzz_generic_n
# import the fizzbuzz method from fizzbuzz.py


class FizzbuzzTestCase(unittest.TestCase):  # inhereting from unittest class
    'Tests for fizz_buzz.py'

    def test_returns_a_list(self):
        'When you call fizz_buzz(), you should get a list back'
        self.assertIsInstance(fizz_buzz(), list)

    def test_returns_100_elements(self):
        'When you call fizz_buzz(), checks for 100 returned in list'
        returned_list = fizz_buzz()
        elements = len(returned_list)
        self.assertEqual(elements, 100)

    def test_fizz_and_buzz(self):
        'When you call fizz_buzz(), verify that Fizz and Buzz are populated correctly'

        returned_list = fizz_buzz()
        expected_output = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz", "Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]

        self.assertListEqual(returned_list, expected_output)

    def test_fizz_buzz_for_n_value(self):
        'When you call fizz_buzz(), verify that Fizz and Buzz are populated correctly for n elements'

        returned_list = fizz_buzz_n(20)
        expected_output = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz"]

        self.assertListEqual(returned_list, expected_output)

    def test_fizz_buzz_for_0_value(self):
        'When you call fizz_buzz(), verify that Fizz and Buzz are populated correctly for n elements'

        returned_list = fizz_buzz_n(0)
        expected_output = []

        self.assertListEqual(returned_list, expected_output)

    def test_fizz_buzz_for_generic(self):
        'When you call fizz_buzz(), verify that Fizz and Buzz are populated correctly for n elements with generic strings'

        returned_list = fizz_buzz_generic_n(20, 'Test', 'Case', 'TestCase')
        expected_output = [
            1, 2, "Test", 4, "Case", "Test", 7, 8, "Test", "Case", 11, "Test", 13, 14, "TestCase", 16, 17, "Test", 19, "Case"]

        self.assertListEqual(returned_list, expected_output)


if __name__ == '__main__':
    unittest.main()
