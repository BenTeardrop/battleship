board = [('0') * 5 for x in range(5)]
computer_board = [('0') * 5 for x in range(5)]


def print_board(board):
    """
    Prints the board and an horinzontal line 
    to separate the two boards
    """
    print ('---------')
    for row in board:
        print(" ".join(row))
    print ('---------')


print_board(board)