from random import randint

player_board = [["."] * 10 for x in range(10)]
computer_board = [["."] * 10 for x in range(10)]

def print_board(board):
    print("0 1 2 3 4 5 6 7 8 9")
    print("*******************")
    for row in board:
        print(" ".join(row))



print_board(player_board)        
print_board(computer_board)