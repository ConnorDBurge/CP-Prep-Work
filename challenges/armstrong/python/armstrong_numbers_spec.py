# The code is written as driver code. Can you convert it to Unit Test?
from armstrong_numbers import find_armstrong_numbers
import unittest  # imports the Unit Test library


class ArmstrongTestCases(unittest.TestCase):
    'Test for armstrong_numbers.py'

    def test_returns_a_list(self):
        'Checks if find_armstrong_numbers() returns a list'
        self.assertIsInstance(find_armstrong_numbers([0]), list)

    def test_returns_a_list_with_14_elements(self):
        'Checks if find_armstrong_numbers() returns 999 elements'
        test_list = list(range(0, 999))
        length_of_list = len(find_armstrong_numbers(test_list))
        self.assertEqual(length_of_list, 14)

    def test_range_to_8(self):
        'Checks if find_armstrong_numbers() returns an armstrong list 0 - 8'
        test_list = find_armstrong_numbers(list(range(0, 8)))
        expected_list = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(test_list, expected_list)

    def test_range_to_100(self):
        'Checks if find_armstrong_numbers() returns an armstrong list 0 - 100'
        test_list = find_armstrong_numbers(list(range(0, 100)))
        expected_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(test_list, expected_list)

    def test_range_to_999(self):
        'Checks if find_armstrong_numbers() returns an armstrong list 0 - 999'
        test_list = find_armstrong_numbers(list(range(0, 999)))
        expected_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
        self.assertListEqual(test_list, expected_list)


if __name__ == '__main__':
    unittest.main()
