from balance_parens import balance_parens
import unittest


class BalanceParen(unittest.TestCase):
    'Unittest BalanceParen.py'

    def test_return_type(self):
        received = balance_parens('abc(d)e(fgh))(i)j)k')
        self.assertIsInstance(received, str)

    def test_return_correct_1(self):
        received = balance_parens('(()()(')
        self.assertEqual(received, '()()')

    def test_return_correct_2(self):
        received = balance_parens('abc(d)e(fgh))(i)j)k')
        self.assertEqual(received, 'abc(d)e(fgh)(i)jk')


if __name__ == '__main__':
    unittest.main()
