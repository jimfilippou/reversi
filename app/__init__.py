from app.board import *
from app.helpers import *
import time, os

board = initialize_board()

# Letter to coordinate (ltc)


def ltc(x): return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(x) + 1


def main():

    run = True
    player = who_plays_first()  # Αρχικοποίηση για το ποιός παίζει πρώτος.
    show_board(board)

    while run:
        if player == 'human':
            ans = input("\nWhere do you want to put your tile? [X,Y] ")
            if ans == 'break':
                break
            x = int(str(ans).split(',')[0])
            y = ltc(str(ans).split(',')[1])

            should_move = pickPos(x, y, board, 'human')

            if should_move:
                player = 'ai'
                # os.system('cls')
                show_board(board)
            else:
                print("\nYou can't put your tile here!Choose another position.")
        else:
            # AI move
            done = False
            print('\nThinking....')
            time.sleep(1)
            for i in range(8):
                for j in range(8):
                    print(i+1, j+1)
                    should_move = pickPos(i+1, j+1, board, 'ai')
                    if should_move:
                        player = 'human'
                        done = True
                        break
                if done:
                    break
            # os.system('cls')
            show_board(board)

