import tkinter
from tkinter import *
import random

count = 0
CollectList = SecretWord = []
WrongList = []
class Hangman(Canvas):
    def __init__(self):
        window = Tk()
        window.title("Hangman")
        self.word = self.hiddenWord()
        self.SecretWord = self.word_selected_dashed()
        self.count = 0
        size = 400
        self.Print1 = False
        self.Print2 = False
        self.canvas = Canvas(window, width=size, height=size)
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.create_arc(20, 200, 100, 240, start=0, extent=180, style=tkinter.ARC)
        self.canvas.create_line(20, 220, 100, 220)
        self.canvas.create_line(60, 20, 60, 200)
        self.canvas.create_line(60, 20, 160, 20)
        self.canvas.create_line(160, 20, 160, 40)
        self.canvas.bind("<KeyPress>", self.check)  # bind all keys
        window.mainloop()

    def check(self, event):
        global SecretWord, WrongList, count

        CorrentAlpha = event.char

        if not CorrentAlpha.isalpha():
            if self.Print2:
                self.canvas.delete(self.message4)
                self.Print2 = False
            self.message4 = self.canvas.create_text(50, 300, text=" is not a letter.", font=("Arial 15", 10), anchor="w")
            self.Print2 = True
            return

        if CorrentAlpha in WrongList:
            if self.Print2:
                self.canvas.delete(self.message4)
                self.Print2 = False
            self.message4 = self.canvas.create_text(50, 300, text=" is already in missed list", font=("Arial 15", 10),
                                                    anchor="w")
            return

        if CorrentAlpha in self.word:
            for i in range(0, len(self.word)):  # Traverse list
                if self.word[i] == CorrentAlpha:
                    CollectList[i] = self.word[i]
            SecretWord = ''.join(CollectList)  # Append space
            msg1 = "Guess a word: " + SecretWord
            msg2 = "Missed letters: " + str(WrongList)
        else:
            WrongList.append(CorrentAlpha)
            self.count += 1
            if self.count < 7:
                msg1 = "Guess a word: " + str(SecretWord)
                msg2 = "Missed letter: " + str(WrongList)
                print("msg1", msg1)
                print("msg2", msg2)
            else:
                msg1 = "Sorry! The word is: " + str(self.word)
                msg2 = "To continue the game, press ENTER"
                print("msg1", msg1)
                print("msg2", msg2)

        if '*' not in SecretWord:
            msg1 = "Congrats! The word is: " + str(self.word)
            msg2 = "To continue the game, press ENTER"
            print("msg1", msg1)
            print("msg2", msg2)

        self.draw(SecretWord, msg1, msg2)

    def hiddenWord(self):
        word_file = open('hangman.txt', 'r+')
        secret_word = random.choice(word_file.read().split())
        word_file.close()
        print(secret_word)
        return secret_word


    def word_selected_dashed(self):
        secret_word = self.word
        for i in range(len(secret_word)):
            SecretWord.append('*')
        return SecretWord


    def draw(self, SecretWord, msg1, msg2):
        global count
        # head
        if self.count >= 1:
            self.canvas.create_oval(140, 40, 180, 80)
        # arm left
        if self.count >= 2:
            self.canvas.create_line(150, 77, 100, 120)
        # arm Right
        if self.count >= 3:
            self.canvas.create_line(170, 77, 220, 120)
        # body
        if self.count >= 4:
            self.canvas.create_line(160, 80, 160, 140)
        # leg left
        if self.count >= 5:
            self.canvas.create_line(160, 140, 110, 190)
        # leg Right
        if self.count >= 6:
            self.canvas.create_line(160, 140, 210, 190)
        if self.count >= 7:
            self.message2 = self.canvas.create_text(50, 270, text=msg1, font=("Arial 15", 10), anchor="w")

        if not self.Print1:
            self.message1 = self.canvas.create_text(130, 250, text=SecretWord, font="Arial 15", anchor="w")
            self.message3 = self.canvas.create_text(50, 280, text=msg2, font=("Arial 15", 10), anchor="w")
            self.Print1 = True
        else:
            self.canvas.delete(self.message1)
            self.canvas.delete(self.message3)
            self.message1 = self.canvas.create_text(130, 250, text=SecretWord, font="Arial 15", anchor="w")
            self.message3 = self.canvas.create_text(50, 280, text=msg2, font=("Arial 15", 10), anchor="w")



Hangman()
