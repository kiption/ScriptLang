from tkinter import *
from tkinter import messagebox
import random as r

root = Tk()
root.title("Tic-Tac-Toe")
x = r.choice(['O', 'X'])
color = {'O': "red", 'X': "blue"}
y = [[], [], []]