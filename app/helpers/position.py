from app.board import show_board


def pickPos(x, y, board, who):

    move = False
    human = who == 'human'

    if board[x][y] == "-":

        # Look up down left and right for moves and execute moves
        for s in ['up', 'down', 'left', 'right']:
            pos = x - 1 if s == 'up' else x + \
                1 if s == 'down' else y - 1 if s == 'left' else y + 1
            axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
            while axis == "O" if human else "X":
                pos = pos - 1 if s == 'up' or s == 'left' else pos + 1
                axis = board[pos][y] if s == 'up' or s == 'down' else board[x][pos]
                if axis == "X" if human else "O":
                    # right move
                    board[x][y] = "X" if human else "O"
                    temp = x - 1 if s == 'up' else x + \
                        1 if s == 'down' else y - 1 if s == 'left' else y + 1
                    condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
                    while condition == "O" if human else "X":
                        if s == 'up' or s == 'down':
                            board[temp][y] = "X" if human else "O"
                        else:
                            board[x][temp] = "X" if human else "O"
                        temp = temp - 1 if s == 'up' or s == 'left' else temp + 1
                        move = True
                        condition = board[temp][y] if s == 'up' or s == 'down' else board[x][temp]
                    break


        if board[x-1][y-1] == "O":
            pos = y - 1
            pos1 = x-1
            while board[pos1][pos] == "O":
                pos -= 1
                pos1 -= 1
                if board[pos1][pos] == "X":
                    # right move
                    board[x][y] = "X"
                    temp = x - 1
                    temp1 = y-1
                    while board[temp][temp1] == "O":
                        board[temp][temp1] = "X"
                        temp -= 1
                        temp1 -= 1
                        move = True

                    break
        if board[x+1][y+1] == "O":
            pos = y + 1
            pos1 = x+1
            while board[pos1][pos] == "O":
                pos += 1
                pos1 += 1
                if board[pos1][pos] == "X":
                    # right move
                    board[x][y] = "X"
                    temp = x + 1
                    temp1 = y+1
                    while board[temp][temp1] == "O":
                        board[temp][temp1] = "X"
                        temp += 1
                        temp1 += 1
                        move = True

                    break
        if board[x-1][y+1] == "O":
            pos = y + 1
            pos1 = x-1
            while board[pos1][pos] == "O":
                pos += 1
                pos1 -= 1
                if board[pos1][pos] == "X":
                    # right move
                    board[x][y] = "X"
                    temp = x - 1
                    temp1 = y+1
                    while board[temp][temp1] == "O":
                        board[temp][temp1] = "X"
                        temp -= 1
                        temp1 += 1
                        move = True
                    break

        if board[x+1][y-1] == "O":
            pos = y - 1
            pos1 = x+1
            while board[pos1][pos] == "O":
                pos -= 1
                pos1 += 1
                if board[pos1][pos] == "X":
                    # right move
                    board[x][y] = "X"
                    temp = x + 1
                    temp1 = y-1
                    while board[temp][temp1] == "O":
                        board[temp][temp1] = "X"
                        temp += 1
                        temp1 -= 1
                        move = True

                    break
        return move
    else:
        return move
