from tkinter import*

matrix = []
def drawBoard():
    for i in range(6):
        for j in range(7):
            print('ㅣ',matrix[i][j],' ',end='')
        print('ㅣ')
    print("--------------------------")

def check():
    for i in range(6):
        for j in range(7):

def findRow(col):
    for row in range(5, -1, -1): # row: 5->0
        if matrix[row][col] == ' ':
            return row
    return 6

def main():
    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append(' ')

    drawBoard()
    turn = True
    while(True):
        if turn:
            col = eval(input("열 0~6사이 하얀돌을 입력하세요: "))

        else:
            col = eval(input("열 0~6사이 겅은돌을 입력하세요: "))

        row = findRow(col) # 들어갈 행 구하기
        if turn:
            matrix[row][col] = 'W'
        else:
            matrix[row][col] = 'B'
        drawBoard()
        Player = check()
        if Player !='':
            print("플레이어", Player, "가 이겼습니다")
            break
        turn = not turn

main()