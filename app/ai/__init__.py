from app.helpers import valid_move


def map_to_tile(ply):
    return 'O' if ply == 'ai' else 'X'


def snapshot_board(b, player):
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


# if no valid move(s) possible then True
def terminal_node(b, player):
    for y in range(8):
        for x in range(8):
            if valid_move(b, x, y, player):
                return False
    return True
