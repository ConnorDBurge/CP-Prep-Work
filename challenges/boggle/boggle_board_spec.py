from boggle_board import BoggleBoard
import unittest


class BoggleBoardUnittest(unittest.TestCase):

    def test_initialization(self):
        'Creates a new blank board'
        received = BoggleBoard()  # new BoggleBoard
        expected = [
            ['•'], ['•'], ['•'], ['•'],
            ['•'], ['•'], ['•'], ['•'],
            ['•'], ['•'], ['•'], ['•'],
            ['•'], ['•'], ['•'], ['•']
        ]
        self.assertEqual(received.board, expected)

    def test_random_seed(self):
        received = BoggleBoard(4)  # new BoggleBoard
        expected = [
            ['A'], ['R'], ['A'], ['O'],
            ['T'], ['O'], ['I'], ['E'],
            ['D'], ['A'], ['N'], ['S'],
            ['G'], ['A'], ['L'], ['R']
        ]
        self.assertEqual(received.shake(), expected)


if __name__ == '__main__':
    unittest.main()
