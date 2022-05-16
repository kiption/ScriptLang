from tkinter import *
DIAMETER = 75
FOOTER = 25

initialColor = "white"
class Board(Canvas):
    def __init__(self, col, row, window):
        self.row = row
        self.col = col
        self.data = []
        self.turn = True
        for r in range(self.row):
            boardRow = []
            for c in range(self.col):
                boardRow += [' ']
            self.data += [boardRow]

        self.gameOver = False
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        height = (DIAMETER * row) + 50
        self.draw = Canvas(window, width=((DIAMETER) * col), height=((DIAMETER) * row) + 50, bg="gray",
                           highlightbackground="black", highlightthickness=5)

        self.draw.bind("<Button-1>", self.mouse)
        self.draw.pack()

        self.qButton = Button(self.frame, text="QUIT", fg="red", command=self.quitGame)
        self.qButton.pack(side=RIGHT)
        self.cButton = Button(self.frame, text="NEW GAME", fg="black", command=self.clear)
        self.cButton.pack(side=RIGHT)

        self.circles = []
        self.colors = []

        y = 0
        for r in range(row):
            x = 0
            circleRow = []
            colorRow = []
            for c in range(col):
                circleRow += [self.draw.create_oval(x + 5, y + 5, x + DIAMETER, y + DIAMETER, fill=initialColor)]
                colorRow += [initialColor]
                x += DIAMETER
            self.circles += [circleRow]
            self.colors += [colorRow]
            y += DIAMETER

        # text
        self.message = self.draw.create_text(FOOTER, height - FOOTER, text="CONNECT FOUR GAME: Choose Your Move!",
                                             font="Arial 15", anchor="w")

    def quitGame(self):
        self.window.destroy()

    def mouse(self, event):
        if self.gameOver:
            return
        if self.turn:
            text = 'X'
        else:
            text = 'O'
        x = int(event.x / DIAMETER)
        y = self.addMove(x, text)

        if self.turn:
            self.draw.itemconfig(self.circles[y][x], fill="red")
            myMessage = "Player Red - Choose Your Next Move!"
            self.draw.itemconfig(self.message, text=myMessage)  # Modifies the previous message to new message
            self.turn = False

        else:
            self.draw.itemconfig(self.circles[y][x], fill="blue")
            myMessage = "Player Blue - Choose Your Next Move!"
            self.draw.itemconfig(self.message, text=myMessage)  # Modifies the previous message to new message
            self.turn = True

        if self.Check('X'):
            myMessage = "Red Player won!"
            self.draw.itemconfig(self.message, text=myMessage)
            self.gameOver = True
            return

        if self.Check('O'):
            myMessage = "Blue Player won"
            self.draw.itemconfig(self.message, text=myMessage)
            self.gameOver = True

            # game fill
        if self.isFull():
            myMessage = "Game was a tie!!!"
            self.draw.itemconfig(self.message, text=myMessage)
            self.gameOver = True
            return

    def addMove(self, j, text):
        if self.allowsMove(j):
            for i in range(self.row):
                if self.data[i][j] != ' ':
                    self.data[i - 1][j] = text
                    return i - 1
            self.data[self.row - 1][j] = text
            return self.row - 1

    def allowsMove(self, col):
        if 0 <= col < self.col:
            return self.data[0][col] == ' '
        else:
            return False

    def clear(self):
        self.gameOver = False

        for i in range(self.row):
            for j in range(self.col):
                self.data[i][j] = ' '
        self.circles = []
        self.colors = []
        # creating our GUI board

        y = 0
        for i in range(self.row):
            x = 0
            circleRow = []
            colorRow = []
            for j in range(self.col):
                circleRow += [self.draw.create_oval(x + 5, y + 5, x + DIAMETER, y + DIAMETER, fill=initialColor)]
                colorRow += [initialColor]
                x += DIAMETER
            self.circles += [circleRow]
            self.colors += [colorRow]
            y += DIAMETER

        myMessage = "CONNECT FOUR GAME: Choose your move!!"
        self.draw.itemconfig(self.message, text=myMessage)

    def delMove(self, j):
        for i in range(self.row):
            if self.data[i][j] != ' ':
                self.data[i][j] = ' '
                return

    def isFull(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.data[i][j] == ' ':
                    return False
        else:
            return True

    def Check(self, text):
        # checks horizontal
        for i in range(0, self.row):
            for j in range(0, self.col - 3):
                if self.data[i][j] == text and self.data[i][j + 1] == text and \
                        self.data[i][j + 2] == text and self.data[i][j + 3] == text:
                    return True

        # checks vertical
        for i in range(0, self.row - 3):
            for j in range(0, self.col):
                if self.data[i][j] == text and self.data[i + 1][j] == text and \
                        self.data[i + 2][j] == text and self.data[i + 3][j] == text:
                    return True

        # checks diagonal T2B
        for i in range(0, self.row - 3):
            for j in range(0, self.col - 3):
                if self.data[i][j] == text and self.data[i + 1][j + 1] == text and \
                        self.data[i + 2][j + 2] == text and self.data[i + 3][j + 3] == text:
                    return True
        # checks diagonal B2T
        for i in range(3, self.row):
            for j in range(0, self.col - 3):
                if self.data[i][j] == text and self.data[i - 1][j + 1] == text and \
                        self.data[i - 2][j + 2] == text and self.data[i - 3][j + 3] == text:
                    return True

root = Tk()
root.title("Connect 4")
b = Board(7, 6, root)
root.mainloop()