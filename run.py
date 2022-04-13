import random


board = [('0') * 5 for x in range(5)]
computer_board = [('0') * 5 for x in range(5)]
players_ships_coords = []
computer_ships_coords = []

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


def players_choice():
    """
    player choice of row and column
    """
    global computer_board
    try:
        row_choice = int(input('Choose your row: '))
        column_choice = int(input('Choose your column: '))
        coordinates = row_choice, column_choice
        if row_choice and column_choice > 5:
            raise ValueError('stay below 5')
        print(f'your shot:{coordinates}')
        return coordinates
    except ValueError as e:
        print(e)
        return players_choice()


def generate_random_coords():
    """
    Generates 2 random coordinates integers
    1 for row and 1 for column
    """
    row = int(random.randint(1, 5))
    column = int(random.randint(1, 5))
    # print(f'random row:{row} and column: {column}')
    return (row, column)


def generate_ships_coords():
    """
    Generates 5 random ship coordinates list
    """
    coords_list = []
    for x in range(0, 5):
        ships_coords = generate_random_coords()
        coords_list.append(ships_coords)
    # print(f'Coords list: {coords_list}')
    return coords_list


def add_players_ships_on_board(coords_list):
    """
    Add players ships to the board 
    with an @ using generates ships coords
    function and using the global keyword 
    to get access to the players board
    """
    global board

    for coords in coords_list:
        row, column = coords
        board[row - 1][column - 1] = "@"



        

def main():
    """
    Main game functions
    """
    global computer_ships_coords, players_ships_coords

    print("Battleship")
    computer_ships_coords = generate_ships_coords()
    # print(f'computer ship coords:{computer_ships_coords}')
    players_ships_coords = generate_ships_coords()
    # print(f'players ship coords:{players_ships_coords}')
    # add_players_ships_on_board(players_ships_coords)
    print_board(board)
    print_board(computer_board)

main()
players_choice()
