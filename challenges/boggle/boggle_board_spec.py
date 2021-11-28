from boggle_board import BoggleBoard
import unittest


class BoggleBoardUnittest(unittest.TestCase):

    def test_initialization(self):
        'Creates a new blank board'
        received = BoggleBoard()  # new BoggleBoard
        expected = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_']
        ]
        self.assertEqual(received.board, expected)


if __name__ == '__main__':
    unittest.main()
