import re

# String search
text = 'Hello world'
index = text.find('o')
print(index)  # 4

# create a list of all occurrences
text = 'Hello world'
indices = [i for i, char in enumerate(text) if char == 'o']
print(indices)  # [4, 7]

# create a list of all value indices
text = 'Hello world'
v = ['a', 'e', 'i', 'o', 'e']
indices = [i for i, char in enumerate(text) if char.lower() in v]
print(indices)  # [1, 4, 7]

# REGEX
text = 'Hello to Oscar Platoon'
pattern = r'[aeiou][^aeiou ]+[aeiou]'
vowel_sandwich = re.findall(pattern, text, re.I)
print(vowel_sandwich)  # ['ello', 'Osca', 'ato']

# re.search(pattern, text)
# re.findall(pattern, text)
# re.finditer(pattern, text)
# re.sub(pattern, replacement, text)

text = 'jadz'
pattern = r'a.z'
match = re.search(pattern, text)
print(match)
