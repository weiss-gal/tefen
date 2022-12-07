import functools
import random

logfile = open('tictactoe.log', 'wt')
cache = None
cache_stats = {'hit': 0, 'miss': 0}

def encode_move(board, human_symbol):
    return ''.join(functools.reduce(lambda x, y: x + y, board, [])) + human_symbol

def get_cached_result(board, human_symbol):
    global cache
    if cache is None:
        cache = {}
    
    encoded_move = encode_move(board, human_symbol)
    if encoded_move in cache:
        cache_stats['hit'] += 1
        return cache[encoded_move]
    
    cache_stats['miss'] += 1
    return None
    
def cache_result(board, human_symbol, result):
    global cache
    if cache is None:
        cache = {}
    
    encoded_move = encode_move(board, human_symbol)
    cache[encoded_move] = result

def log(msg):
    logfile.write(msg + '\r')
    #print("LOG: " + msg)
    
def get_clean_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def display_board(board):
    line_separator = '\n' + 5 * '-' + '\n'
    print()
    print(line_separator.join(['|'.join(row) for row in board]))
    print()

def board_full(board):
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

# gets human move as a 2-tuple of (row, col)
def get_human_move():
    row = None
    while row == None:
        print('Enter row')
        row = input()
        if row not in ['1', '2', '3']:
            print('Please enter 1, 2, or 3')
            row = None
        else:
            row = int(row) - 1
    col = None
    while col == None:
        print('Enter column')
        col = input()
        if col not in ['1', '2', '3']:
            print('Please enter 1, 2, or 3')
            col = None
        else:
            col = int(col) - 1
    return row, col 

def get_next_move_symbol(board):
    if functools.reduce(lambda x, y: x + y, board, []).count('X') == functools.reduce(lambda x, y: x + y, board, []).count('O'):
        return 'X'
    else:
        return 'O'

def is_human_turn(board, human_symbol):
    return get_next_move_symbol(board) == human_symbol

def clone_board(board):
    return [row[:] for row in board]

# get all possible moves as an n-tuple of 2-tpules of (move, board clone)
def get_next_moves(board):
    next_move_symbol = get_next_move_symbol(board)

    next_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board_copy = clone_board(board)
                board_copy[row][col] = next_move_symbol
                next_moves.append(((row, col), board_copy))
    
    return next_moves

def _check_move(board, human_symbol):
    computer_symbol = 'X' if human_symbol == 'O' else 'O'
    is_last_move_human = not is_human_turn(board, human_symbol)
    
    if board_full(board) and not is_win(board, human_symbol) and not is_win(board, computer_symbol):
        return 'tie'

    if is_last_move_human:
        # a human move is a loss win if the human wins at this turn or all next moves are a loss
        if is_win(board, human_symbol):
            return 'loss'

        next_moves = get_next_moves(board)
        if all([check_move(move[1], human_symbol) == 'loss' for move in next_moves]):
            return 'loss'

        # a human move is a win if one of teh next moves is a win
        if any([check_move(move[1], human_symbol) == 'win' for move in next_moves]):
            return 'win'
    else:    
        # a computer move is a win if the computer wins at this turn or all next moves are a win
        if is_win(board, computer_symbol):
            return 'win'

        next_moves = get_next_moves(board)
        if all([check_move(move[1], human_symbol) == 'win' for move in next_moves]):
            return 'win'

        # a computer move is a loss if one of the next moves is a loss
        if any([check_move(move[1], human_symbol) == 'loss' for move in next_moves]):
            return 'loss'

    # if none of the above conditions are met, the move is neither a win nor a loss, nor a tie
    return None

def check_move(board, human_symbol):
    # check if the move is cached
    cached_result = get_cached_result(board, human_symbol)
    if cached_result is not None:
        return cached_result
    
    result = _check_move(board, human_symbol)
    cache_result(board, human_symbol, result)
    return result

def get_computer_move(board, human_symbol):
    next_moves_results = [(move, check_move(board, human_symbol)) for move, board in get_next_moves(board)]

    # if there are any winning moves, pick one of them randomly
    winning_moves = [move for move, result in next_moves_results if result == 'win']
    if winning_moves:
        log(f'choosing winning move {winning_moves}')
        return random.choice(winning_moves)

    # if there are unlosing moves, pick one of them randomly
    unlosing_moves = [move for move, result in next_moves_results if result is None]
    if unlosing_moves:
        log(f'choosing unclosing move {unlosing_moves}')
        return random.choice(unlosing_moves) 
    
    # if there are a tie moves, pick one of them randomly
    tie_moves = [move for move, result in next_moves_results if result == 'tie']
    if tie_moves:
        log(f'choosing tie move {tie_moves}')
        return random.choice(tie_moves)

    # if there are no winning moves, no unlosing moves, and no tie moves, then there must be a losing move
    losing_moves = [move for move, result in next_moves_results if result == 'loss']
    log(f'Somthing is very wrong! choosing losing move {losing_moves}')

    return random.choice(losing_moves)

def is_win(board, symbol):
    # Check rows
    for row in board:
        if row.count(symbol) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False

def print_computer_delay():
    import time
    
    output = 'Thinking'
    for i in range(len(output)):
        print(output[i], end='', flush=True)
        time.sleep(0.1)

    computer_delay = random.randint(2, 5)
    for i in range(computer_delay):
        print('.', end='', flush=True)
        time.sleep(0.2)
    print()

# Tic Tac Toe
# ###########

banner = 'Welcome to Tic Tac Toe!'
print(banner)
print('#' * len(banner))

human_symbol = None
print('Do you want to be X or O?')
while not human_symbol:
    human_symbol = input().upper()
    if human_symbol not in ['X', 'O']:
        print('Please enter X or O')
        human_symbol = None

board = get_clean_board()
winner = None
while winner == None and not board_full(board):
 
    display_board(board)
    
    if is_human_turn(board, human_symbol):
        print("It's your turn")
        human_move = get_human_move()
        while board[human_move[0]][human_move[1]] != ' ':
            print('That space is taken')
            human_move = get_human_move()

        board[human_move[0]][human_move[1]] = human_symbol
    else:
        print_computer_delay()
        computer_move = get_computer_move(board, human_symbol)
        print(f'Computer move is Row:{computer_move[0] + 1}, Col:{computer_move[1] + 1}')
        board[computer_move[0]][computer_move[1]] = 'X' if human_symbol == 'O' else 'O'

    
    if is_win(board, 'X'):
        winner = 'X'
    elif is_win(board, 'O'):
        winner = 'O'
        
display_board(board)
if winner == human_symbol:
    print('You win!')
elif winner:
    print('Computer wins!')
else:
    print('Tie game!')

log(f'Cache Stats: {cache_stats}')

logfile.close()