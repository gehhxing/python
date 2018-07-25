import tkinter
# import time
import Board

board_init = [[0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]


class Draw:
    '''
    Includes draw board,
    and calculation of the next state of board
    '''

    def __init__(self):
        '''
        initialization of interface
        '''
        self.root = tkinter.Tk()
        self.root.geometry('700x700')  # 界面大小700x700
        # 在界面中画出一个700*600的画布，画布颜色黑色
        self.cv = tkinter.Canvas(self.root, bg='black', width=700, height=600)
        self.cv.pack()
        self.board_a = Board.Board(m=60, n=70)

        # self.cv.update_idletasks()

    def printScreen(self):
        '''
        print cell on screen
        '''
        self.cv.delete('cell')
        for i in range(len(self.board_a.board)):
            for j in range(len(self.board_a.board[0])):
                tag_pos = '{}_{}'.format(i, j)
                if self.board_a.board[i][j] == 1:
                    self.cv.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill='blue', tags=('cell', tag_pos))
        self.cv.pack()

    def nextBoard(self, event):
        '''
        enent trigger
        '''
        self.board_a.nextState()
        self.printScreen()

    def boardRandom(self):
        '''
        random cell on board
        '''
        self.board_a.boardRandom()

    def clickNext(self):
        '''
        click left button to trigger nextBoard()
        '''
        self.cv.bind_all('<Button-1>', self.nextBoard)
        self.cv.pack()
        self.root.mainloop()

    def start(self):
        '''
        start draw the cell
        '''
        self.printScreen()
        self.boardRandom()
        self.clickNext()


if __name__ == '__main__':
    Draw().start()


# root = tkinter.Tk()
# # 创建一个Canvas，设置其背景色为白色
# cv = tkinter.Canvas(root,bg = 'white')
# # 创建三个rectangle
# rt1 = cv.create_rectangle(
#     10,10,110,110,
#     width = 8,
#     tags = ('r1','r2','r3'))
# def printRect(event):
#     print('rectangle')
# # 绑定item与事件，单击
# cv.tag_bind('r2','<Button-1>',printRect)
# cv.pack()
# root.mainloop()
