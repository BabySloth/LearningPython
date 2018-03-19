import random

def drawBoard():
    # This function clears terminal, prints out the board, and asks for user input
    # what globals do you need here?
    print('\033[H\033[J')
    print(' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]))
    print('-----------')
    print(' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]))
    print('-----------')
    print(' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]))
    if gameOver:
        # print who won the game?
    else:
        # ask for player input

def switchTurn():
    # what globals do you need here?
    # what do you need to change?

def processInput():
    # what globals do you need here?
    # i did this quickly last night - if you can think of a better way
    # go for it
    if userInput == "1":
        board[0][0] = currentPlayer
        switchTurn()
    if userInput == "2":
        board[0][1] = currentPlayer
        switchTurn()
    if userInput == "3":
        board[0][2] = currentPlayer
        switchTurn()
    if userInput == "4":
        board[1][0] = currentPlayer
        switchTurn()
    if userInput == "5":
        board[1][1] = currentPlayer
        switchTurn()
    if userInput == "6":
        board[1][2] = currentPlayer
        switchTurn()
    if userInput == "7":
        board[2][0] = currentPlayer
        switchTurn()
    if userInput == "8":
        board[2][1] = currentPlayer
        switchTurn()
    if userInput == "9":
        board[2][2] = currentPlayer
        switchTurn()

def checkWinner():
    # should scan the board for a winner
    # if there is a winner, should set the winner "X" or "O"
    # if there is a winner, should set gameOver to True

def playGame():
    # what globals do you need?
    # what do you need to set them to?
    while not gameOver:
        drawBoard()
        processInput()
        checkWinner()

playGame()
