from balance_parens import balance_parens
import unittest


class BalanceParens(unittest.TestCase):
    'Unittest balance_parens.py'

    def test_return_type(self):
        '1. Returns string type'
        received = balance_parens('abc(d)e(fgh))(i)j)k')
        self.assertIsInstance(received, str)

    def test_return_correct_1(self):
        '2. Returns correct string for "(()()("'
        received = balance_parens('(()()(')
        self.assertEqual(received, '()()')

    def test_return_correct_2(self):
        '3. Returns correct string for "abc(d)e(fgh))(i)j)k"'
        received = balance_parens('abc(d)e(fgh))(i)j)k')
        self.assertEqual(received, 'abc(d)e(fgh)(i)jk')

    def test_return_correct_3(self):
        '4. Returns correct string for "()"'
        received = balance_parens('()')
        self.assertEqual(received, '()')

    def test_return_correct_4(self):
        '4. Returns correct string for "((a(b)c((("'
        received = balance_parens('((a(b)c(((')
        self.assertEqual(received, 'a(b)c')


if __name__ == '__main__':
    unittest.main()
