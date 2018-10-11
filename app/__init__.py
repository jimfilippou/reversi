from app.board import *
from app.helpers import *
import time

board = initialize_board()


def get_y_from_letter(letter):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return letters.index(letter) + 1


def main():

    run = True
    player = who_plays_first() # Αρχικοποίηση για το ποιός παίζει πρώτος. 

    while run:
        show_board(board)
        if player == 'human':
            ans = input("\nWhere do you want to put your tile? [X,Y] ")
            if ans == 'break':
                break
            x = int(str(ans).split(',')[0])
            y = get_y_from_letter(str(ans).split(',')[1])
            
            should_move = pickPos(x, y, board)
            
            if should_move == 'true':
                player = 'ai'
            else:
                print("\nYou can't put your tile here!Choose another position.")
        else:
            # AI move
            print('\nAi is thinkging....')
            time.sleep(3)
            player = 'human'
