import string
import random


class BoggleBoard:

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        new_board = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_']
        ]
        for row in new_board:
            print(''.join(row))
        print()
        return new_board

    def shake(self):
        for row in self.board:
            for i, cell in enumerate(row):
                row[i] = random.choice(string.ascii_uppercase)
            print(''.join(row))
        print()


board = BoggleBoard()
while True:
    selection = input()
    if selection == 'shake!':
        print()
        board.shake()
    elif selection == 'q':
        break
    else:
        selection = None
