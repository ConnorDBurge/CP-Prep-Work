# The code is written as driver code. Can you convert it to Unit Test?
from armstrong_numbers import find_armstrong_numbers
import unittest  # imports the Unit Test library


class ArmstrongTestCases(unittest.TestCase):
    'Test for armstrong_numbers.py'

    def test_returns_a_list(self):
        self.assertIsInstance(find_armstrong_numbers([0]), list)

    def test_returns_100_elements(self):
        numbers = len(find_armstrong_numbers(list(range(0, 100))))
        self.assertEqual(numbers, 100)

    # def test_range_to_0(self):
    #     test_list = [0]
    #     expected_list = find_armstrong_numbers(test_list)
    #     self.assertListEqual(test_list, expected_list)


if __name__ == '__main__':
    unittest.main()


print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
print(find_armstrong_numbers(list(range(0, 100)))
      == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(find_armstrong_numbers(list(range(0, 999))) == [
      0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
