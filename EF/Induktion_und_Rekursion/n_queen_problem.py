import numpy as np

def check_square(row, column, board, n):
    # check if column is already occupied by a queen in one of the rows above
    i = row - 1
    while (i >= 0):
        if board[i][column] == 1:
            return False
        i -= 1

    # check north-western diagonal
    i = row - 1
    j = column - 1
    while ((i >= 0) and (j >= 0)):
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check north-eastern diagonal
    i = row - 1
    j = column + 1
    while ((i >= 0) and (j < n)):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

number_of_solutions = 0
def solve_queen_problem(board, n, row = 0):
    global number_of_solutions # can be done way prettier! for example with classes
    if (row == n):
        number_of_solutions += 1
        print(board)
        return
    
    for j in range(n):
        if (check_square(row, j, board, n)):
            board[row][j] = 1
            solve_queen_problem(board, n, row + 1)
            board[row][j] = 0

def run():
    n = 8
    board = np.zeros((n,n), dtype = int)
    solve_queen_problem(board, n)
    print("for n = {0:>2}".format(n), ", there are exactly", "{0:>15}".format(number_of_solutions), " solutions", sep = '')

run()