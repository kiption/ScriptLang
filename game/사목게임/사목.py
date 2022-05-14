from tkinter import*

class Cell:
    def __init__(self):
        window = Tk()
        window.title("Samok-Game")
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='game_sub/x.gif')
        self.imageO = PhotoImage(file='game_sub/o.gif')
        self.imageE = PhotoImage(file='game_sub/empty.gif')
        self.turn = True
        self.done = False
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, image=self.imageE,
                                          text=' ', command=lambda col=j: self.pressed(col)))
                self.matrix[i][j].grid(row=i, column=j)
        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("Player X turn")
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='retry', command=self.refresh).pack(side=LEFT)
        window.mainloop()

    def findRow(self, col):
        for row in range(5, -1, -1):  # row: 5->0
            if self.matrix[row][col]['text'] == ' ':
                return row
        return 6

    def pressed(self, col):
        row = self.findRow(col)
        if not self.done and self.matrix[row][col]['text']==' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] ='B'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'W'
            self.turn = not self.turn
            if self.check()!= '':
                self.done = True
                self.explain.set('Player'+self.check()+'win')
            elif self.turn:
                self.explain.set('Player B turn')
            else:
                self.explain.set('Player W turn')

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set("Player B turn")
        self.turn = True

    def check(self):
        #row Check
        for i in range(6):
            for j in range(4):  # 4개 판별.
                Player = self.matrix[i][j]['text']
                if Player != ' ' and Player == self.matrix[i][j + 1]['text'] \
                        and Player == self.matrix[i][j + 2]['text'] and Player == self.matrix[i][j + 3]['text']:
                    return Player

        # col Check
        for i in range(3):
            for j in range(7):
                Player = self.matrix[i][j]['text']
                if Player != ' ' and Player == self.matrix[i + 1][j]['text'] \
                        and Player == self.matrix[i + 2][j]['text'] and Player == self.matrix[i + 3][j]['text']:
                    return Player

            # cross Check (left->right)
        for i in range(3):
            for j in range(4):  # col 0~3
                Player = self.matrix[i][j]['text']
                if Player != ' ' and Player == self.matrix[i + 1][j + 1]['text'] \
                        and Player == self.matrix[i + 2][j + 2]['text'] and Player == self.matrix[i + 3][j + 3]['text']:
                    print("대각선 좌에서 우", i, j)
                    return Player

            # cross Check (right->left)
        for i in range(3):
            for j in range(3, 7):  # col 3~6
                Player = self.matrix[i][j]['text']
                if Player != ' ' and Player == self.matrix[i + 1][j - 1]['text'] \
                        and Player == self.matrix[i + 2][j - 2]['text'] and Player == self.matrix[i + 3][j - 3]['text']:
                    print("대각선 좌에서 우", i, j)
                    return Player
        return ''

Cell()