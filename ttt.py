import random

global winner
global board

board = [	[1, 2, 3] , 
			[4, 5, 6] , 
			[7, 8, 9] ]

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
	board = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]
	listMoves = []
	diagonal1 = []
	diagonal2 = []
	row = 0
	winner = ""
	while row < 3:
		#Horizontal checking
		column = 0
		while column < 3:
			listMoves.append(board[row][column])
			if row == column:
				diagonal1.append(board[row][column])
			if row + column == 2:
				diagonal2.append(board[row][column])
			column += 1
		#Vertical checking 
		'''if column''' 
		row += 1
	column = 0
	while column < 3:
		row = 0
		while row < 3:
			listMoves.append(board[row][column])
			print listMoves
			row += 1
		column += 1
	listMoves.append(diagonal1)
	listMoves.append(diagonal2)


	index = 0
	while index < len(listMoves) - 2:
		if listMoves[index] == listMoves[index + 1] == listMoves[index + 2]:
			winner = listMoves[index]
		index += 3

	if not winner:
		return 
	return winner

def playGame():
    # what globals do you need?
    # what do you need to set them to?
    while not gameOver:
        drawBoard()
        processInput()
        checkWinner()

playGame()
