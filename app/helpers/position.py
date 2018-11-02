class Actions:
    def __init__(self, moves, flips):
        self.moves = moves
        self.flips = flips


def pick_pos(x, y, board, who):
    actions = Actions(0, 0)
    human = who == 'human'

    if board[x][y] == "-":

        # Look up down left and right for moves and execute moves
        for s in ['up', 'down', 'left', 'right']:
            pos = x - 1 if s == 'up' else x + 1 if s == 'down' else y - 1 if s == 'left' else y + 1
            try:
                axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
            except IndexError:
                continue
            if (axis == "O" or axis == "X") and not (axis == "X" and human or axis == "O" and not human):
                while axis == "O" if human else "X":
                    pos = pos - 1 if s == 'up' or s == 'left' else pos + 1
                    try:
                        axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
                    except IndexError:
                        break
                    if human and axis == "X" or not human and axis == "O":
                        # Player did a valid move, flip current tile
                        board[x][y] = "X" if human else "O"
                        actions.moves += 1
                        actions.flips = flip_tiles(x, y, board, human, s)
                    elif axis == "-":
                        break

        #  Look NorthWest SouthWest NorthEast SouthEast for moves and execute moves
        for s in ['ul', 'ur', 'dl', 'dr']:
            pos_y = y - 1 if s == 'ul' or s == 'dl' else y + 1
            pos_x = x - 1 if s == 'ul' or s == 'ur' else x + 1
            try:
                tile = board[pos_x][pos_y]
            except IndexError:
                continue
            if (tile == "O" or tile == "X") and not (tile == "X" and human or tile == "O" and not human):
                while tile == "O" if human else "X":
                    pos_y = pos_y - 1 if s == 'ul' or s == 'dl' else pos_y + 1
                    pos_x = pos_x - 1 if s == 'ul' or s == 'ur' else pos_x + 1
                    try:
                        tile = board[pos_x][pos_y]
                    except IndexError:
                        break
                    if human and tile == "X" or not human and tile == "O":
                        # Player did a valid move, flip current tile
                        board[x][y] = "X" if human else "O"
                        actions.moves += 1
                        actions.flips = flip_tiles_diagonally(x, y, board, human, s)
                    elif tile == '-':
                        break

        return actions


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
