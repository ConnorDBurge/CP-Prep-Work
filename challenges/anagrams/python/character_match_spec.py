from character_match import is_character_match
import unittest


class CharacterMatchUnitTest(unittest.TestCase):
    'Unit test for character_match.py'

    def test_return_type_bool(self):
        'returns type bool'
        test = is_character_match('charm', 'march')
        self.assertIsInstance(test, bool)

    def test_for_same_len(self):
        'test for same length strings'
        test = is_character_match('charm', 'march')
        self.assertEqual(test, True)

    def test_for_same_len(self):
        'test an empty string'
        test = is_character_match('', '')
        self.assertEqual(test, False)

    def test_return_true_for_true_anagram_1(self):
        'returns true for valid anagram'
        test = is_character_match('charm', 'march')
        self.assertEqual(test, True)

    def test_return_true_for_true_anagram_2(self):
        'returns true for valid anagram'
        test = is_character_match('CharM', 'mARcH')
        self.assertEqual(test, True)

    def test_return_true_for_true_anagram_3(self):
        'returns true for valid anagram'
        test = is_character_match('abcde2', 'c2abed')
        self.assertEqual(test, True)

    def test_return_true_for_true_anagram_4(self):
        'returns true for non-valid anagram'
        test = is_character_match('zach', 'attack')
        self.assertEqual(test, False)

    def test_return_true_for_True_anagram_5(self):
        'returns true for valid anagram'
        test = is_character_match('Anna Madrigal', 'A man and a girl')
        self.assertEqual(test, True)


if __name__ == '__main__':
    unittest.main()
