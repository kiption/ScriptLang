class ConnectFour(object):
    def __init__(self):
        self.game_over = False
        self.current_player = 1
        self.player1_moves = 0
        self.player2_moves = 0
        self.winner = 0
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

    def next_spot(self, x_coord):
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][x_coord] == 0:
                self.board[row][x_coord] = self.current_player
                self.increase_player_moves()
                if self.player1_moves >= 4 or self.player2_moves >= 4:
                    self.check_winner()
                return row

        return None

    def increase_player_moves(self):
        if self.current_player == 1:
            self.player1_moves += 1
        else:
            self.player2_moves += 1

    def check_winner(self):
        if self.match_H() != None:
            print('Winner is: Player ' + str(self.winner))
            self.game_over = True
        elif self.match_v() != None:
            print('Winner is: Player ' + str(self.winner))
            self.game_over = True
        elif self.match_diagonal() != None:
            print('Winner is: Player ' + str(self.winner))
            self.game_over = True
        elif self.checkTie() != None:
            self.game_over = True

    def match_H(self):
        for row in range(len(self.board)-1, -1, -1):
            if self.is_empty_row(row):
                break
            else:
                pointer1 = 0
                pointer2 = 1
                counter = 1

                while pointer1 < len(self.board[row]) and pointer2 < len(self.board[row]):
                    if self.board[row][pointer1] == self.board[row][pointer2] and self.board[row][pointer1] != 0:
                        pointer2 += 1
                        counter += 1
                    else:
                        pointer1 = pointer2
                        pointer2 += 1
                        counter = 1

                    if counter == 4:
                        self.winner = self.board[row][pointer1]
                        return self.board[row][pointer1]

        return None

    def match_v(self):
        for col in range(len(self.board[0])):
            temp_list = []
            for row in range(len(self.board)-1, -1, -1):
                temp_list.append(self.board[row][col])

            if self.check_row_match(temp_list) != None:
                return self.winner

        return None

    def match_diagonal(self):
        rows = len(self.board)
        columns = len(self.board[0])
        for d in range(rows+columns-1):
            temp_row = []
            for x in range(max(0, d-columns+1), min(rows, d+1)):
                temp_row.insert(0, self.board[x][d-x])

            if len(temp_row) >= 4:
                if self.check_row_match(temp_row) != None:
                    return self.winner

        for d in range(rows+columns-1):
            temp_row = []
            for x in range(min(rows-1, d), max(-1, d-columns), -1):
                temp_row.append(self.board[x][x-d-1])

            if len(temp_row) >= 4:
                if self.check_row_match(temp_row) != None:
                    return self.winner

    def check_row_match(self, row):
        if not self.is_empty_row_v(row):
            pointer1 = 0
            pointer2 = 1
            counter = 1

            while pointer1 < len(row) and pointer2 < len(row):
                if row[pointer1] == row[pointer2] and row[pointer1] != 0:
                    pointer2 += 1
                    counter += 1
                else:
                    pointer1 = pointer2
                    pointer2 += 1
                    counter = 1

                if counter == 4:
                    self.winner = row[pointer1]
                    return row[pointer1]
        return None

    def is_empty_row(self, row):
        return self.board[row].count(0) > 3

    def is_empty_row_v(self, row):
        return row.count(0) > 3

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def get_current_player(self):
        return self.current_player

    def get_game_status(self):
        return self.game_over

    def reset_game(self):
        self.game_over = False
        self.current_player = 1
        self.player1_moves = 0
        self.player2_moves = 0
        self.winner = 0
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

    def checkTie(self):
        if (self.player1_moves + self.player2_moves) == (len(self.board) * len(self.board[0])):
            self.winner = 0
            return self.winner

        return None