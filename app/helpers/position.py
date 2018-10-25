from app.board import show_board


class Actions:
    def __init__(self, x, y, moves):
        self.x = x
        self.y = y
        self.moves = moves


def pickPos(x, y, board, who):

    actions = Actions(x, y, 0)

    # ok = False
    human = who == 'human'

    if board[x][y] == "-":

        # Look up down left and right for moves and execute moves
        for s in ['up', 'down', 'left', 'right']:
            pos = x - 1 if s == 'up' else x + \
                1 if s == 'down' else y - 1 if s == 'left' else y + 1
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
                        continue
                    if human and axis == "X" or not human and axis == "O":
                        # Player did a valid move, flip current tile
                        board[x][y] = "X" if human else "O"
                        actions.moves += 1
                        # Now flip tiles in between and return if at least one was flipped
                        flip_tiles(x, y, board, human, s)
                    elif axis == "-":
                        break

        #  Look NorthWest SouthWest NorthEast SouthEast for moves and execute moves
        for s in ['ul', 'ur', 'dl', 'dr']:
            if s == 'ul':
                pos_y = y - 1
                pos_x = x - 1
            elif s == 'ur':
                pos_y = y + 1
                pos_x = x - 1
            elif s == 'dl':
                pos_y = y - 1
                pos_x = x + 1
            elif s == 'dr':
                pos_y = y + 1
                pos_x = x + 1
            try:
                tile = board[pos_x][pos_y]
            except IndexError:
                continue
            if (tile == "O" or tile == "X") and not (tile == "X" and human or tile == "O" and not human):
                while tile == "O" if human else "X":
                    if s == 'ul':
                        pos_y -= 1
                        pos_x -= 1
                    elif s == 'ur':
                        pos_y += 1
                        pos_x -= 1
                    elif s == 'dl':
                        pos_y -= 1
                        pos_x += 1
                    elif s == 'dr':
                        pos_y += 1
                        pos_x += 1
                    try:
                        tile = board[pos_x][pos_y]
                    except IndexError as err:
                        continue
                    if human and tile == "X" or not human and tile == "O":
                        # ? Player did a valid move here
                        board[x][y] = "X" if human else "O"
                        flip_tiles_diagonally(x, y, board, human, s)
                        actions.moves += 1
                    elif tile == '-':
                        break  # ! break ?

        return actions.moves > 0


def flip_tiles_diagonally(x, y, board, human, s):
    response = False
    if s == 'ul':
        temp_y = y - 1
        temp_x = x - 1
    elif s == 'ur':
        temp_y = y + 1
        temp_x = x - 1
    elif s == 'dl':
        temp_y = y - 1
        temp_x = x + 1
    elif s == 'dr':
        temp_y = y + 1
        temp_x = x + 1
    condition = board[temp_x][temp_y]
    while (human and condition == "O") or (not human and condition == "X"):
        board[temp_x][temp_y] = "X" if human else "O"
        if not response:
            response = True
        condition = board[temp_x][temp_y]
    return response


def flip_tiles(x, y, board, human, s):
    response = False
    temp = x - 1 if s == 'up' else x + \
        1 if s == 'down' else y - 1 if s == 'left' else y + 1
    condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
    while (human and condition == "O") or (not human and condition == "X"):
        if s == 'up' or s == 'down':
            board[temp][y] = "X" if human else "O"
        else:
            board[x][temp] = "X" if human else "O"
        temp = temp - 1 if s == 'up' or s == 'left' else temp + 1
        if not response:
            response = True
        condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
    return response
