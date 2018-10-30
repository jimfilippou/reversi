from app.board import *
from app.helpers import *
import time

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
    counter = 4
    counter_human = 2
    counter_ai = 2
    player = who_plays_first()  # Αρχικοποίηση για το ποιός παίζει πρώτος.
    show_board(board)
    while run:
        if counter >= 64:
            print('\ngame over!!!')
            if counter_human > counter_ai:
                print('You win!!!')
            elif counter_human < counter_ai:
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

                should_move = pickPos(x, y, board, counter_ai, counter_human, 'human')

                if should_move:
                    player = 'ai'
                    counter += 1
                    counter_human += 1
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
                        print(i + 1, j + 1)
                        should_move = pickPos(i + 1, j + 1, board, counter_ai, counter_human, 'ai')
                        if should_move:
                            player = 'human'
                            counter += 1
                            counter_ai += 1
                            done = True
                            break
                        if i == 8 and j == 8 and not should_move:
                            print("No posible moves!!! It's your turn!")
                            player = "human"
                            done = True
                            break
                    if done:
                        break
                # os.system('cls')
                show_board(board)
