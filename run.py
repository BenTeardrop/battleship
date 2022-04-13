import random


board = [('0') * 5 for x in range(5)]
computer_board = [('0') * 5 for x in range(5)]


def print_board(board):
    """
    Prints the board 5 x 5 coordinates
    and an horinzontal line 
    to separate the two boards
    """
    print ('---------')
    for row in board:
        print(" ".join(row))
    print ('---------')


def generate_random_coords():
    """
    Generates 2 random coordinates integers
    1 for row and 1 for column
    """
    row = int(random.randint(1, 5))
    column = int(random.randint(1, 5))
    # print(f'random row:{row} and column: {column}')
    return (row, column)


def generate_ship_coords():
    """
    Generates random ship coordinates list
    """
    coords_list = []
    for x in range(0, 5):
        ship_coords = generate_random_coords()
        coords_list.append(ship_coords)
    print(f'Coord list: {coords_list}')
    return coords_list
    

generate_ship_coords()
# generate_random_coords()
print_board(board)
print_board(computer_board)