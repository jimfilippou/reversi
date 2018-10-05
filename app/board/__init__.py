from .show import show_board

def initialize_board():
    """
    Initializes a 8x8 board with initial tile placements.
    """
    board = []
    for i in range(8):
        c = []
        for j in range(8):
            c.append(0)
        
        board.append(c)
    board[3][3] = 'W'
    board[4][4] = 'W'
    board[4][3] = 'B'
    board[3][4] = 'B'
    return board
