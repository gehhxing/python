m = 4
n = 4
board = [[0, 0, 1, 0],
         [0, 1, 1, 1],
         [0, 0, 1, 0],
         [0, 0, 0, 0]]

next_board = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]


def aroundNum(board, i, j):
    sum_j = []
    if i == 0:
        around_i = [0, 1, m - 1]
    elif i == m - 1:
        around_i = [0, m - 2, m - 1]
    else:
        around_i = [i - 1, i, i + 1]
    for i in around_i:
        if j == 0:
            sum_j.append(board[i][n - 1] + board[i][0] + board[i][1])
        elif j == n - 1:
            sum_j.append(board[i][n - 2] + board[i][n - 1] + board[i][0])
        else:
            sum_j.append(board[i][j - 1] + board[i][j] + board[i][j + 1])
    return sum(sum_j) - board[i][j]


def caluNext(board, i, j):
    print(board[i][j])
    num = aroundNum(board, i, j)
    if num in [0, 1, 4, 5, 6, 7, 8, 9]:
        next_board[i][j] = 0
    if num == 3:
        next_board[i][j] = 1

if __name__ == '__main__':
    for i in range(m):
        for j in range(n):
            caluNext(board, i, j)
    print(next_board)
