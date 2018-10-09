from .show import show_board

def initialize_board():
    """
    Initializes a 8x8 board with initial tile placements.
    """
    board = []
    for i in range(8):
        c = []
        for j in range(8):
            c.append('-')
        
        board.append(c)
    board[3][3] = 'O'
    board[4][4] = 'O'
    board[4][3] = 'X'
    board[3][4] = 'X'
    return board
