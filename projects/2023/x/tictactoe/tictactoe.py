"""
Tic Tac Toe Player
"""

import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #Check the number of plays each player has completed
  
    # Using for loop
    # initializing the for loop variables
    i=0
    j=0
    xcount = 0
    ocount = 0
    nullcount = 0
    #iterating through the board 2d list
    for i in range(3):
        for j in range(3):
            value =board[i]
            if value[j] == X:
                xcount += 1
            elif value[j] == O:
                ocount += 1 
            else:
                nullcount += 1 
            j+=1
        i+=1
    #working out whose turn it is 
    # if X has less turns than O it is X move next
    # if O has less turns than X it is O move next

    if xcount<=ocount:
        return(X)
    else:
        return(O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #initialize an empty set
    availableactions = set()

    #initialize loop variables
    i=0
    j=0
    for i in range(3):
        for j in range(3):
            value =board[i]
            # if the board[i,j] position is empty, this position is added to
            # the available actions set
            if value[j] == EMPTY:
                move=(i,j)
                availableactions.add(move)
            j+=1
        i+=1
    # the full set of available actions is returned
    return(availableactions)
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid move")
    else:
        #copy board to new board
        newboard = initial_state()
        for i in range(3):
            for j in range(3):
                # copy the value of the board to the new board
                newboard[i][j] = board[i][j]
                j+=1
            i+=1
        #figure out whose turn it is using the player(board) method use the
        # action tuple to set the value of the position to X or O
        newboard[action[0]][action[1]] = player(board)
        # the updated board is returned
        return(newboard)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    i=0
    j=0
    # check winning condition    
    for i in range(3):
        for j in range(3):                
            # check if this node is the . 
            # i.e three of their moves in a row horizontally, vertically, or diagonally (left or right).
            #vertical win
            if i-1 >= 0 and i+1 <= 2 and board[i][j] != EMPTY:
                if board[i][j] == board[i-1][j] and board[i][j] == board[i+1][j]:
                    return board[i][j]
            #horzontal win
            if j-1 >= 0 and j+1 <= 2 and board[i][j] != EMPTY:
                if board[i][j] == board[i][j-1] and board[i][j] == board[i][j+1]:
                    return board[i][j]
            #left digonal win
            if i-1 >= 0 and j-1 >= 0 and j+1 <= 2 and i+1 <= 2 and board[i][j] != EMPTY:
                if board[i][j] == board[i-1][j-1] and board[i][j] == board[i+1][j+1]:
                    return board[i][j]
            #right diagonal win
            if i-1 >= 0 and j-1 >= 0 and j+1 <= 2 and i+1 <= 2 and board[i][j] != EMPTY:
                if board[i][j] == board[i+1][j-1] and board[i][j] == board[i-1][j+1]:
                    return board[i][j]
            j+=1
        i+=1
    #if there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # define if game board is full
    gameboardfull = True
    for i in range(3):
        for j in range(3):
            value =board[i]
            if value[j] == EMPTY:
                gameboardfull = False
            j+=1
        i+=1
    if (gameboardfull == True or winner(board) != None ):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def  minimaxutil(board, depth : int, maximizingPlayer : bool, alpha, beta):
    # implementation based on the tutorial at 
    # https://papers-100-lines.medium.com/the-minimax-algorithm-and-alpha-beta-pruning-tutorial-in-30-lines-of-python-code-e4a3d97fa144
    if (depth==0) or (terminal(board)):
        return utility(board), None

    if maximizingPlayer:
        value = float('-inf')
        moves = actions(board)
        # for each action run the minimax function recursively until best move for that action is
        # found based on the minimax algorithm https://en.wikipedia.org/wiki/Minimax
        for action in moves:
            child = result(board,action)
            tmp = minimaxutil(child, depth-1, False, alpha, beta)[0]
            #print("min called in max ,depth = ",depth, " value ",tmp)
            if tmp > value:
                #print(" *** value = ",value, "  **** tmp = ", tmp)
                value = tmp
                bestaction = action

            if value >= beta:
                break
            alpha = max(alpha, value)

    else:
        value = float('inf')
        moves = actions(board)
        for action in moves:
            child = result(board,action)
            
            tmp = minimaxutil(child, depth-1, True, alpha, beta)[0]
            # print("max called in min ,depth = ",depth, " value ",tmp)
            if tmp < value:
                #print(" *** value = ",value, "  **** tmp = ", tmp)
                value = tmp
                bestaction = action
                #print("best move ",bestaction)
            if value <= alpha:
                break
            beta = min(beta, value)
    #print("best move ",best_movement)
    return value, bestaction

def minimax(board):
    # set the maximizing player based on the player whose turn it is 
    if player(board) == X:
        maximizingplayer = True
    else:
        maximizingplayer = False
    # If the board is a terminal board, the minimax function should return None
    if terminal(board):
        return None
    else:
        # call the minimax algoritm implementation function minimaxutil for the maximizing player 
        # and setting alpha and beta to -inf and +inf respectively
        temporary = minimaxutil(board, 15, maximizingplayer, alpha=float('-inf'), beta=float('inf'))
        # return only the best move from the value, best move tuple output of the minimaxutil function
        return temporary[1]




    