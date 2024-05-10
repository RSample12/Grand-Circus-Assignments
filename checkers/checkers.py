# Checkers.py
"""
The application prompts the user to enter a square board size between minimum of 4 and maximum of 16.
The application prints out a random board where each cell is either empty or contains a red or black checker.
"""
from numpy import random
from numpy import count_nonzero
Spaces = ['Empty', 'Red', 'Black']


def build_board(num):
    arr = random.choice(Spaces, size=(num, num))
    return arr

def get_count(board, s):
    count = count_nonzero(board == s)
    return count

if __name__ == '__main__':
    print('file not intended as main...')