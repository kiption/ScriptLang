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


def Bingocheck():
    for i in range(3):
        if (cells[i][0]["text"] == cells[i][1]["text"] == cells[i][2]["text"] == currentToken
                or cells[0][i]["text"] == cells[1][i]["text"] == cells[2][i]["text"] == currentToken):
            messagebox.showinfo("게임종료", currentToken + "가 이겼습니다.")
            quit(0)

    if (cells[0][0]["text"] == cells[1][1]["text"] == cells[2][2]["text"] == currentToken
            or cells[0][2]["text"] == cells[1][1]["text"] == cells[2][0]["text"] == currentToken):
        messagebox.showinfo("게임종료", currentToken + "가 이겼습니다.")
        quit(0)

    elif (cells[0][0]["state"] == cells[0][1]["state"] == cells[0][2]["state"]
          == cells[1][0]["state"] == cells[1][1]["state"] == cells[1][2]["state"]
          == cells[2][0]["state"] == cells[2][1]["state"] == cells[2][2]["state"] == DISABLED):
        messagebox.showinfo("게임종료", "비겼습니다.")
        quit(0)

def click(row, col):
    cells[row][col].config(text=currentToken, image=images[currentToken], state=DISABLED)
    Bingocheck()
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