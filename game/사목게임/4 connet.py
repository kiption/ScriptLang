import tkinter
from canvas4 import ConnectFour
from tkinter import *

class Game(object):
    def __init__(self, root):
        self.game_pieces = []
        self.root = root
        self.column_width = 100
        self.row_height = 100
        self.connectFourObj = ConnectFour()
        self.init_window()
        self.init_grid(self.game_canvas, self.column_width, self.row_height)
        self.init_Start_game_window()
        self.get_mouse_x_coord()

    def init_window(self):
        self.root.title('Connect 4 Game')
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.columnconfigure(6, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.canvas_width = 700
        self.canvas_height = 600
        self.game_canvas = Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, background='#e6e6e6')
        self.game_canvas.grid(column=0, row=0)

    def init_grid(self, canvas, column_width, row_height):
        for x in range(column_width, self.canvas_width, column_width):
            canvas.create_line(x, 0, x, self.canvas_height,
                               fill='#1d66db', width=2,)

        for y in range(row_height, self.canvas_width-100, row_height):
            canvas.create_line(0, y, self.canvas_width,
                               y, fill='#1d66db', width=2)

    def draw_circle(self, color, start_coords, end_coords):
        self.game_pieces.append(self.game_canvas.create_oval(
            start_coords[0]+10, start_coords[1]+10, end_coords[0]-10, end_coords[1]-10, fill=color))

    def get_mouse_x_coord(self):
        self.game_canvas.bind(
            '<Button-1>', lambda e: self.where_to_draw(e.x))

    def where_to_draw(self, x_coord):
        column = x_coord//self.column_width
        row = self.connectFourObj.next_spot(column)

        if row != None:
            x1, y1 = column*self.column_width, row*self.row_height
            x2, y2 = (column*self.column_width) + \
                self.column_width, (row*self.row_height)+self.row_height

            if self.connectFourObj.get_current_player() == 1:
                self.draw_circle('red', (x1, y1), (x2, y2))
                if self.connectFourObj.get_game_status():
                    return self.init_game_over_window()
                self.connectFourObj.switch_player()
            else:
                self.draw_circle('blue', (x1, y1), (x2, y2))
                if self.connectFourObj.get_game_status():
                    return self.init_game_over_window()
                self.connectFourObj.switch_player()

        else:
            pass

    def reset_board(self):
        for piece in self.game_pieces:
            self.game_canvas.delete(piece)
        self.game_pieces = []

    def init_Start_game_window(self):
        self.start_window_canvas = Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, background='#a7e6e8')
        self.start_window_canvas.grid(
            column=0, row=0,  columnspan=7, rowspan=6, sticky=(N, S, E, W))

        Label(self.start_window_canvas,
              text='Click To Start Game', font=('Helvetica', 30), background='#a7e6e8').place(relx=0.5, rely=0.4, anchor=CENTER)

        Label(self.start_window_canvas,
              text='Player1:', font=('Helvetica', 30), background='#a7e6e8').place(relx=0.5, rely=0.4, anchor=CENTER, y=70, x=-50)
        Label(self.start_window_canvas,
              text='Red', font=('Helvetica', 30), background='#a7e6e8', fg='red').place(relx=0.55, rely=0.4, anchor=CENTER, y=70, x=50)

        Label(self.start_window_canvas,
              text='Player2:', font=('Helvetica', 30), background='#a7e6e8').place(relx=0.5, rely=0.4, anchor=CENTER, y=125, x=-50)

        Label(self.start_window_canvas,
              text='Blue', font=('Helvetica', 30), background='#a7e6e8', fg='blue').place(relx=0.55, rely=0.4, anchor=CENTER, y=125, x=50)

        tkinter.Misc.lift(self.start_window_canvas)

        self.start_window_canvas.bind(
            '<Button-1>', lambda e: tkinter.Misc.lift(self.game_canvas))

    def init_game_over_window(self):
        if self.connectFourObj.get_game_status:
            self.reset_board()

            self.game_over_canvas = Canvas(
                self.root, width=self.canvas_width, height=self.canvas_height, background='#a7e6e8')
            self.game_over_canvas.grid(
                column=0, row=0,  columnspan=7, rowspan=6, sticky=(N, S, E, W))
            if self.connectFourObj.winner == 0:
                Label(self.game_over_canvas,
                      text="It's A Tie", font=('Helvetica', 50), background='#a7e6e8', fg='brown').place(relx=0.5, rely=0.4, anchor=CENTER)
            else:
                Label(self.game_over_canvas,
                      text='Winner Is:', font=('Helvetica', 30), background='#a7e6e8').place(relx=0.45, rely=0.4, anchor=CENTER, y=70, x=-50)
                if self.connectFourObj.winner == 1:
                    Label(self.game_over_canvas,
                          text='Player 1', font=('Helvetica', 30), background='#a7e6e8', fg='red').place(relx=0.55, rely=0.4, anchor=CENTER, y=70, x=50)
                elif self.connectFourObj.winner == 2:
                    Label(self.game_over_canvas,
                          text='Player 2', font=('Helvetica', 30), background='#a7e6e8', fg='blue').place(relx=0.55, rely=0.4, anchor=CENTER, y=70, x=50)

            tkinter.Misc.lift(self.game_over_canvas)

            self.game_over_canvas.bind(
                '<Button-1>', lambda e: tkinter.Misc.lift(self.start_window_canvas))
            self.connectFourObj.reset_game()



root = Tk()
Game(root)
root.mainloop()