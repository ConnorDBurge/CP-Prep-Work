from recursion_challenge import Recursion
import unittest


class RecursionTest(unittest.TestCase):
    recursion = Recursion()

    def test_factorial(self):
        self.assertEqual(self.recursion.factorial(10), 3628800)

    def test_palindrome(self):
        self.recursion.palindrome('racecar')
        self.assertEqual(self.recursion.palindrome('racecar'), True)


if __name__ == '__main__':
    unittest.main()
