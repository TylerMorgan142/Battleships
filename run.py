from random import randint

player_board = [["."] * 5 for x in range(5)]
computer_board = [["."] * 5 for x in range(5)]

player_score = 0
computer_score = 0

print(f"Player score = {player_score}")
print(f"Computer_score = {computer_score}")
def print_board(board):
    """
    Prints the board where the game will take place.
    """
    print("0 1 2 3 4")
    for row in board:
        print(" ".join(row))



def add_player_ships(board):
    """
    Populates the board with ships in random locations.
    """
    for ship in range(5):
        row = randint(0, 4)
        column = randint(0, 4)
        while board[row][column] == "*":
            row = randint(0, 4)
            column = randint(0, 4)   
        board[row][column] = "*"

def add_computer_ships():


    for ship in range(5):
        row = randint(0, 4)
        column = randint(0, 4)
        return row, column




def player_guess():
    """
    Gets the players input for their guess of a row and column.
    """
    try:
        guess_row = int(input("Please enter a row between 0-4\n"))
        while  guess_row not in range(0, 4):
            print("Row must be between 0-4")
            guess_row = int(input("Please enter a row between 0-4\n"))    
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess()
    
    try:
        
        guess_column = int(input("Please enter a column between 0-4\n"))
        while  guess_column not in range(0, 4):
            print("Column must be between 0-4")
            guess_row = int(input("Please enter a column between 0-4\n"))
            return guess_column    
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess()
    return guess_row, guess_column

def check_for_hits():
    computer_ships = add_computer_ships()
    guess = player_guess()
    if guess == computer_ships:
        print("Congratlations you hit a ship!")
        global player_score
        player_score += 1
    else:
        print("You missed!")     





add_player_ships(player_board)
print_board(player_board)
print_board(computer_board)
check_for_hits()



