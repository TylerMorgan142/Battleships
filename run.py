from random import randint

player_board = [["."] * 10 for x in range(10)]
computer_board = [["."] * 10 for x in range(10)]

def print_board(board):
    """
    Prints the board where the game will take place.
    """
    print("0 1 2 3 4 5 6 7 8 9")
    for row in board:
        print(" ".join(row))



def add_ships(board):
    """
    Populates the board with ships in random locations.
    """
    for ship in range(10):
        row = randint(0, 9)
        column = randint(0, 9)
        while board[row][column] == "*":
            row = randint(0, 9)
            column = randint(0, 9)   
        board[row][column] = "*"




add_ships(player_board)
print_board(player_board)
print_board(computer_board)



