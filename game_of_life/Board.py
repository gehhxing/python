class Board:
    '''
    版面类
    包含版面初始化，版面元素下一个状态的计算和版面打印
    '''
    def __init__(self, board=None, m=9, n=9):
        '''
        初始化版面，以全0填充
        需补充board和m,n冲突的处理
        '''
        if board:
            self.board = board
            self.m = len(board)
            self.n = len(board[0])
        else:
            self.board.zeros((m, n))
            self.m = m
            self.n = n
        self.next_board = board

    def aroundNum(self, board, i, j):
        sum_j = []
        if i == 0:
            around_i = [0, 1, self.m - 1]
        elif i == self.m - 1:
            around_i = [0, self.m - 2, self.m - 1]
        else:
            around_i = [i - 1, i, i + 1]
        for i in around_i:
            if j == 0:
                sum_j.append(board[i][self.n - 1] + board[i][0] + board[i][1])
            elif j == self.n - 1:
                sum_j.append(board[i][self.n - 2] + board[i][self.n - 1] + board[i][0])
            else:
                sum_j.append(board[i][j - 1] + board[i][j] + board[i][j + 1])
        return sum(sum_j) - board[i][j]

    def nextState(self, board, i, j):
        print(board[i][j])
        num = self.aroundNum(board, i, j)
        if num in [0, 1, 4, 5, 6, 7, 8, 9]:
            self.next_board[i][j] = 0
        if num == 3:
            self.next_board[i][j] = 1

    def printBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.nextState(board, i, j)
        print(self.next_board)


if __name__ == '__main__':
    # board = [[0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [0, 1, 1, 1, 0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [0, 1, 1, 1, 0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [0, 0, 1, 0, 0, 0, 1, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 1, 0, 0]]
    board = [[0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    board_a = Board(board)
    board_a.printBoard(board)


[0, 1, 0, 0, 0, 1, 1, 1, 0], 
[0, 0, 1, 1, 0, 0, 0, 1, 0], 
[0, 0, 1, 1, 0, 0, 1, 1, 0], 
[0, 0, 0, 1, 0, 1, 0, 1, 0], 
[0, 0, 0, 0, 1, 0, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 1, 0, 0], 
[0, 0, 1, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 1, 0], 
[0, 0, 1, 0, 1, 0, 0, 1, 1]