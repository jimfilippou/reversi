
board = []


def initialize_board():
    for row in range(8):
        constructed_col = []
        for col in range(8):
            constructed_col.append(0)
        board.append(constructed_col)
    board[3][3] = 'W'
    board[4][4] = 'W'
    board[4][3] = 'B'
    board[3][4] = 'B'


def main():
    initialize_board()
    show_board()


def show_board():
    for i in range(len(board)):
        print()
        for j in range(len(board[i])):
            print(board[i][j], end="", flush=True)


if __name__ == '__main__':
    main()
