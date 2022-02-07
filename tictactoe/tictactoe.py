import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-','-','-'], ['-','-','-'], ['-','-','-']]

    def print_instructions(self):
        print("Welcome to TicTacToe")
        print("Player 1 is X and Player 2 is 0")
        print("Take turns placing your pieces - the first to 2 in a row wins!")
        return

    def print_board(self):
        print("\t0\t1\t2")
        for r in range(len(self.board)):
            printB = str(r)
            for c in range(len(self.board[r])):
                printB = printB + "\t" + str(self.board[r][c])
            print(printB)
        return

    def is_valid_move(self, row, col):
        if row <= len(self.board) - 1 and col <= len(self.board[:]) - 1 and self.board[row][col] == '-':
            return True
        else:
            return False

    def place_player(self, player, row, col):
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        row = input("Enter a row: ")
        col = input("Enter a col: ")
        while self.is_valid_move(int(row),int(col)) == False:
            print("Please enter a valid move.")
            row = input("Enter a row: ")
            col = input("Enter a col: ")
        self.place_player(player, int(row), int(col))
        return

    def take_turn(self, player):
            if player == "X":
                print("It is player one's turn")
                self.take_manual_turn(player)
            else:
                print("It is player two's turn")
                self.take_random_turn(player)

    def check_col_win(self, player):

       for col in range(len(self.board[:])):
            columList = []
            for row in range(len(self.board)):
                columList.append(self.board[row][col])
            if columList == [player,player,player]:
                return True
       return False

    def check_row_win(self, player):
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board[:])):
                rowList.append(self.board[row][col])
            if rowList == [player, player, player]:
                return True
        return False

    def check_diag_win(self, player):
        playerList = [player, player, player]
        if [self.board[0][0],self.board[1][1], self.board[2][2]] == playerList:
            return True
        elif [self.board[2][0],self.board[1][1], self.board[0][2]] == playerList:
            return True
        return False

    def check_win(self, player):
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        if any("-" in sublist for sublist in self.board):
            return False
        return True

    def change_player(self, player):
        if player == "X":
            return "0"
        else:
            return "X"

    def take_random_turn(self, player):
        row = random.randint(0,2)
        col = random.randint(0,2)
        while self.is_valid_move(int(row), int(col)) == False:
            row = random.randint(0, 2)
            col = random.randint(0,2)
        self.place_player(player, int(row), int(col))
        return


    def play_game(self):
        player = "0"
        gameRun = True
        while gameRun:
            player = self.change_player(player)
            self.take_turn(player)
            self.print_board()
            if self.check_win(player):
                print(player + " Wins!")
                gameRun = False
            elif self.check_tie():
                print("Tie")
                gameRun = False
        return

