def is_character_match(string1, string2):  # Performs anagram test

    # get raw character list with no whitespace to compare against each other
    string1Split = [char for char in string1.lower() if char != ' ']
    string2Split = [char for char in string2.lower() if char != ' ']

    # first, check len of strings, if false then they are not anagrams
    if len(string1Split) == len(string2Split):
        # checks characters in strings
        for char in string1Split:
            if char not in string2Split:
                return False  # false when different char is found
            else:
                return True

    # returns if strings are not equal size
    return False


def anagrams_for(word, list_of_words):
    # uses logic from anagrams1 challenge to perform anagram test
    anagrams = list(
        filter(lambda ana: is_character_match(word, ana), list_of_words))
    return anagrams
