import arcade

class TicTacToeUI:

    def __init__(self):
        # Constants
        self.SCREEN_WIDTH = 700
        self.SCREEN_HEIGHT = 800
        self.SCREEN_TITLE = "Welcome to TicTacToe"

    def setup_board(self):
       arcade.open_window(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
       arcade.set_background_color((43, 64, 89))


    def draw_grid(self):
       SQUAREDIM = 200
       X = 50
       Y = 50
       for row in range(3):
           X = 50
           for col in range(3):
               arcade.draw_rectangle_outline(X + 100, Y + 100, SQUAREDIM, SQUAREDIM, (240,123,63))
               X += 200
           Y += 200

    def runUI(self):
        self.setup_board()
        arcade.start_render()
        self.draw_grid()
        arcade.finish_render()
        arcade.run()