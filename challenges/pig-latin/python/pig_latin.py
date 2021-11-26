import re


class PigLatin():

    def __init__(self, string):
        self.string = self.translate(string)

    def __str__(self):
        return self.string

    def translate(self, words_passed):
        if words_passed == '':
            return ''
        pig_latin_words = list()  # []
        words = words_passed.split(' ')  # 'School' = ['School']
        for word in words:  # ['School']
            chars = [char.lower() for char in word]  # [s,c,h,o,o,l]
            while not re.match('[aeiouAEIOU]', chars[0]):  # [s,c,h,o,o,l] == True
                chars.append(chars.pop(0))  # [o,o,l,s,c,h]
            chars.append('a')  # [o,o,l,s,c,h,a]
            chars.append('y')  # [o,o,l,s,c,h,a,y]
            chars[0] = chars[0].upper() if word[0].isupper() else chars[0]
            pig_latin_words.append(''.join(chars))  # ['Oolschay']
        pig_latin = ' '.join(pig_latin_words)  # Oolschay
        return pig_latin  # Oolschay
