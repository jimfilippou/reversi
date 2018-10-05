
def show_board(board):
    """
    Prints board to the screen
    """
    for i in range(len(board)):
        print()
        for j in range(len(board[i])):
            print(board[i][j], end="", flush=True)
