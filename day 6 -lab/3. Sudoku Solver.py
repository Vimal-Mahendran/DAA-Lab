def solve_sudoku(board):
    if not board:
        return False
    
    if solve_helper(board):
        return True
    else:
        return False

def solve_helper(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in map(str, range(1, 10)):
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if solve_helper(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

board_to_solve = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solve_sudoku(board_to_solve)

for row in board_to_solve:
    print(row)
