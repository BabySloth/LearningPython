import random

gameOver = False
currentPlayer = "X"
winner = ""

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
availableMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

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
        '''#print who won the game?'''
        if not winner:
            print 'It\'s a tie'
        else:
            print winner + " won the game"

def switchTurn():
    # Player X will always go first
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

def processInput():
	global userInput
	global currentPlayer
	userInput = None
	validMove = False
    # Forces user to play a move that is valid
	while not validMove:
		userInput = raw_input("Input a number 1-9 that is not used already") 
		if userInput in availableMoves:			
			# Prevents user from making the same move
			availableMoves.remove(userInput)
			validMove = True

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
	'''# should scan the board for a winner'''
	# if there is a winner, should set the winner "X" or "O"
	# if there is a winner, should set gameOver to True
	global gameOver
	global availableMoves
	global winner

	moveList = []
	row = 0
	diagonalLeftRight = []
	diagonalRightLeft = []
	while row < 3:
		column = 0
		while column < 3:
            # Horizontal moves
			moveList.append(board[row][column])
            # Diagonal
			if column == row:
				diagonalLeftRight.append(board[row][column])
			if column + row == 2:
				diagonalRightLeft.append(board[row][column])
			column += 1
		row += 1


	column = 0
	while column < 3:
		row = 0
		while row < 3:
            # Vertical moves
			moveList.append(board[row][column])
			row += 1
		column += 1

    # Adds diagonal to end of list
	moveList.extend(diagonalLeftRight)
	moveList.extend(diagonalRightLeft)

	index = 0
	while index < len(moveList) - 3:
		if moveList[index] == moveList[index + 1] == moveList[index + 2]:
			winner = moveList[index]
		index += 3

    # If there is a winner, the game is over or is a tie (all moves used)
	if winner or not availableMoves:	
		gameOver = True
		drawBoard()	
		print "end of game"		

def playGame():
	'''
	Ask player if they want to play against a computer or a bot
	'''
	validChoice = False
	global singleOrDual
	while not validChoice:
		singleOrDual = raw_input("Press '1' or bot and '2' for dual")
		if singleOrDual in ['1', '2']:
			validChoice = True
	print singleOrDual

	while not gameOver:
		drawBoard()
		processInput()
		checkWinner()

playGame()
