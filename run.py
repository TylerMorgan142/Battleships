from random import randint

# Legend
# @ = friendly ship
# . = empty/unknown space
# X = hit ship
# * = missed shot


player_board = [["."] * 5 for x in range(5)]
computer_board = [["."] * 5 for x in range(5)]

def print_board(board):
    """
    Prints the board where the game will take place.
    """
    print("0 1 2 3 4")
    for row in board:
        print(" ".join(row))



def add_player_ships(board):
    """
    Populates the the player's board with ships in random locations.
    """
    for ship in range(5):
        row = randint(0, 4)
        column = randint(0, 4)
        while board[row][column] == "@":
            row = randint(0, 4)
            column = randint(0, 4)   
        board[row][column] = "@"

def add_computer_ships(board):
    """
    Populates the the computer's board with ships in random locations.
    """
    for ship in range(5):
        row = randint(0, 4)
        column = randint(0, 4)
        global ship_locations
        ship_locations = board[row][column]
    
    




def player_guess(board):
    """
    Gets the players input for their guess of a row and column.
    """
    
    try:
        global guess_row
        guess_row = input("Please enter a row between 0-4\n")
        while  guess_row not in "01234":
            print("Row must be between 0-4")
            guess_row = input("Please enter a row between 0-4\n")   
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess()
    
    try:
        global guess_column
        guess_column = input("Please enter a column between 0-4\n")
        while  guess_column not in "01234":
            print("Column must be between 0-4")
            guess_column = input("Please enter a column between 0-4\n")
               
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess(computer_board)
   
    guess_row = int(guess_row)
    guess_column = int(guess_column)

    if board[guess_row][guess_column] == "X":
        print("You already guessed those coordinates")
        player_guess(computer_board)
    elif board[guess_row][guess_column] == "*":
        print("You already guessed those coordinates")
        player_guess(computer_board)
    
    

def check_for_hits(board):
    
    guess = board[guess_row][guess_column]
    if guess == ship_locations:
        print("Congratulations you hit a ship!")
        board[guess_row][guess_column] = "X"
    else:
        print("You missed!") 
        board[guess_row][guess_column] = "*"

    

def computer_guess(board):
    row = randint(0, 4)
    column = randint(0, 4)
    if board[row][column] == ".":
        print("Computer missed!")
        board[row][column] = "*"
    elif board[row][column] == "X" or board[row][column] == "*":
        computer_guess
    elif board[row][column] == "@":
        print("Computer successfully landed a shot!")
        board[row][column] = "X"
    print_board(player_board) 
    print_board(computer_board)
    new_round()

def new_game():
    add_player_ships(player_board)
    add_computer_ships(computer_board)
    print_board(player_board)
    print_board(computer_board)
    new_round()     

def new_round():
    player_guess(computer_board)
    check_for_hits(computer_board)
    computer_guess(player_board)

new_game()    