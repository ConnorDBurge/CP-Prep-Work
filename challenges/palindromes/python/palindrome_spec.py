from palindrome import palindrome
import unittest


class PalindromeTestCase(unittest.TestCase):
    'Test case for palindrome.py'

    def test_return_type(self):
        received = palindrome('racecar')
        self.assertIsInstance(received, bool)

    def test_return_true_1(self):
        received = palindrome('racecar')
        self.assertEqual(received, True)

    def test_return_true_2(self):
        received = palindrome('Noon')
        self.assertEqual(received, True)

    def test_return_true_3(self):
        received = palindrome('ciVic')
        self.assertEqual(received, True)

    def test_return_true_4(self):
        received = palindrome(404)
        self.assertEqual(received, True)

    def test_return_true_5(self):
        received = palindrome('A man, a plan, a canal -- Panama')
        self.assertEqual(received, True)

    def test_return_true_6(self):
        received = palindrome('Sore was I ere I saw Eros.')
        self.assertEqual(received, True)

    def test_return_false_1(self):
        received = palindrome('nice')
        self.assertEqual(received, False)

    def test_return_false_2(self):
        received = palindrome(123)
        self.assertEqual(received, False)

    def test_return_false_3(self):
        received = palindrome('bomb')
        self.assertEqual(received, False)


if __name__ == '__main__':
    unittest.main()
