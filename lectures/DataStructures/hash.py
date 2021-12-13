import hashlib


class HashTable:
    def __init__(self):
        self.hash_table = dict()

    def hash(self, data):
        string = str(data)
        sum = 0
        for i in range(len(string)):
            sum += ord(string[i])
        index = hash(sum * 1.5) % 2069
        self.hash_table[index] = data


table = HashTable()
table.hash('abcdefg')
table.hash('dfgdfgdf')
table.hash('erwer3')
print(table.hash_table)
