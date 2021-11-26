from pig_latin import PigLatin
import unittest


class PigLatinTestCase(unittest.TestCase):
    'Unit test for pig_latin.py'

    def test_return_type(self):
        'Returns a string'
        received = PigLatin('apple')
        self.assertIsInstance(received.__str__(), str)


if __name__ == '__main__':
    unittest.main()


# print(f"translates a word beginning with a vowel: {translate('apple') == 'appleay'}")
# print(f"translates a word beginning with a consonant: {translate('banana') == 'ananabay'}")
# print(f"translates a word beginning with two consonants: {translate('cherry') == 'errychay'}")
# print(f"translates two words: {translate('eat pie') == 'eatay iepay'}")
# print(f"translates a word beginning with three consonants: {translate('three') == 'eethray'}")
# print(f"counts 'sch' as a single phoneme: {translate('school') == 'oolschay'}")
# print(f"counts 'qu' as a single phoneme: {translate('quiet') == 'ietquay'}")
# print(f"counts 'qu' as a consonant even when it's preceded by a consonant: {translate('square') == 'aresquay'}")
# print(f"translates many words: {translate('the quick brown fox') == 'ethay ickquay ownbray oxfay'}")

# write a test asserting that capitalized words are still capitalized
# (but with a different initial capital letter, of course) retain the
# punctuation from the original phrase
