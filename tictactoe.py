#Large
""" #1. Tic-tac-toe
Write a function move that accepts three arguments:
board = a 2-dimensional array that represents a 3x3 tic-tac-toe board
location = a 2-item tuple that specifies an cell on the board
player = a String, either "X" or "Y"
Return a copy of the board with the player String placed at the location.

Throw an error if:

The board is the wrong size
The location is already occupied by a player
The location is invalid
The player String is something other than "X" or "Y" """

board = [["-"],["-"],["-"],

         ["-"],["-"],["-"],

         ["-"],["-"],["-"]]

location = [[]]
playerA= "A"
playerB= "B"
playerturn = str(input("who's turn is it?\n"))

def board():
    print(board[0]) + "|" + (board[1]) + "|" + (board[2])
    print(board[3]) + "|" + (board[4]) + "|" + (board[5])
    print(board[6]) + "|" + (board[7]) + "|" + (board[8])
    return board


def turn(playerturn):
    if playerturn == "A":
        print(input("where on the board would you like to move?\n"))

turn(playerturn)