# The following code is used to test your board_clone function.

######################################
# Put your board_clone function here
######################################
def board_clone(board):
    return board

######################################
# Don't change anything below this point
######################################


original_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res_board = board_clone(original_board)

if not isinstance(res_board, list):
    print("The board clone function did not return a list.")
    exit()

if len(res_board) != 3:
    print("The board clone function did not return a board with 3 rows.")
    print(f"  Expected 3 rows but got {len(res_board)} rows.")
    exit()

for row in res_board:
    if not isinstance(row, list):
        print("The board clone function did not return a list of lists.")
        exit()
    if len(row) != 3:
        print("The board clone function did not return a board with 3 columns.")
        print(f"  Expected 3 columns but got {len(row)} columns.")
        exit()

expected_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
passed = True
for row in range(3):
    for col in range(3):
        if res_board[row][col] != expected_board[row][col]:
            print(f"The board cloning failed at row {row} and column {col}.")
            print(f"  Expected {expected_board[row][col]} but got {res_board[row][col]}.")
            passed = False
            continue
        res_board[row][col] = 0
        if original_board[row][col] != expected_board[row][col]:
            print(f"The board clone failed to make a deep copy of the board at row {row} and column {col}")
            print(f"  The original board was changed at row {row} and column {col}.")
            passed = False
            continue


if passed:
    print("The board clone function passed the test. well done!")
        