from random import randint

# Legend
# @ = friendly ship
# . = empty/unknown space
# X = hit ship
# * = missed shot


player_board = [["."] * 5 for x in range(5)]
computer_board = [["."] * 5 for x in range(5)]
hidden_board = [["."] * 5 for x in range(5)]

player_score = 0
computer_score = 0

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
        while board[row][column] =="@":
            row = randint(0,4)
            column = randint(0,4)
        board[row][column] = "@"              


def player_guess(board):
    """
    Gets the players input for their guess of a row and column
    Asks the user to retry if their input is invalid
    """
    
    try:
        global guess_row
        guess_row = int(input("Please enter a row between 0-4\n"))
        while  guess_row not in range(0, 5):
            print("Row must be between 0-4")
            guess_row = int(input("Please enter a row between 0-4\n"))
            break 
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess(computer_board)
    
    try:
        global guess_column
        guess_column = int(input("Please enter a column between 0-4\n"))
        while  guess_column not in range(0, 5):
            print("Column must be between 0-4")
            guess_column = int(input("Please enter a column between 0-4\n"))
               
    except ValueError:
        print("Input must be a number between 0-4")
        player_guess(computer_board)

    if hidden_board[guess_row][guess_column] == "X":
        print("You already guessed those coordinates")
        player_guess(computer_board)
    elif board[guess_row][guess_column] == "*":
        print("You already guessed those coordinates")
        player_guess(computer_board)
    

 

def check_for_hits(board,real_board):
    """
    Compares the user's guess to a hidden board that stores the computer's ship locations
    Marks the location as either hit or miss on the board the player can see
    """

    if board[guess_row][guess_column] == "@":
        print("Congratulations, you hit a battleship!")
        real_board[guess_row][guess_column] = "X"
        increment_player_score()
    else:
        print("You missed!") 
        real_board[guess_row][guess_column] = "*"   
        
    

def computer_guess(board):
    """
    Gets the computer's guess by randonmly generating coordinates on the player's board
    """
    row = randint(0, 4)
    column = randint(0, 4)
    if board[row][column] == ".":
        print("Computer missed!")
        board[row][column] = "*"
    elif board[row][column] == "X" or board[row][column] == "*":
        computer_guess(player_board)
    elif board[row][column] == "@":
        print("Computer successfully landed a shot!")
        board[row][column] = "X"
        increment_computer_score()
    

def increment_player_score():
    """
    Increases the player's score by 1
    """
    global player_score
    player_score += 1
    
        

def increment_computer_score():
    """
    Increases the computer's score by 1
    """
    global computer_score
    computer_score += 1
        

def new_game():
    """
    Starts a new game
    """
    add_player_ships(player_board)
    add_computer_ships(hidden_board)
    new_round()     

def new_round():
    """
    Starts a new round of guessing
    Stops the game if the player's or computer's ships 
    have all been destroyed
    """ 
    while player_score < 5 and computer_score < 5:
        print(f"Player score = {player_score}")
        print(f"Computer score = {computer_score}")
        print_board(player_board) 
        print_board(computer_board)
        player_guess(computer_board)
        check_for_hits(hidden_board, computer_board)
        computer_guess(player_board)
    if player_score == 5:
            print("Congratulations, you sunk all the computer's battleships!")
            print("Thanks for playing")
    elif computer_score == 5:
            print("Game Over! The computer sunk all of your battleships!")
            print("Thanks for playing")
new_game()    