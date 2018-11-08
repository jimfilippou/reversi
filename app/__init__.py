import time

from app.board import *
from app.helpers import *

board = initialize_board()
points = Score(human=2, ai=2)


def main():
    """
    The main loop of the game.
    :return:
    """
    player = who_plays_first()
    depth = ask_depth()
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
            time.sleep(1)
            moves = []
            for i in range(8):
                for j in range(8):
                    actions = pick_pos(i + 1, j + 1, copy.deepcopy(board), 'ai')
                    try:
                        if i == 8 and j == 8 and not actions.moves > 0:
                            print("No possible moves!!! It's your turn!")
                            player = "human"
                            done = True
                            break
                    except AttributeError:
                        continue
                    try:
                        if actions.moves > 0:
                            moves.append(actions)
                    except AttributeError:
                        continue
            player = 'human'
            show_board(board)
