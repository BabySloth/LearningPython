gameOver = False
currentPlayer = "X"
winner = ""
gameOver = False
userInput = None

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
        drawBoard()
        if not winner:
            print 'It\'s a tie'
        else:
            print winner
    else:
        userInput = None
        # Forces user to play a move that is valid
        while userInput not in availableMoves:
            userInput = raw_input("Input a number 1-9 that is not used already")
        # Prevents user from making the same move
        availableMoves.remove(userInput)



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

    '''Horizontal and Diagonal checking'''
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

    '''Vertical checking'''
    column = 0
    while column < 3:
        row = 0
        while row < 3:
            # Vertical moves
            moveList.append(board[column][row])
            row += 1
        column += 1

    # Adds diagonal to end of list
    moveList.append(diagonalLeftRight)
    moveList.append(diagonalRightLeft)

    '''
    Checks for winner
    '''

    index = 0
    while index < len(moveList) - 3:
        if moveList[index] == moveList[index + 1] == moveList[index + 2]:
            winner = moveList[index]
        index += 3

    # If there is a winner, the game is over or is a tie (all moves used)
    if winner or not availableMoves:
        gameOver = True
        print "end of game"

def playGame():
    # what globals do you need?
    # what do you need to set them to?
    while not gameOver:
        drawBoard()
        processInput()
        checkWinner()

playGame()
