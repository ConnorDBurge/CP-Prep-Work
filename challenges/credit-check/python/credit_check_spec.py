from credit_check import credit_check, to_list, times_two, split_digits_sum, sum_gt_9, sum_all
import unittest


class CreditCheckUnitTest(unittest.TestCase):
    'Unit test for credit_check_spec.py'

    def test_return_type_string(self):
        'Returns a type string'
        test = credit_check('5541808923795240')
        self.assertIsInstance(test, str)

    def test_return_digit_list(self):
        'Return a list of digits from string'
        test = to_list('5541808923795240')
        self.assertIsInstance(test, list)

    def test_return_correct_digit_list(self):
        'Returns the correct digit list'
        test = to_list('5541808923795240')
        expectation = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
        self.assertEqual(test, expectation)

    def test_product_2_returns_list(self):
        'Successfully returns list from times_two()'
        testList = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
        test = times_two(testList)
        self.assertIsInstance(test, list)

    def test_product_2(self):
        'Successfully doubles every other digit starting from end'
        testList = [5, 5, 4, 1, 8, 0, 8, 9, 2, 3, 7, 9, 5, 2, 4, 0]
        test = times_two(testList)
        expected = [10, 5, 8, 1, 16, 0, 16, 9, 4, 3, 14,  9, 10, 2, 8, 0]
        self.assertEqual(test, expected)

    def test_split_digits_return_int(self):
        'Sussessfully returns int from split_digits_sum()'
        test = split_digits_sum(16)
        self.assertIsInstance(test, int)

    def test_split_digits(self):
        'Sussessfully splits and sums digits greater than length 2'
        test = split_digits_sum(16)
        expected = 7
        self.assertEqual(test, expected)

    def test_sum_digits_array(self):
        'Sussessfully returns list to be summed'
        test_array = [10, 5, 8, 1, 16, 0, 16, 9, 4, 3, 14,  9, 10, 2, 8, 0]
        test = sum_gt_9(test_array)
        expected = [1, 5, 8, 1, 7, 0, 7, 9, 4, 3, 5,  9, 1, 2, 8, 0]
        self.assertEqual(test, expected)

    def test_sum_all_numbers(self):
        'Sussessfully sum final numbers'
        test_array = [1, 5, 8, 1, 7, 0, 7, 9, 4, 3, 5,  9, 1, 2, 8, 0]
        test = sum_all(test_array)
        expected = 70
        self.assertEqual(test, expected)

    # Test cases for valid card numbers
    def test_valid_1(self):
        'Sussessfully check valid card number'
        test_string = '5541808923795240'
        test = credit_check(test_string)
        expected = 'The number is valid!'
        self.assertEqual(test, expected)

    def test_valid_2(self):
        'Sussessfully check valid card number'
        test_string = '4024007136512380'
        test = credit_check(test_string)
        expected = 'The number is valid!'
        self.assertEqual(test, expected)

    def test_valid_3(self):
        'Sussessfully check valid card number'
        test_string = '6011797668867828'
        test = credit_check(test_string)
        expected = 'The number is valid!'
        self.assertEqual(test, expected)

    # Test cases for non-valid card numbers
    def test_non_valid_1(self):
        'Sussessfully check non valid card number'
        test_string = '5541801923795240'
        test = credit_check(test_string)
        expected = 'The number is invalid!'
        self.assertEqual(test, expected)

    def test_non_valid_2(self):
        'Sussessfully check non valid card number'
        test_string = '4024007106512380'
        test = credit_check(test_string)
        expected = 'The number is invalid!'
        self.assertEqual(test, expected)

    def test_non_valid_3(self):
        'Sussessfully check non valid card number'
        test_string = '6011797668868728'
        test = credit_check(test_string)
        expected = 'The number is invalid!'
        self.assertEqual(test, expected)


if __name__ == '__main__':
    unittest.main()
