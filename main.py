from board import Board
from map import Map
from state import State
import numpy as np
from strategy import Strategy, RandomStrategy, EducatedRandomStrategy, AlphaBeta
import sys
from pieces import pieces_types
import json
from helpers import get_points

class Game:
    def __init__(self, strategy1: Strategy, strategy2: Strategy):
        self.board1 = Board()
        self.board2 = Board()
        self.state = State(Map(), self.board1, self.board2)
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.is_live = False
        self.history = []

    def run(self):
        self.is_live = True
        self.history.append(self.state.to_dict())

        while self.is_live:
            print(f"Player1 offset: {self.state.map.player1_offset}")
            print(f"Player2 offset: {self.state.map.player2_offset}")
            self.state.show()
            self.state.current_board = self.state.get_further_player()

            if self.state.current_board == self.board1:
                move = self.strategy1.get_move(self.state)
            else:
                move = self.strategy2.get_move(self.state)

            self.state.apply(move)
            self.history.append(self.state.to_dict())

            if self.state.map.player1_offset >= self.state.map.length and \
                    self.state.map.player2_offset >= self.state.map.length:
                self.is_live = False
        print(f"Player 1 points {get_points(self.state.p1board)}")
        print(f"Player 2 points {get_points(self.state.p2board)}")

        print("{}".format(np.sum(self.state.p1board.board)+np.sum(self.state.p2board.board)), file=sys.stderr)
        return get_points(self.state.p1board), get_points(self.state.p2board)

    def to_dict(self):
        return {
            "history": self.history,
            "pieces_types": [piece.to_dict() for piece in pieces_types]
        }



def main():
    #g = Game(RandomStrategy(), RandomStrategy())
    p1wins = 0
    #for i in range(100):
    g = Game(AlphaBeta(), EducatedRandomStrategy())
    p1, p2 = g.run()
        #if p1 > p2:
        #    p1wins += 1
    #print(p1wins)

    game_json = json.dumps(g.to_dict())
    with open("front/history.json", "w") as f:
        f.write(game_json)


if __name__ == '__main__':
    main()
