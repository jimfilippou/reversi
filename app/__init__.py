from app.board import *

board = initialize_board()


def main():
    ans = ''
    while str(ans).lower() != 'y' or str(ans).lower() != 'n':
        ans = input("Do you want to play first? [Y/N] ")
        if str(ans).lower() == 'y' or str(ans).lower() == 'n':
            break

    if ans == "Y" or ans == "y":
        FirstPlayer = 'human'
    else:
        FirstPlayer = 'ai'

    if FirstPlayer == 'human':
        ans = input("Where do you want to put your tile? [X,Y] ")
        x = int(str(ans).split(',')[0])
        y = int(str(ans).split(',')[1])

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
                        show_board(board)
                        break
            elif board[x][y-1] == "O":
                pos = y-1
                while board[x][pos] == "O":
                    pos -= 1
                    if board[x][pos] == "X":
                        # right move
                        board[x][y] = "X"
                        show_board(board)
                        break
            elif board[x][y+1] == "O":
                pos = y+1
                while board[x][pos] == "O":
                    pos += 1
                    if board[x][pos] == "X":
                        # right move
                        board[x][y] = "X"
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
                        show_board(board)
                        break
            else:
                print("You can't put your tile here!Please choose another position.")            
                                        

                                       
                            
        else:
            print("You can't put your tile here!Please choose another position.")              

                
