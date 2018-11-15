from .flip import flip_tiles, flip_tiles_diagonally


class Actions:
    def __init__(self, moves, flips, x, y):
        self.moves = moves
        self.flips = flips
        self.x = x
        self.y = y


def pick_pos(x, y, board, who):
    actions = Actions(0, 0, x, y)
    actions.board = board
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
