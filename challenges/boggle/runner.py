from boggle_board import BoggleBoard

board = BoggleBoard(4)
board.print_board()
while True:
    selection = input()
    if selection == '':
        board.shake()
        board.print_board()
    elif selection == 'q':
        break
    else:
        print(board.includes_word(selection))
