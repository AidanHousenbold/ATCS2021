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
            self.take_manual_turn(player)
            if player == "X":
                player = "0"
            else:
                player = "X"


    def check_col_win(self, player):

       # for col in range(len(self.board[:])):
         #   for row in range(len(self.board)):

       return False

    def check_row_win(self, player):
        # TODO: Check row win
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        return False

    def check_win(self, player):
        # TODO: Check win
        return False

    def check_tie(self):
        # TODO: Check tie
        return False

    def play_game(self):
        # TODO: Play game
        return

