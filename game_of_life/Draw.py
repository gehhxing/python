import tkinter as tk
import Board
import threading

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
        self.root = tk.Tk()
        self.root.geometry('700x700')  # 界面大小700x700
        # 在界面中画出一个700*600的画布，画布颜色黑色
        self.cv = tk.Canvas(self.root, bg='black', width=700, height=600)
        self.cv.pack()
        self.button_auto = tk.Button(self.root, text='AutoPlay', command=self.startLoop)
        self.button_auto.pack(side=tk.LEFT)
        self.button_stop = tk.Button(self.root, text='StopPlay', command=self.stopLoop)
        self.button_stop.pack(side=tk.LEFT)
        self.button_next = tk.Button(self.root, text='Next', command=self.nextBoard)
        self.button_next.pack(side=tk.LEFT)
        self.button_clr = tk.Button(self.root, text='Clear', command=self.clearBoard)
        self.button_clr.pack(side=tk.LEFT)
        self.button_random = tk.Button(self.root, text='Random', command=self.boardRandom)
        self.button_random.pack(side=tk.LEFT)
        self.board_a = Board.Board(m=60, n=70)
        # self.timer = threading.Timer(0.2, self.autoLoop)
        self.LOOP_SWITCH = False

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

    def nextBoardEvent(self, event):
        '''
        enent trigger
        '''
        self.board_a.nextState()
        self.printScreen()

    def nextBoard(self):
        '''
        click 'Next' button to trigger nextBoard(), then display the next screen
        '''
        self.board_a.nextState()
        self.printScreen()

    def boardRandom(self):
        '''
        random cell on board
        '''
        self.board_a.boardRandom()
        self.printScreen()

    def clickLeft(self):
        '''
        click left mouse button to trigger nextBoardEvent()
        '''
        self.cv.bind_all('<Button-1>', self.nextBoardEvent)
        self.cv.pack()

    def autoLoop(self):
        '''
        click 'AutoPlay' button to trigger autoLoop(), then auto-refresh screen
        '''
        self.board_a.nextState()
        self.printScreen()
        self.cv.pack()
        # self.timer.cancel()
        if self.LOOP_SWITCH:
            self.timer = threading.Timer(0.5, self.autoLoop)
            self.timer.start()

    def startLoop(self):
        '''
        click 'AutoPlay' button to trigger startLoop(), then run autoLoop()
        '''
        self.LOOP_SWITCH = True
        self.autoLoop()

    def stopLoop(self):
        '''
        click 'StopPlay' button to trigger stopLoop(), then stop auto-refresh screen
        '''
        self.LOOP_SWITCH = False

    def clearBoard(self):
        '''
        click 'Clear' button to trigger clearBoard(), then clear next screen
        '''
        self.board_a.clearBoard()
        self.printScreen()

    def a(self):
        pass

    def start(self):
        '''
        start draw the cell
        '''
        self.printScreen()
        self.boardRandom()
        # self.autoLoop()
        # self.clickLeft()
        self.root.mainloop()


if __name__ == '__main__':
    Draw().start()


# root = tk.Tk()
# # 创建一个Canvas，设置其背景色为白色
# cv = tk.Canvas(root,bg = 'white')
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
