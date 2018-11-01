import time

from app.board import *
from app.helpers import *

board = initialize_board()


def ltc(x):
    """
    Letter to coordinate function is used to transform a letter from upper X axis
    to the corresponding value on the 8x8 grid.
    :param x: The letter to search
    :return: A number which corresponds to proper coordinate.
    """
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(x) + 1


def main():
    run = True
    points = Score(2, 2)
    player = who_plays_first()
    show_board(board)
    while run:
        if points.total >= 64:
            print('\ngame over!!')
            if points.human > points.ai:
                print('You win!!!')
            elif points.human < points.ai:
                print('You lost!!!')
            else:
                print('Tied!!!')
            break
        else:
            if player == 'human':
                ans = input("\nWhere do you want to put your tile? [X,Y] ")
                if ans == 'break':
                    break
                try:
                    x = int(str(ans).split(',')[0])
                    y = ltc(str(ans).split(',')[1])
                except ValueError as err:
                    print('Please provide a proper coordinate.')
                    continue

                actions = pick_pos(x, y, board, 'human')

                if actions.moves > 0:
                    player = 'ai'
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
                        print(i + 1, j + 1)
                        actions = pick_pos(i + 1, j + 1, board, 'ai')
                        try:
                            if actions.moves > 0:
                                player = 'human'
                                done = True
                                break
                        except AttributeError:
                            continue
                    if done:
                        break
                # os.system('cls')
                show_board(board)
