from app.helpers import valid_move


def map_to_tile(ply):
    """
    Maps the player to proper tile.
    :param ply: Player string
    :return: returns 'O' if player is 'ai' else 'X'
    """
    return 'O' if ply == 'ai' else 'X'


def snapshot_board(b, player):
    """
    Snapshot of the board at it's current state. Checks at corners side rows and calculates
    how good is the state of the current board for the corresponding player.
    :param b: Board to snapshot
    :param player: Player
    :return: returns the total points of the board evaluation.
    """
    total = 0
    for y in range(8):
        for x in range(8):
            if b[y][x] == map_to_tile(player):
                if (x == 0 or x == 7) and (y == 0 or y == 7):
                    total += 4  # corner: woo!
                elif (x == 0 or x == 7) or (y == 0 or y == 7):
                    total += 2  # side: cool!
                else:
                    total += 1  # Anywhere else: meh...
    return total


def terminal_node(b, player):
    """
    If there are no valid moves, return true.
    :param b: Board to check
    :param player: player
    :return: boolean
    """
    for y in range(8):
        for x in range(8):
            if valid_move(b, x, y, player):
                return False
    return True
