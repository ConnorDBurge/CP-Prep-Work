from char_count import char_count
import unittest


class CharacterMatchUnitTest(unittest.TestCase):
    'Unit tests for char_count.py'

    def test_return_type(self):
        received = char_count("aaabbc")
        self.assertIsInstance(received, dict)

    def test_simple_string(self):
        received = char_count("aaabbc")
        expected = {
            'a': 3,
            'b': 2,
            'c': 1
        }
        self.assertEqual(received, expected)

    def test_complex_string(self):
        received = char_count("an apple a day will keep the doctor away")
        expected = {
            "a": 6,
            "e": 4,
            "l": 3,
            "p": 3,
            "w": 2,
            "d": 2,
            "o": 2,
            "t": 2,
            "y": 2,
            "k": 1,
            "h": 1,
            "i": 1,
            "c": 1,
            "n": 1,
            "r": 1
        }
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
