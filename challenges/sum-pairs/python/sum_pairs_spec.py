from sum_pairs import sum_pairs
import unittest


class SumPairUnitTest(unittest.TestCase):
    'Unit test for sum_pairs()'

    def test_for_returned_list(self):
        'Checks if sum_pairs() returns a list'
        self.assertIsInstance(sum_pairs([0], 0), list)

    def test_for_sum_pairs_on_empty_list(self):
        'Checks on empty list'
        test = sum_pairs([], 9)
        result = 'unable to find pairs'
        self.assertEqual(test, result)

    def test_for_sum_pairs_9(self):
        'Returns a list of sum pairs for 9'
        test = sum_pairs([1, 2, 3, 4, 5], 9)
        result = [[4, 5]]
        self.assertEqual(test, result)

    def test_for_sum_pairs_7(self):
        'Returns a list of sum pairs for 7'
        test = sum_pairs([1, 2, 3, 4, 5], 7)
        result = [[2, 5], [3, 4]]
        self.assertEqual(test, result)

    def test_for_sum_pairs_27(self):
        'Returns a list of sum pairs for 7'
        test = sum_pairs([3, 1, 5, 8, 2], 27)
        result = 'unable to find pairs'
        self.assertEqual(test, result)


if __name__ == '__main__':
    unittest.main()
