import random
import time

class TicTacToe:
    def __init__(self):
        #self.board = [['-','-','-'], ['-','-','-'], ['-','-','-']]
        self.board = [['X', '0', 'X'], ['0','0', 'X'], ['-','X', '-']]

    def print_instructions(self):
        print("Welcome to TicTacToe")
        print("Player 1 is X and Player 2 is 0")
        print("Take turns placing your pieces - the first to 3 in a row wins!")
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
                self.take_minimax_alpha_beta_turn(player)

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
        if self.check_win("X"):
            return False
        elif self.check_win("0"):
            return False
        elif any("-" in sublist for sublist in self.board):
            return False
        else:
            return True

    def change_player(self, player):
        if player == "X":
            return "0"
        else:
            return "X"
    def take_minimax_turn(self, player):
        depth = 100
        start = time.time()
        score,row,col = self.minimax(player, depth)
        end = time.time()
        self.place_player(player, row, col)
        print("This turn took: ", end-start, "seconds")

    def take_random_turn(self, player):
        row = random.randint(0,2)
        col = random.randint(0,2)
        while self.is_valid_move(int(row), int(col)) == False:
            row = random.randint(0, 2)
            col = random.randint(0,2)
        self.place_player(player, int(row), int(col))
        return

    def get_possible_moves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[:])):
                if self.board[row][col] == "-":
                    moves.append([row,col])
        return moves

    def take_minimax_alpha_beta_turn(self, player):
        depth = 15
        alpha = -100
        beta = 100
        score,row,col = self.minimax_alpha_beta(player, depth, alpha, beta)
        self.place_player(player, row, col)

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        if self.check_tie() or depth == 0:
            return (0, None, None)

        opt_row = -1
        opt_col = -1
        if player == "0":
            if self.check_win(player):
                return (10, None, None)
            best = -1000000
            for move in self.get_possible_moves():
                self.place_player("0", move[0], move[1])
                score = self.minimax_alpha_beta("X", depth - 1, alpha, beta)[0]
                self.place_player("-", move[0], move[1])
                if best < score:
                    best = score
                    opt_row = move[0]
                    opt_col = move[1]
                alpha = max(alpha, score)
                if alpha >= beta:
                    return (best, opt_row, opt_col)
            return (best, opt_row, opt_col)

        if player == "X":
            if self.check_win(player):
                return (-10, None, None)
            worst = 100000
            for move in self.get_possible_moves():
                self.place_player("X", move[0], move[1])
                score = self.minimax_alpha_beta("0", depth - 1, alpha, beta)[0]
                self.place_player("-", move[0], move[1])
                if worst > score:
                    worst = score
                    opt_row = move[0]
                    opt_col = move[1]
                beta = min(beta, score)
                if alpha >= beta:
                    return (worst, opt_row, opt_col)
            return (worst, opt_row, opt_col)

    def minimax(self, player, Depth):
        if self.check_tie() or Depth == 0:
            return (0, None, None)
        opt_row = -1
        opt_col = -1
        if player == "0":
            if self.check_win(player):
                return (10, None, None)
            best = -1000000
            for move in self.get_possible_moves():
                self.place_player("0",move[0], move[1])
                score = self.minimax("X", Depth - 1)[0]
                self.place_player("-", move[0], move[1])
                if best < score:
                    best = score
                    opt_row = move[0]
                    opt_col = move[1]
            return (best, opt_row, opt_col)

        if player == "X":
            if self.check_win(player):
                return (-10, None, None)
            worst = 100000
            for move in self.get_possible_moves():
                self.place_player("X", move[0], move[1])
                score = self.minimax("0", Depth - 1)[0]
                self.place_player("-", move[0], move[1])
                if worst > score:
                    worst = score
                    opt_row = move[0]
                    opt_col = move[1]
            return (worst, opt_row, opt_col)

    def play_game(self):
        player = "0"
        gameRun = True
        while gameRun:
            player = self.change_player(player)
            self.take_turn(player)
            if player == "0":
                self.print_board()
            if self.check_win(player):
                print(player + " Wins!")
                gameRun = False
            elif self.check_tie():
                print("Tie")
                gameRun = False
        return

