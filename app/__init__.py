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


def game_is_finished(pts):
    return pts.total >= 64


def show_winner(pts):
    if pts.human > pts.ai:
        print('Human won!')
    elif pts.human < pts.ai:
        print('AI won!')
    else:
        print('It\'s a tie!')


def main():
    """
    The main loop of the game.
    :return:
    """
    points = Score(human=2, ai=2)
    player = who_plays_first()
    show_board(board)
    while True:
        if game_is_finished(points):
            show_winner(points)
            break
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
            try:
                if actions.moves > 0:
                    points.human = points.human + 1
                    points.human = points.human + actions.flips
                    points.ai = points.ai - actions.flips
                    player = 'ai'
                    show_board(board)
                else:
                    print("\nYou can't put your tile here!Choose another position.")
            except AttributeError:
                continue
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
                        if i == 8 and j == 8 and not actions.moves > 0:
                            print("No posible moves!!! It's your turn!")
                            player = "human"
                            done = True
                            break
                    except AttributeError:
                        continue
                    try:
                        if actions.moves > 0:
                            points.ai = points.ai + 1
                            points.ai = points.ai + actions.flips
                            points.human = points.human - actions.flips
                            player = 'human'
                            done = True
                            break
                    except AttributeError:
                        continue
                if done:
                    break
            # os.system('cls')
            show_board(board)
