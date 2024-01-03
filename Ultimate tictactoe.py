
import math
import random


def simulate_game(board, current_player):
    player = current_player
    while True:
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
        if not available_moves:
            return 0  
        x, y = random.choice(available_moves)
        board[x][y] = player

        result = CheckWin(board)
        if result == 1:
            return 1  
        elif result == 2:
            return 2 
        elif result == 3:
            return 0  

        player = 'X' if player == 'O' else 'O'

def monte_carlo_simulation(board, player, simulations=100000):
    legal_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
    results = {}

    
    for move in legal_moves:
        wins = 0
        for _ in range(simulations):
            temp_board = [row[:] for row in board]
            temp_board[move[0]][move[1]] = player
            result = simulate_game(temp_board, 'X')  
            if result == 1:
                wins += 1
        results[move] = wins

   
    best_move = max(results, key=lambda x: results[x])
    return best_move


A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
list_names = [A, B, C, D, E, F, G, H, I]

for board_index, board in enumerate(list_names):
    for i in range(3):
        row = []
        for j in range(3):
            row.append("-")
        board.append(row)

def PrintBoard(boards):
    for i in range(3):
        for board in boards:
            for j in range(3):
                print(board[i][j], end=" ")
            print("  ", end="")
        print("\n")

def transpose(board):
    return [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
    ]

X, O, S = ('X', 'O', '-')

def horizontal(board):
    for row in board:
        if all(square == O for square in row):
            return 1
        elif all(square == X for square in row):
            return 2
    return 0

def diag(board):
    if (board[0][0] == board[1][1] == board[2][2] == O) and board[0][0] is not S: 
        return 1
    elif (board[0][2] == board[1][1] == board[2][0] == O) and board[0][2] is not S:
        return 1
    elif (board[0][0] == board[1][1] == board[2][2] == X) and board[0][0] is not S:
        return 2
    elif (board[0][2] == board[1][1] == board[2][0] == X) and board[0][2] is not S:
        return 2
    return 0


winning_index_combinations = ['048', '246', '147', '345', '036', '258', '012', '678']

def checkWin(current_board):
    incomplete_board_check = False    
    for combination in winning_index_combinations:
        index_integer_set = set()
        for index_character in combination:
            temp_index_int = int(index_character)
            if current_board[temp_index_int] == 0 : 
                incomplete_board_check = True
            index_integer_set.add(current_board[temp_index_int])
        
        if len(index_integer_set) == 1:
            if X in index_integer_set:
                return 1
            if O in index_integer_set:
                return 2
            if 0 not in index_integer_set:
                print("Something Went Wrong")
    
    if incomplete_board_check :
        return 0
    else:
        return 3




def CheckWin(currentboards):
    result = (
        horizontal(currentboards) or
        horizontal(transpose(currentboards)) or
        diag(currentboards)
    )

    if result == 0:
        for row in currentboards:
            if S in row:
                return 0
        return 3
    
    return result

def currentboard():
    PrintBoard(list_names[:3])
    print()
    PrintBoard(list_names[3:6])
    print()
    PrintBoard(list_names[6:9])





gamestate = True
playerturn = 1
big_board = [0] * 9
playerturn = 1
big_result = 0

while big_result == 0:
    currentboard()
    choice = input("Which board do you want to play on (1-9)?")
    try:
        board_index = int(choice) - 1
        if 0 <= board_index < 9:
            selected_board = list_names[board_index]
            while big_result == 0:
                x, y = map(int, input("Enter row and column (e.g., '2 3') to place: ").split())

                if 1 <= x <= 3 and 1 <= y <= 3:
                    if playerturn == 1:
                    
                        if selected_board[x - 1][y - 1] == "-" and selected_board[x - 1][y - 1] != "O" and selected_board[x - 1][y - 1] != "X" :
                            selected_board[x - 1][y - 1] = "O"
                            print(f"'O' placed at row {x}, column {y}")
                            
                        else:
                            print("That square is already occupied. choose again")
                            x, y = map(int, input("Enter row and column (e.g., '2 3') to place: ").split())
                            selected_board[x - 1][y - 1] = "O"
                            print(f"'O' placed at row {x}, column {y}")
                    

                    else:
                        if selected_board[x - 1][y - 1] == "-" and selected_board[x - 1][y - 1] != "X" and selected_board[x - 1][y - 1] != "O":
                            selected_board[x - 1][y - 1] = "X"
                            print(f"'X' placed at row {x}, column {y}")
                            playerturn = 1
                        else:
                            print("That square is already occupied.")
                else:
                    print("Invalid row or column. Please enter row and column numbers between 1 and 3.")

                result = CheckWin(selected_board)
                if result == 1:
                    index_selectedboard = list_names.index(selected_board)
                    big_board.insert(index_selectedboard,X)
                    print("Player X wins on this board!")
                elif result == 2:
                    index_selectedboard = list_names.index(selected_board)
                    print("Player O wins on this board!")
                    big_board.insert(index_selectedboard,O)
                elif result == 3:
                    index_selectedboard = list_names.index(selected_board)
                    print("It's a draw on this board!")
                    big_board.insert(index_selectedboard,0)
                    
                currentboard()

                    
                if x == 1 and y == 1:
                    if CheckWin(list_names[0]) == 1 or CheckWin(list_names[0]) == 2:
                         selected_board = list_names[random.randint(0,8)]

                    else:
                        selected_board = list_names[0]
                                                
                elif x == 1 and y == 2:
                    if CheckWin(list_names[1]) == 1 or CheckWin(list_names[1]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                    else:
                        selected_board = list_names[1]

                elif x == 1 and y == 3:
                    if CheckWin(list_names[2]) == 1 or CheckWin(list_names[2]) == 2:
                        selected_board = list_names[random.randint(0,8)]
                    else:
                        selected_board = list_names[2]
        
                elif x == 2 and y == 1:
                    if CheckWin(list_names[3]) == 1 or CheckWin(list_names[3]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                    else:
                        selected_board = list_names[3]

                elif x == 2 and y == 2:
                    if CheckWin(list_names[4]) == 1 or CheckWin(list_names[4]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                            
                    else:
                        selected_board = list_names[4]
    
                elif x == 2 and y == 3:
                    if CheckWin(list_names[5]) == 1 or CheckWin(list_names[5]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                            
                    else:
                        selected_board = list_names[5]

                elif x == 3 and y == 1:
                    if CheckWin(list_names[6]) == 1 or CheckWin(list_names[6]) == 2:
                            selected_board = list_names[random.randint(0,8)]
    
                    else:
                        selected_board = list_names[6]
    
                elif x == 3 and y == 2:
                    if CheckWin(list_names[7]) == 1 or CheckWin(list_names[7]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                    
                    else:
                        selected_board = list_names[7]
        
                elif x == 3 and y == 3:
                    if CheckWin(list_names[8]) == 1 or CheckWin(list_names[8]) == 2:
                            selected_board = list_names[random.randint(0,8)]
                    else:
                        selected_board = list_names[8]

                big_result = checkWin(big_board)
                
                playerturn = 2



                ############################################################################

                if playerturn == 2 and big_result == 0:  
                    ai_move = monte_carlo_simulation(selected_board, 'O', simulations=1000)
                    selected_board[ai_move[0]][ai_move[1]] = "X"
                    x, y = ai_move[0]+1,ai_move[1]+1
                    print(f"AI 'X' placed at row {ai_move[0] + 1}, column {ai_move[1] + 1}")
                    playerturn = 1 

                currentboard()

                if x == 1 and y == 1:
                    if CheckWin(list_names[0]) == 1 or CheckWin(list_names[0]) == 2:
                        choose = input("Which board do you want to play on (1-9)?")
                        selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[0]
                        print("You are in board 1")
                                                
                elif x == 1 and y == 2:
                    if CheckWin(list_names[1]) == 1 or CheckWin(list_names[1]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[1]
                        print("You are in board 2")

                elif x == 1 and y == 3:
                    if CheckWin(list_names[2]) == 1 or CheckWin(list_names[2]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[2]
                        print("You are in board 3")
        
                elif x == 2 and y == 1:
                    if CheckWin(list_names[3]) == 1 or CheckWin(list_names[3]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[3]
                        print("You are in board 4")

                elif x == 2 and y == 2:
                    if CheckWin(list_names[4]) == 1 or CheckWin(list_names[4]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[4]
                        print("You are in board 5")
    
                elif x == 2 and y == 3:
                    if CheckWin(list_names[5]) == 1 or CheckWin(list_names[5]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[5]
                        print("You are in board 6")

                elif x == 3 and y == 1:
                    if CheckWin(list_names[6]) == 1 or CheckWin(list_names[6]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[6]
                        print("You are in board 7")
    
                elif x == 3 and y == 2:
                    if CheckWin(list_names[7]) == 1 or CheckWin(list_names[7]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[7]
                        print("You are in board 8")
        
                elif x == 3 and y == 3:
                    if CheckWin(list_names[8]) == 1 or CheckWin(list_names[8]) == 2:
                            choose = input("Which board do you want to play on (1-9)?")
                            selected_board = list_names[int(choose) - 1]
                    else:
                        selected_board = list_names[8]
                        print("You are in board 9")



            big_result = checkWin(big_board)  
            
                    
        else:
            break
                          
    except ValueError:
        print("Invalid input.")
    

if big_result == 1:
    print("X  has won")
elif big_result == 2:
    print("Player O has won the game!")
else:
    print("Stalemate!")

        