import arcade
from tictactoe import *

class TicTacToeUI:

    def __init__(self):
        # Constants
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 800
        self.SCREEN_TITLE = "Welcome to TicTacToe"
        self.game = TicTacToe()


    def setup_board(self):
       arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
       arcade.set_background_color((43, 64, 89))


    def draw_grid(self):
       arcade.draw_text("Tic Tac Toe", 290, 750)
       SQUAREDIM = 200
       X = 50
       Y = 50
       for row in range(3):
           X = 50
           for col in range(3):
               arcade.draw_rectangle_outline(X + 100, Y + 100, SQUAREDIM, SQUAREDIM, (240,123,63))
               X += 200
           Y += 200

    def draw_board(self):
        X = 100
        Y = 525
        board = self.game.board
        for r in range(len(self.game.board)):
            for c in range(len(self.game.board[r])):
                if self.game.board[r][c] == "0" or self.game.board[r][c] == "X":
                    arcade.draw_text(str(self.game.board[r][c]), X, Y, arcade.color.WHITE,60, 100, 'center')
                X += 200
            X = 100
            Y -= 200
        return

    def runUI(self):
        game = TicTacToe()
        self.setup_board()
        arcade.start_render()
        self.draw_grid()
        arcade.finish_render()
        arcade.run()

        player = "0"
        gameRun = True
        while gameRun:
            arcade.start_render()
            player = self.game.change_player(player)
            self.game.take_turn(player)
            if player == "0":
                self.draw_board()
            if self.game.check_win(player):
                print(player + " Wins!")
                gameRun = False
            elif self.game.check_tie():
                print("Tie")
                gameRun = False
            arcade.finish_render()
        arcade.run()