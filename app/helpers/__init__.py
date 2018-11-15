import copy

from .position import pick_pos
from .score import Score


# All functions below are for generic use


def ask_depth():
    while True:
        ans = input("Set difficulty: \n1) Easy\n2) Normal\n3) Pro\n")
        if int(ans) in [1, 2, 3]:
            return [4, 8, 12][int(ans) - 1]


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
        print('\nHuman won!')
    elif pts.human < pts.ai:
        print('\nAI won!')
    else:
        print('\nIt\'s a tie!')


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


def valid_move(_board, x, y, player):
    if x < 0 or x > 8 - 1 or y < 0 or y > 8 - 1:
        return False
    move = pick_pos(x, y, copy.deepcopy(_board), player)
    try:
        if move.moves > 0:
            return True
        else:
            return False
    except AttributeError:
        return False
