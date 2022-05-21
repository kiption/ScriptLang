import math
from tkinter import * # Import tkinter
import random
import re

# Initialize words, get the words from a file
infile = open("hangman.txt", "r")

words = infile.read().split()

class Hangman:

    def __init__(self):
        self.hiddenWord = random.choice(words)    # 파일에서 읽은 것 중 임의로 선택한 단어
        self.guessWord = ["*" for i in range(len(self.hiddenWord))]   # ‘***’로 시작하여 사용자가 맞추는 것에 따라 내용 변경.
                                    # Str 타입을 immutable 이므로 문자의 리스트 사용
        self.nCorrectChar = 0   # 맞춘 알파벳 개수
        self.nMissChar = 0  # 틀린 알파벳 개수
        self.nMissedLetters = []    # 틀린 알파벳의 리스트
        self.finished = 0   # 0 = not finished, 1 = correct, 2 = wrong
        self.draw()

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger

        radius = 20 # 반지름

        if self.nMissChar > 0:
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

            # Draw the circle
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        if self.nMissChar > 1:
            # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 - radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 - (radius+60) * math.cos(math.radians(45))
            y2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.nMissChar > 2:
            # Draw the right arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 + radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 + (radius + 60) * math.cos(math.radians(45))
            y2 = 60 + (radius + 60) * math.sin(math.radians(45))

            # Draw the line
            canvas.create_line(x1, y1, x2, y2, tags="hangman")

        if self.nMissChar > 3:
            canvas.create_oval(160, 80, 160, 140, tags="hangman")

        if self.nMissChar > 4:
            # Draw the left leg (중심(160,140)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x2 = 160 - (radius + 40) * math.cos(math.radians(45))
            y2 = 140 + (radius + 40) * math.sin(math.radians(45))

            canvas.create_line(160, 140, x2, y2, tags="hangman")

        if self.nMissChar > 5:

            # Draw the right leg (중심(160,140)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x2 = 160 + (radius + 40) * math.cos(math.radians(45))
            y2 = 140 + (radius + 40) * math.sin(math.radians(45))

            canvas.create_line(160, 140, x2, y2, tags="hangman")

        MissCount = "틀린횟수: " + str(self.nMissChar)
        canvas.create_text(350,100,text = MissCount,tags="text")
        CorrectCount = "맞춘 알파벳 수: " + str(self.nCorrectChar)
        canvas.create_text(350, 120, text=CorrectCount, tags="text")

        if self.finished == 1:
            canvas.delete("text")
            canvas.create_text(200, 220, text=self.hiddenWord, tags="text")
            canvas.create_text(200, 200, text="맞았습니다. 게임을 계속하려면 ENTER을 누르세요", tags="text")

        if self.finished == 2:
            canvas.delete("text")
            answer = "정답은 " + ''.join(self.hiddenWord) + "입니다."
            canvas.create_text(200, 220, text=answer, tags="text")
            canvas.create_text(200, 200, text="틀렸습니다. ENTER을 눌러서 다시 시작하세요", tags="text")




    def setWord(self):

        canvas.delete("text")

        self.hiddenWord = random.choice(words)
        self.guessWord = ["*" for i in range(len(self.hiddenWord))]
        self.nCorrectChar = 0
        self.nMissChar = 0
        self.nMissedLetters = []
        self.finished = 0
        self.draw()

    def guess(self, letter):
        if self.finished == 0:
            if letter not in self.guessWord:
                for c in range(0, len(self.hiddenWord)):
                    if self.hiddenWord[c] == letter:
                        self.guessWord[c] = letter
                        self.nCorrectChar += 1

                if letter not in self.hiddenWord:
                    if letter not in self.nMissedLetters:
                        self.nMissChar += 1
                        self.nMissedLetters.append(letter)

            if self.nMissChar > 6:
                self.finished = 2

            if self.hiddenWord == ''.join(self.guessWord):
                self.finished = 1

        canvas.delete("text")

        hdword = "단어 추측: " + ''.join(self.guessWord)
        hwd = canvas.create_text(200, 200, text=hdword, tags="text")
        wrongletters = "틀린 글자: " + ','.join(self.nMissedLetters)

        canvas.create_text(200, 240, text=wrongletters, tags="text")

        self.draw()







window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    key = event.keysym

    if 'a' <= event.char and event.char <= 'z':
        hangman.guess(key)

    elif event.keycode == 13:
        hangman.setWord()


width = 400
height = 280

# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg="white", width=width, height=height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop