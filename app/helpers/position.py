from app.board import show_board


def pickPos(x, y, board, who):

    move = False
    human = who == 'human'

    if board[x][y] == "-":

        # Look up down left and right for moves and execute moves
        for s in ['up', 'down', 'left', 'right']:
            pos = x - 1 if s == 'up' else x + \
                1 if s == 'down' else y - 1 if s == 'left' else y + 1
            try:
                axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
            except IndexError:
                return False
            if (axis == "O" or axis == "X") and not (axis == "X" and human or axis == "O" and not human):

                while axis == "O" if human else "X":
                    pos = pos - 1 if s == 'up' or s == 'left' else pos + 1
                    axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
                    if human and axis == "X" or not human and axis == "O":
                        # Player did a valid move, flip current tile
                        board[x][y] = "X" if human else "O"
                        # Now flip tiles in between and return if at least one was flipped
                        return flip_tiles(x, y, board, human, s)
                    elif axis == "-":
                        return False

        #  Look NorthWest SouthWest NorthEast SouthEast for moves and execute moves
        for s in ['ul', 'ur', 'dl', 'dr']:
            pos_y = y - 1 if s == 'ul' or s == 'ur' else y + 1
            pos_x = x - 1 if s == 'ul' or s == 'dl' else x + 1
            try:
                tile = board[pos_x, pos_y]
            except IndexError:
                return False
            if (tile == "O" or tile == "X") and not (tile == "X" and human or tile == "O" and not human):
                while tile == "O" if human else "X":
                    pos_y = pos_y - 1 if s == 'ul' or s == 'ur' else pos_y + 1
                    pos_x = pos_x - 1 if s == 'ul' or s == 'dl' else pos_x + 1
                    if human and tile == "X" or not human and tile == "O":
                        # Player did balid move
                        board[pos_x, pos_y] = "X" if human else "O" # !WARNING may produce error
                        # Now flip tiles
                        return flip_tiles(pos_x, pos_y, board, s)
                elif tile == '-':
                    return False

            # while board(pos_x, pos_y)

# UP LEFT

        #         if board[pos1][pos] == "X":
        #             # right move
        #             board[x][y] = "X"
        #             temp = x - 1
        #             temp1 = y-1
        #             while board[temp][temp1] == "O":
        #                 board[temp][temp1] = "X"
        #                 temp -= 1
        #                 temp1 -= 1
        #                 move = True

        #             break

        #  DOWN RIGHT

        #         if board[pos1][pos] == "X":
        #             # right move
        #             board[x][y] = "X"
        #             temp = x + 1
        #             temp1 = y+1
        #             while board[temp][temp1] == "O":
        #                 board[temp][temp1] = "X"
        #                 temp += 1
        #                 temp1 += 1
        #                 move = True

        #             break
        # DOWN LEFT

        #         if board[pos1][pos] == "X":
        #             # right move
        #             board[x][y] = "X"
        #             temp = x - 1
        #             temp1 = y+1
        #             while board[temp][temp1] == "O":
        #                 board[temp][temp1] = "X"
        #                 temp -= 1
        #                 temp1 += 1
        #                 move = True
        #             break

        # UP RIGHT

            #     if board[pos1][pos] == "X":
            #         # right move
            #         board[x][y] = "X"
            #         temp = x + 1
            #         temp1 = y-1
            #         while board[temp][temp1] == "O":
            #             board[temp][temp1] = "X"
            #             temp += 1
            #             temp1 -= 1
            #             move = True

            #         break
        return move
    else:
        return False

def flip_tiles_diagonally(x, y, board, s):
    pass

def flip_tiles(x, y, board, human, s):
    """
    DOES NOT WORK FOR DIAGONIA
    """
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
