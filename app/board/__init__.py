from .show import show_board

def initialize_board():
    """
    Initializes a 8x8 board with initial tile placements.
    """
    board = []
    for i in range(9):
        c = []
        for j in range(9):
            c.append('-')
        
        board.append(c)
    board[0][0] = '0' 
    board[1][0] = '1'
    board[2][0] = '2'
    board[3][0] = '3'
    board[4][0] = '4'
    board[5][0] = '5' 
    board[6][0] = '6'
    board[7][0] = '7'
    board[8][0] = '8'

    board[0][1] = 'A'
    board[0][2] = 'B'
    board[0][3] = 'C'
    board[0][4] = 'D'
    board[0][5] = 'E' 
    board[0][6] = 'F'
    board[0][7] = 'G'
    board[0][8] = 'H'

    board[4][4] = 'O'
    board[5][5] = 'O'
    board[5][4] = 'X'
    board[4][5] = 'X'
    return board
