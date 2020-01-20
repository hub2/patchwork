from helpers import available_moves
from strategy import Strategy
from main import Game
from copy import deepcopy


def test_available_moves():
    g = Game(Strategy(), Strategy())
    s = g.state

    moves = available_moves(s)
    for m in moves:
        new_state = deepcopy(g.state)

        new_state.apply(m)
        new_state.show()

    return moves


if __name__ == '__main__':
    m = test_available_moves()
    #print(m)
    print(len(m))
