from caesar_cipher import Cipher
import unittest


class TestCipher(unittest.TestCase):
    'Unittest cipher implementation'

    def test_return_type(self):
        received = Cipher('Hello Zach168! Yes here.', -5)
        self.assertIsInstance(received.caesar_cipher(), str)

    def test_return_correct_cipher_1(self):
        received = Cipher('Hello Zach168! Yes here.', 5)
        expected = 'Mjqqt Efhm168! Djx mjwj.'
        self.assertEqual(received.caesar_cipher(), expected)

    def test_return_correct_cipher_2(self):
        received = Cipher('Boy! What a string!', -5)
        expected = 'Wjt! Rcvo v nomdib!'
        self.assertEqual(received.caesar_cipher(), expected)

    def test_return_correct_cipher_3(self):
        received = Cipher('Hello Zach168! Yes here.', -5)
        expected = 'Czggj Uvxc168! Tzn czmz.'
        self.assertEqual(received.caesar_cipher(), expected)


if __name__ == '__main__':
    unittest.main()
