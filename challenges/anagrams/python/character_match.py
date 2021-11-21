# Strips whitespace from strings
def stringStripper(string):
    stringList = []
    for char in string:
        if char != ' ':
            stringList.append(char)
    return stringList


def is_character_match(string1, string2):

    # get raw characters with no whitespace
    string1Split = stringStripper(string1.lower())
    string2Split = stringStripper(string2.lower())

    # first, check len of strings
    if len(string1Split) == len(string2Split):
        # checks characters in strings
        for char in string1Split:
            if char not in string2Split:
                return False
            else:
                return True

    # returns if strings are not equal size
    return False
