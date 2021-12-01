import random


class BoggleBoard:

    def __init__(self, random_seed=None):
        self.board = [["•"] for _ in range(16)]  # create a new board
        if random_seed is not None:
            random.seed(random_seed)

    def print_board(self):
        print('-------------')
        for i, cell in enumerate(self.board):
            print(f'{cell[0]:<3} ', end='')
            if (i + 1) % 4 == 0:  # every 4 cells, add new row
                if not i > 12:  # don't add new line after 4th row
                    print('\n')

    def shake(self):
        dice_sides = [
            ['A', 'A', 'E', 'E', 'G', 'N'], ['E', 'L', 'R', 'T', 'T', 'Y'],
            ['A', 'O', 'O', 'T', 'T', 'W'], ['A', 'B', 'B', 'J', 'O', 'O'],
            ['E', 'H', 'R', 'T', 'V', 'W'], ['C', 'I', 'M', 'O', 'T', 'U'],
            ['D', 'I', 'S', 'T', 'T', 'Y'], ['E', 'I', 'O', 'S', 'S', 'T'],
            ['D', 'E', 'L', 'R', 'V', 'Y'], ['A', 'C', 'H', 'O', 'P', 'S'],
            ['H', 'I', 'M', 'N', 'Q', 'U'], ['E', 'E', 'I', 'N', 'S', 'U'],
            ['E', 'E', 'G', 'H', 'N', 'W'], ['A', 'F', 'F', 'K', 'P', 'S'],
            ['H', 'L', 'N', 'N', 'R', 'Z'], ['D', 'E', 'I', 'L', 'R', 'X']]

        random.shuffle(dice_sides)
        for i, _ in enumerate(self.board):
            self.board[i][0] = random.choice(dice_sides[i])
            self.board[i][0] = 'Qu' if self.board[i][0] == 'Q' else self.board[i][0]

        return self.board

    def includes_word(self, word):
        word_chars = [char.upper() for char in word]
        board_chars = []
        for i, _ in enumerate(self.board):
            board_chars.append(self.board[i][0])
        for i, _ in enumerate(word_chars):
            if not word_chars[i] in board_chars:
                return False
        return True
