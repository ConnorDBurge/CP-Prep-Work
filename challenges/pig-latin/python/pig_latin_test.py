from pig_latin import PigLatin
import unittest


class PigLatinTestCase(unittest.TestCase):
    'Unit test for pig_latin.py'

    def test_return_type(self):
        'Returns a string'
        received = PigLatin('apple').__str__()
        self.assertIsInstance(received, str)

    def test_return_correct_1(self):
        'Returns an empty string'
        received = PigLatin('').__str__()
        expected = ''
        self.assertEqual(received, expected)

    def test_return_correct_2(self):
        'Returns correct string'
        received = PigLatin('apple').__str__()
        expected = 'appleay'
        self.assertEqual(received, expected)

    def test_return_correct_3(self):
        'Returns correct string'
        received = PigLatin('banana').__str__()
        expected = 'ananabay'
        self.assertEqual(received, expected)

    def test_return_correct_4(self):
        'Returns correct string'
        received = PigLatin('cherry').__str__()
        expected = 'errychay'
        self.assertEqual(received, expected)

    def test_return_correct_5(self):
        'Returns correct string'
        received = PigLatin('eat pie').__str__()
        expected = 'eatay iepay'
        self.assertEqual(received, expected)

    def test_return_correct_6(self):
        'Returns correct string'
        received = PigLatin('three').__str__()
        expected = 'eethray'
        self.assertEqual(received, expected)

    def test_return_correct_7(self):
        'Returns correct string'
        received = PigLatin('school').__str__()
        expected = 'oolschay'
        self.assertEqual(received, expected)

    def test_return_correct_8(self):
        'Returns correct string'
        received = PigLatin('quiet').__str__()
        expected = 'uietqay'
        self.assertEqual(received, expected)

    def test_return_correct_9(self):
        'Returns correct string'
        received = PigLatin('the quick brown fox').__str__()
        expected = 'ethay uickqay ownbray oxfay'
        self.assertEqual(received, expected)

    def test_return_correct_10(self):
        'Returns correct string'
        received = PigLatin('The Quick Brown Fox').__str__()
        expected = 'Ethay Uickqay Ownbray Oxfay'
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
