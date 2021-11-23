from anagram2 import anagrams_for, is_character_match
import unittest


class Anagrams(unittest.TestCase):
    'Unittest for anagrams.py'
    list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

    def test_for_returned_list(self):
        received = anagrams_for('threads', self.list_of_words)
        self.assertIsInstance(received, list)

    def test_for_is_character_match(self):
        received = is_character_match('trashed', 'hardest')
        expected = True
        self.assertEqual(received, expected)

    def test_returns_a_anagram_list(self):
        received = anagrams_for('threads', self.list_of_words)
        expected = ["threads", "trashed", "hardest", "hatreds"]
        self.assertEqual(received, expected)

    def test_returns_an_empty_list(self):
        received = anagrams_for("apple", self.list_of_words)
        expected = []
        self.assertEqual(received, expected)

    def test_return_true_for_whitespace(self):
        list_words = ['A man and a girl', 'Aman and a girl', 'Aand a gi']
        received = anagrams_for('Anna Madrigal', list_words)
        expected = ['A man and a girl', 'Aman and a girl']
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
