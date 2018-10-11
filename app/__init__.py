from app.board import *
from app.helpers import *
import time

board = initialize_board()

# Letter to coordinate (ltc)
ltc = lambda x: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(x) + 1

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
            y = ltc(str(ans).split(',')[1])
            
            should_move = pickPos(x, y, board, 'human')
            
            if should_move:
                player = 'ai'
            else:
                print("\nYou can't put your tile here!Choose another position.")
        else:
            # AI move
            print('\nAi is thinkging....')
            time.sleep(3)
            player = 'human'
