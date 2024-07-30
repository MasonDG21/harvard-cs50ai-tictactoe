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
    #count number of X and O on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set() # create empty set to store possible actions.
    
    # New Actions are only possible when cells do not already contain an X or an O.
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions # returns the set of all possible actions for the current state of the board.

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # check if the action is valid
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action: Cell is not empty.")
    
    #create a copy of the current board so we don't mess up the original board.
    new_board = [[board[i][j] for j in range(len(board[i]))] for i in range(len(board))]
    
    # simulate the output by applying the action to the new board.
    new_board[action[0]][action[1]] = player(board)
    
    return new_board # returning the board we copied earlier in it's simulated state AFTER a given action.  

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows for a winner (3-in-a-row)
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # check columns for a winner (3-in-a-row)
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O
    
    # check diagonals for a winner
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None # return None if there is no winner.


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True # if there's a winner the game is over.
    
    # check if there are still EMPTY cells on the game board.
    for i in board:
        if EMPTY in i:
            return False
    return True # if there's no Empty cell and no winner. game is over.

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # check for a winner
    win = winner(board)
    
    if win == X:
        return 1 # return 1 if X wins.
    elif win == O:
        return -1 # return -1 if O wins.
    else:
        return 0 # return 0 if there's no winner but the game is over. (draw)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # get the current player from the current board state.
    current_player = player(board)
    
    def maximize(board):
        # if the game is over return the utility of the board.
        if terminal(board):
            return utility(board), None
        
        # set the initial value of v to negative infinity.
        v = -math.inf
        best_action = None
        
        # Loop through the possible actions
        for action in actions(board):
            # get the max value of current board
            min_value, _ = minimize(result(board, action))
            if min_value > v:
                v = min_value
                best_action = action
        return v, best_action
    
    def minimize(board):
        # like in maximize - if the game is terminal we want to return the utlity.
        if terminal(board):
            return utility(board), None
        
        # set initial value of v to positive infinity
        v = math.inf
        best_action = None
        
        # loop through the possible actions
        for action in actions(board):
            # get the max value of the current board.
            max_value, _ = maximize(result(board, action))
            if max_value < v:
                v = max_value
                best_action = action
        return v, best_action
    
    if current_player == X:
        _, optimal_action = maximize(board)
    else:
        _, optimal_action = minimize(board)
        
    return optimal_action