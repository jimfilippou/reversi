import time

from app.ai import *
from app.board import *
from app.helpers import *

# Initialize 8x8 board
board = initialize_board()

# Initialize score
points = Score(human=2, ai=2)

# Initialize minimax depth
depth = ask_depth()

# Minimum evaluation for minimax
min_eval = -1

# Max evaluation for minimax.
max_eval = 101


def main():
    player = who_plays_first()
    print("\nHuman: %i" % points.human)
    print("   AI: %i" % points.ai)
    show_board(board)
    while True:
        if game_is_finished(points):
            show_winner(points)
            break
        if player == 'human':
            if not available_moves(board):
                player = 'ai'
                print("\nNot available moves!!!")
                time.sleep(2)
                continue
            ans = input("\nWhere do you want to put your tile? [X,Y] ")
            try:
                x = int(str(ans).split(',')[0])
                y = ltc(str(ans).split(',')[1])
            except ValueError:
                print('Please provide a proper coordinate.')
                continue
            actions = pick_pos(x, y, board, 'human')
            try:
                if actions.moves > 0:
                    points.add_points('human', actions.flips + 1)
                    points.sub_points('ai', actions.flips)
                    player = 'ai'
                    print("\nHuman: %i" % points.human)
                    print("   AI: %i" % points.ai)
                    show_board(board)
                else:
                    print("\nYou can't put your tile here!Choose another position.")
            except AttributeError:
                continue
        else:
            # AI move
            print('\nThinking....')
            move = best_move(board, 'ai')
            ndl = pick_pos(move[0], move[1], board, 'ai')
            points.add_points('ai', ndl.flips + 1)
            points.sub_points('human', ndl.flips)
            print("\nHuman: %i" % points.human)
            print("   AI: %i" % points.ai)
            player = 'human'
            show_board(board)


def best_move(b, player):
    """
    Initially starts with the worst points which is 0, and while looping through the 8x8 grid,
    it compares the current points to the move points. If there is a better move, then pick that move
    and continue. When the function finds the best move, it returns the coordinates of that move.
    :param b: Board
    :param player: Player
    :return: (x, y): Returns a tuple that indicates the best move's coordinates.
    """
    max_points = 0
    mx = -1
    my = -1
    for x in range(8):
        for y in range(8):
            if valid_move(b, x, y, player):
                try:
                    pick_pos(x, y, copy.deepcopy(b), player)
                    pts = minimax(b, player, depth, min_eval, max_eval, True)
                    if pts > max_points:
                        max_points = pts
                        mx = x
                        my = y
                except AttributeError:
                    continue
    return mx, my


def minimax(boar, player, depth, alpha, beta, maximizing):
    """
    The minimax implementation using a/b pruning.
    :param boar: The board passed
    :param player: The current player
    :param depth: The max depth of the algorithm
    :param alpha: Alpha
    :param beta: Beta
    :param maximizing: True when maximizing, false when minimizing
    :return:
    """
    if depth == 0 or terminal_node(boar, player):
        return snapshot_board(boar, player)
    if maximizing:
        v = min_eval
        for y in range(8):
            for x in range(8):
                if valid_move(boar, x, y, player):
                    move = pick_pos(x=x, y=y, board=copy.deepcopy(boar), who=player)
                    try:
                        v = max(v, minimax(move.board, player, depth - 1, alpha, beta, False))
                        alpha = max(alpha, v)
                        if beta <= alpha:
                            break  # beta cut-off
                    except AttributeError:
                        continue

        return v
    else:
        v = max_eval
        for y in range(8):
            for x in range(8):
                if valid_move(boar, x, y, player):
                    move = pick_pos(board=copy.deepcopy(boar), x=x, y=y, who=player)
                    try:
                        v = min(v, minimax(move.board, player, depth - 1, alpha, beta, True))
                        beta = min(beta, v)
                        if beta <= alpha:
                            break  # alpha cut-off
                    except AttributeError:
                        continue

        return v
