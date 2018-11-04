import copy

from .position import pick_pos
from .score import Score


# All functions below are for generic use


def who_plays_first():
    """
    Asks user if he/she wants to play first.
    Returns 'human' if human plays first and 'ai' if computer plays first.
    """
    ans = ''
    while str(ans).lower() != 'y' or str(ans).lower() != 'n':
        ans = input("Do you want to play first? [Y/N] ")
        if str(ans).lower() == 'y' or str(ans).lower() == 'n':
            break
    return 'human' if str(ans).lower() == 'y' else 'ai'


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


def available_moves(board):
    for i in range(8):
        for j in range(8):
            actions = pick_pos(i + 1, j + 1, copy.deepcopy(board), 'human')
            try:
                if actions.moves > 0:
                    return True
            except AttributeError:
                continue
    return False
