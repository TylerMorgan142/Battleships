# Battleships

A recreating of the board game Battleships played against the computer made in the Python terminal.

## Game Rules

The player and computer have 5 battleships, randomly allocated on 5x5 grid

The player and computer guess coordinates on the grid, if there is a ship at those coordinates, a battleship is sunk and a point is gained.

First to sink all 5 battleships wins.

If the player and computer sink all battleships simultaneously, it is a draw.

## Features

### Welcome Message

![Screenshot of welcome message](assets/images/bshipswelcome.png)

This brief message welcomes the player to the game and explains what they must do to win the game. 

The scores are also displayed here.

### Input

![Screenshot of input box](assets/images/bships%20input.png)

The input box asks the player to input a number between 0-4 for a row and the again for a column.

![Screenshot of invalid input](assets/images/bshipsinputerror.png)
![Screenshot of repeated input](assets/images/bshipsinputduplicate.png)
![Screenshot of invalid input](assets/images/bshipsinputerrorexceedingvalue.png)

If the player enters coordinates that are not an integer, is a pair of coordinates they have already guessed or not on the board they are met with an error message and asked to retry their guess.


### Game Board
![Screenshot of game board before inputs are made](assets/images/bshipsboard.png)

The game board shows the coordinates 0-4, before any inputs are made the player can see only their own ship locations marked as "@".

![Screenshot of game board after inputs are made](assets/images/bshipsboardinputs.png)

When the player makes inputs, they can see the location they guessed and the location the computer guessed.

Successful hits are marked a "X" and misses are marked as "*"

## Testing

All code passes through the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) without any issues.

The program produces the expected results when inputs are entered including invalid inputs.

