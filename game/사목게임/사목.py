from tkinter import*
class Cell(Canvas):
    def __init(self, parent, row, col, width=20, height=20):
        Canvas.__init__(self, parent, width=width, height=height, bg="blue", borderwidth=2)
        self.color = "white"
        self.row = row
        self.col = col

        self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")
        self.bind("<Button-1>",self.clicked)

    def clicked(self, event):
        nextcolor = "red" if self.color != "red" else "yellow"
        self.setColor(nextcolor)

    def setColor(self,color):
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")

window = Tk()
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()

cell = Cell(frame1, width=20, height=20)
cell.grid(row=0, column=0)

window.mainloop()   # Create an event loop