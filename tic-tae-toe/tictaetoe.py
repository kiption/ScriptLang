from tkinter import *
from tkinter import messagebox
import random

# Global constants
currentToken = random.choice(['O', 'X'])
cells = [[], [], []]

def button(frame):
    cells = Button(frame, bg="pink", image=images[''], relief="groove", padx=100, pady=100,
                   width=100, height=100, bd=20)
    return cells

def TokenChange():
    global currentToken
    for i in ['O', 'X']:
        if not(i == currentToken):
            currentToken = i
            break




def click(row, col):
    cells[row][col].config(text=currentToken, image=images[currentToken], state=DISABLED)

    TokenChange()
    label.config(text=currentToken + "- 차례")


window = Tk()
window.title("TicTacToe")

images = {'': PhotoImage(file="empty.gif"), 'X': PhotoImage(file="x.gif"), 'O': PhotoImage(file="o.gif")}
for i in range(3):
        for j in range(3):
                cells[i].append(button(window))
                cells[i][j].config(command=lambda row=i, col=j: click(row, col))
                cells[i][j].grid(row=i, column=j)

label = Label(text="Tic-Tac-Toe", font=('arial', 20, 'italic'))
label.grid(row=3, column=0, columnspan=3)

window.mainloop()