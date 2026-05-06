N = 4

# -------------------------------
# 1. BACKTRACKING APPROACH
# -------------------------------
def is_safe(board, row, col):
    # Check left side (row)
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Upper diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Lower diagonal
    i, j = row+1, col-1
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_bt(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_bt(board, col + 1):
                return True

            board[i][col] = 0   # Backtrack

    return False


def run_backtracking():
    board = [[0]*N for _ in range(N)]

    if solve_bt(board, 0):
        print("Backtracking Solution:")
        for row in board:
            print(row)
    else:
        print("No solution")


# -------------------------------
# 2. BRANCH & BOUND APPROACH
# -------------------------------
def run_branch_and_bound():
    board = [[0]*N for _ in range(N)]

    col = [False]*N
    diag1 = [False]*(2*N)   # row-col+n-1
    diag2 = [False]*(2*N)   # row+col

    def solve(row):
        if row == N:
            return True

        for c in range(N):
            if not col[c] and not diag1[row-c+N-1] and not diag2[row+c]:
                board[row][c] = 1
                col[c] = diag1[row-c+N-1] = diag2[row+c] = True

                if solve(row + 1):
                    return True

                # Backtrack
                board[row][c] = 0
                col[c] = diag1[row-c+N-1] = diag2[row+c] = False

        return False

    if solve(0):
        print("\nBranch & Bound Solution:")
        for row in board:
            print(row)
    else:
        print("No solution")


# -------------------------------
# DRIVER CODE
# -------------------------------
run_backtracking()
run_branch_and_bound()