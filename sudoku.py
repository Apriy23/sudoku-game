import random

def generate_board(difficulty):
    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    remove_numbers(board, difficulty)
    return board

def fill_board(board):
    for i in range(0, 9, 3):
        fill_3x3_board(board, i, i)
    # Mengisi bagian lain
    fill_remaining(board)

def fill_3x3_board(board, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)
    index = 0
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums[index]
            index += 1

def fill_remaining(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if fill_remaining(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid_move(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def remove_numbers(board, difficulty):
    squares_to_remove = {
        'easy': 5,
        'medium': 10,
        'hard': 20
    }
    count = squares_to_remove[difficulty]
    while count > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count -= 1

def validate_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0
                if not is_valid_move(board, i, j, num):
                    board[i][j] = num
                    return False
                board[i][j] = num
    return True
