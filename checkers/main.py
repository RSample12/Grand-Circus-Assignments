# Main.py
import checkers


def game():
    # build a board with size of user preference
    board_size = int(input('What size board would you like? '))
    new_board = checkers.build_board(board_size)
    print(new_board)

    # count number of red, black, and empty cells in new board
    red = checkers.get_count(new_board, 'Red')
    black = checkers.get_count(new_board, 'Black')
    empty = checkers.get_count(new_board, 'Empty')
    print(f'Red Cells: {red}\nBlack Cells: {black}\nEmpty Cells: {empty}')

if __name__ == '__main__':
    game()