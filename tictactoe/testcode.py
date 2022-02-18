from tictactoe import *

game = TicTacToe()

board1 = [['X', '-', '-'], ['-','-', '-'], ['-','-', '-']]
board2 =[['X', '0', '-'], ['X','-', '-'], ['-','-', '-']]
board3 =[['X', '0', 'X'], ['0','0', 'X'], ['-','X', '-']]
board4 =[['X', 'X', '-'], ['0','-', '-'], ['-','-', '-']]
board5 =[['X', '0', '0'], ['0','X', 'X'], ['-','X', '-']]



list0fBoards = [board1, board2, board3, board4, board5]
depth = 100
for board in list0fBoards:
    game.board = board
    min_start = time.time()
    score1, mm_row, mm_col = game.minimax("0", depth)
    min_end = time.time()

    alpha = -100
    beta = 100
    game.board = board
    ab_start = time.time()
    score2, ab_row, ab_col = game.minimax_alpha_beta("0", depth, alpha, beta)
    ab_end = time.time()

    if mm_row == ab_row and mm_col == ab_col:
        print("passed")
        print("Mini Max got(" + str(mm_row) + ", " + str(mm_col) + ")")
        print("Mini Max Alpha Beta got(" + str(ab_row) + ", " + str(ab_col) + ")" + "\n")
    else:
        print("Mini Max got(" + str(mm_row) + ", " + str(mm_col) + ")")
        print("Mini Max Alpha Beta got(" + str(ab_row) + ", " + str(ab_col) + ")" + "\n")
        print("Minimax got score: " + str(score1))
        print("Minimax AB got score: " + str(score2) + "\n")
    print("minimax Alpha Beta took: ", ab_end - ab_start, "seconds")
    print("minimax took: ", min_end - min_start, "seconds" + "\n")
