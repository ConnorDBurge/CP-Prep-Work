from calculate_mode import calculate_mode
import unittest


class ModeUnittest(unittest.TestCase):
    'Unit tests for mode.py'

    def test_return_list(self):
        received = calculate_mode([1, 2, 3, 3])
        self.assertIsInstance(received, list)

    def test_return_correct_mode_1(self):
        received = calculate_mode([1, 2, 3, 3])
        self.assertEqual(received, [3])

    def test_return_correct_mode_2(self):
        received = calculate_mode([1, 2, 3])
        self.assertEqual(received, [1, 2, 3])

    def test_return_correct_mode_3(self):
        received = calculate_mode([4.5, 0, 0])
        self.assertEqual(received, [0])

    def test_return_correct_mode_4(self):
        received = calculate_mode(["who", "what", "where", "who"])
        self.assertEqual(received, ["who"])


if __name__ == '__main__':
    unittest.main()
