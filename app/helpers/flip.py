def flip_tiles_diagonally(x, y, board, human, s):
    """
    Flips tiles on the board diagonally starting from X,Y
    :param x:
    :param y:
    :param board:
    :param human:
    :param s:
    :return:
    """
    flips = 0
    temp_y = y - 1 if s == 'ul' or s == 'dl' else y + 1
    temp_x = x - 1 if s == 'ul' or s == 'ur' else x + 1
    condition = board[temp_x][temp_y]
    while (human and condition == "O") or (not human and condition == "X"):
        board[temp_x][temp_y] = "X" if human else "O"
        flips += 1
        condition = board[temp_x][temp_y]
    return flips


def flip_tiles(x, y, board, human, s):
    """
    Flips tiles on the board starting from X,Y
    :param x: X coordinate
    :param y: Y coordinate
    :param board: The board array
    :param human: Indicates if current player is human or not
    :param s: Directions provided as strings
    :return: How many tiles were flipped
    """
    flipped = 0
    temp = x - 1 if s == 'up' else x + 1 if s == 'down' else y - 1 if s == 'left' else y + 1
    condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
    while (human and condition == "O") or (not human and condition == "X"):
        if s == 'up' or s == 'down':
            board[temp][y] = "X" if human else "O"
        else:
            board[x][temp] = "X" if human else "O"
        flipped += 1
        temp = temp - 1 if s == 'up' or s == 'left' else temp + 1
        condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
    return flipped
