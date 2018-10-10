 if board[x][y] == "-":
            if board[x-1][y] == "O":
                pos = x-1
                while board[pos][y] == "O":
                    pos -= 1
                    if board[pos][y] == "X":
                        # right move
                        board[x][y] = "X"
                        temp = x - 1
                        while board[temp][y] == "O":
                            board[temp][y] = "X"
                            temp -=1
                        
                        show_board(board)
                        break
            elif board[x+1][y] == "O":
                pos = x+1
                while board[pos][y] == "O":
                    pos += 1
                    if board[pos][y] == "X":
                        # right move
                        board[x][y] = "X"
                        temp = x + 1
                        while board[temp][y] == "O":
                            board[temp][y] = "X"
                            temp +=1
                        show_board(board)
                        break
            elif board[x][y-1] == "O":
                pos = y-1
                while board[x][pos] == "O":
                    pos -= 1
                    if board[x][pos] == "X":
                        # right move
                        board[x][y] = "X"
                        temp = y - 1
                        while board[x][temp] == "O":
                            board[x][temp] = "X"
                            temp -=1
                        show_board(board)
                        break
            elif board[x][y+1] == "O":
                pos = y+1
                while board[x][pos] == "O":
                    pos += 1
                    if board[x][pos] == "X":
                        # right move
                        board[x][y] = "X"
                        temp = y + 1
                        while board[x][temp] == "O":
                            board[x][temp] = "X"
                            temp +=1
                        show_board(board)
                        break
            elif board[x-1][y-1] == "O":
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
                            temp -=1
                            temp1 -=1
                        show_board(board)
                        break
            elif board[x+1][y+1] == "O":
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
                            temp +=1
                            temp1 +=1

                        show_board(board)
                        break
            else:
                print("You can't put your tile here!Please choose another position.")