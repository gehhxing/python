import copy
import random


class Board:
    '''
    Includes initialization and print of board,
    and calculation of the next state of board
    '''
    def __init__(self, board=None, m=9, n=9):
        '''
        initialization of board
        '''
        if board:
            self.board = board
            self.m = len(board)
            self.n = len(board[0])
        else:
            self.board = [[0]*n for _ in range(m)]  # list(numpy.zeros((m, n)))
            self.m = m
            self.n = n
        self.next_board = copy.deepcopy(self.board)

    def aroundNum(self, i, j):
        '''
        calculat the number of board[i][j]'s round
        '''
        sum_j = []
        if i == 0:
            around_i = [0, 1, self.m - 1]
        elif i == self.m - 1:
            around_i = [0, self.m - 2, self.m - 1]
        else:
            around_i = [i - 1, i, i + 1]
        for k in around_i:
            if j == 0:
                sum_j.append(self.board[k][self.n - 1] + self.board[k][0] + self.board[k][1])
            elif j == self.n - 1:
                sum_j.append(self.board[k][self.n - 2] + self.board[k][self.n - 1] + self.board[k][0])
            else:
                sum_j.append(self.board[k][j - 1] + self.board[k][j] + self.board[k][j + 1])
        return sum(sum_j) - self.board[i][j]

    def nextState(self):
        '''
        calculat the next state of board
        '''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                num = self.aroundNum(i, j)
                if num in [0, 1, 4, 5, 6, 7, 8, 9]:
                    self.next_board[i][j] = 0
                if num == 3:
                    self.next_board[i][j] = 1
        self.board = copy.deepcopy(self.next_board)

    def printBoard(self):
        '''
        print board
        '''
        for i in range(len(self.board)):
            print(self.board[i])
        print('')

    def boardRandom(self):
        '''
        random cell on board
        '''
        self.board = [[1 if random.random() > 0.8 else 0 for i in range(self.n)] for j in range(self.m)]


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
    board_a = Board(m=60, n=70)
    board_a.boardRandom()
    board_a.printBoard()
    board_a.nextState()
    # board_a.nextState()
    # board_a.nextState()
    # board_a.nextState()
    board_a.printBoard()
