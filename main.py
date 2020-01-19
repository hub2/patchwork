from board import Board
from map import Map
from state import State
import numpy as np
from strategy import Strategy, RandomStrategy
import sys

class Game:
    def __init__(self, strategy1: Strategy, strategy2: Strategy):
        self.board1 = Board()
        self.board2 = Board()
        self.state = State(Map(), self.board1, self.board2)
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.is_live = False

    def run(self):
        self.is_live = True

        while self.is_live:
            print(f"Player1 offset: {self.state.map.player1_offset}")
            print(f"Player2 offset: {self.state.map.player2_offset}")
            self.state.show()
            self.state.current_board = self.state.get_further_player()

            if self.state.current_board == self.board1:
                move = self.strategy1.get_move(self.state)
            else:
                move = self.strategy2.get_move(self.state)
            print(type(move))
            self.state.apply(move)

            if self.state.map.player1_offset >= self.state.map.length and \
                    self.state.map.player2_offset >= self.state.map.length:
                self.is_live = False
        print("{}".format(np.sum(self.state.p1board.board)+np.sum(self.state.p2board.board)), file=sys.stderr)


def main():
    for i in range(100):
        g = Game(RandomStrategy(), RandomStrategy())
        g.run()


if __name__ == '__main__':
    main()
