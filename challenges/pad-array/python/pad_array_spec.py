from pad_array import pad
import unittest


class PadTestCase(unittest.TestCase):
    'Unittest for pad.py'

    def test_return_type(self):
        received = pad([1, 2, 3], 5)
        self.assertIsInstance(received, list)

    def test_return_correct_list_1(self):
        received = pad([1, 2, 3], 3)
        self.assertEqual(received, [1, 2, 3])

    def test_return_correct_list_2(self):
        received = pad([1, 2, 3], 5)
        self.assertEqual(received, [1, 2, 3, None, None])

    def test_return_correct_list_3(self):
        received = pad([1, 2, 3], 5, 'apple')
        self.assertEqual(received, [1, 2, 3, 'apple', 'apple'])

    def test_return_correct_list_4(self):
        received = pad([1, 2, 3], 0, 'apple')
        self.assertEqual(received, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
