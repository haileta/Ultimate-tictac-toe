# Tic Tac Toe Project
# Uses PyGame Community Edition
# And Minimax/Alpha-beta pruning
# for i in range(0,2,2)
import sys

X, O, S = ('X', 'O', ' ')

def transpose(board):
    return [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
    ]

def horizontal(board):
    for row in board:
        if all(square == X for square in row):
            return 1
        elif all(square == O for square in row):
            return 2
    return 0

def diag(board):
    if (board[0][0] == board[1][1] == board[2][2] == X) and board[0][0] is not S: # checking the diagonal entries 
        return 1
    elif (board[0][2] == board[1][1] == board[2][0] == X) and board[0][2] is not S:
        return 1
    elif (board[0][0] == board[1][1] == board[2][2] == O) and board[0][0] is not S:
        return 2
    elif (board[0][2] == board[1][1] == board[2][0] == O) and board[0][2] is not S:
        return 2
    return 0

def CheckWin(currentboard):
    result = (
        horizontal(currentboard) or
        horizontal(transpose(currentboard)) or
        diag(currentboard)
    )
    
    if result == 0:
        for row in currentboard:
            if S in row:
                return 0
        return 3
    
    return result
    
gameboard = [
    [S, S, X],
    [S, O, O],
    [S, O, X]
]


print("Result:", CheckWin(gameboard))


            
'''
def PrintBoard(currentboard):
    print(currentboard[0:3])
    print(currentboard[3:6])
    print(currentboard[6:9])




def MiniMax(currentboard, playerturn, turnsplayed):
    # returns a move and a score
    bestmove = None
    
    tempboard = currentboard
    winner = CheckWin(tempboard)
    if winner == 1:
        return (None, turnsplayed - 10)
    elif winner == 2:
        return (None, 10 - turnsplayed)
    elif winner == 3:
        return (None, 0)
    
    if playerturn == 1:
        maxscore = -sys.maxsize
        bestmove = None
        for possiblemove in GetPossibleMoves(tempboard):
            tempboard[possiblemove] = 1
            (bestmove, score) = MiniMax(tempboard, 2, turnsplayed+1)
            tempboard[possiblemove] = 0
            if score > maxscore:
                maxscore = score
                bestmove = possiblemove
        return (bestmove, maxscore)

    else:
        minscore = sys.maxsize
        bestmove = None
        for possiblemove in GetPossibleMoves(tempboard):
            tempboard[possiblemove] = 2
            (bestmove, score) = MiniMax(tempboard, 1, turnsplayed+1)
            tempboard[possiblemove] = 0
            if score < minscore:
                minscore = score
                bestmove = possiblemove
        return (bestmove, minscore)


def GetPossibleMoves(currentboard):
    PossibleMoves = []
    for i in range(0,9):
        if currentboard[i] == 0:
            PossibleMoves.append(i)
    return PossibleMoves





gameboard = [0] * 9 
playerturn = 1 #1 is player 1, 2 is player 2
gamestate = 0 #0 for playing, 1 for 1 wins, 2 for 2 wins, 3 for draw
turnsplayed = 0

while(gamestate == 0):
    PrintBoard(gameboard)
    if(playerturn == 1):
        # Get player's input
        playermove = int(input("Choose a space 0 through 8: "))
        while(gameboard[playermove] != 0):
            playermove = input("Invalid move; choose again: ")
        gameboard[playermove] = 1
        playerturn = 2
        turnsplayed = turnsplayed+1
    else:
        #get AI's input
        (aimove, score) = MiniMax(gameboard, playerturn, turnsplayed)
        print(aimove)
        gameboard[aimove] = 2
        playerturn = 1
        turnsplayed = turnsplayed+1
    gamestate = CheckWin(gameboard)
    print(gamestate) 
'''



