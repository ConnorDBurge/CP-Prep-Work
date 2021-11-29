from bubble_sort import BubbleSort
import unittest


class TestBubbleSort(unittest.TestCase):

    sort1 = BubbleSort([4, 3, 5, 0, 1])
    sort2 = BubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_return_type(self):
        self.assertIsInstance(self.sort1, BubbleSort)

    def test_correct_sort_1(self):
        expected = [0, 1, 3, 4, 5]
        self.assertEqual(self.sort1.sorted, expected)

    def test_correct_num_of_swaps_sort_1(self):
        self.assertEqual(self.sort1.iterations, 4)

    def test_correct_sort_2(self):
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.sort2.sorted, expected)

    def test_correct_num_of_swaps_sort_2(self):
        self.assertEqual(self.sort2.iterations, 10)


if __name__ == '__main__':
    unittest.main()
