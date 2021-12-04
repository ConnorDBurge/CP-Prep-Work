from stock_picker import picker
import unittest


class TestPicker(unittest.TestCase):

    def test_return_type(self):
        received = picker([17, 3, 6, 9, 15, 8, 6, 1, 10])
        self.assertIsInstance(received, list)

    def test_return_list_1(self):
        received = picker([17, 3, 6, 9, 15, 8, 6, 1, 10])
        expected = [1, 4]
        self.assertEqual(received, expected)

    def test_return_list_2(self):
        received = picker([3, 17, 6, 9, 18, 15, 6, 1, 10])
        expected = [0, 4]
        self.assertEqual(received, expected)

    def test_return_list_3(self):
        received = picker([1, 17, 6, 9, 8, 15, 6, 3, 19])
        expected = [0, 8]
        self.assertEqual(received, expected)

    def test_return_list_4(self):
        received = picker([19, 17, 6, 9, 8, 15, 6, 3, 1])
        expected = [2, 5]
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
