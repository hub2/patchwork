from map import Map
from board import Board
import copy

class State:
    def __init__(self, map: Map, p1board: Board, p2board: Board):
        self.map: Map = map
        self.current_board = p1board
        self.p1board = p1board
        self.p2board = p2board

    def get_further_player(self):
        player = self.map.get_further_player(self.p1board, self.p2board)
        if not player:
            return self.current_board
        return player

    @property
    def current_player_offset(self):
        if self.current_board == self.p1board:
            return self.map.player1_offset
        else:
            return self.map.player2_offset

    def apply(self, move: "Move"):
        return move.apply(self)

    def verify(self, move: "Move"):
        return move.verify(self)

    def show(self):
        if self.current_board == self.p1board:
            print("Player 1 turn")
        else:
            print("Player 2 turn")

        self.map.show()

        print("Player 1 board")
        self.p1board.show()
        print("Player 2 board")
        self.p2board.show()

    def copy(self):
        new_p1_board = self.p1board.copy()
        new_p2_board = self.p2board.copy()
        new_map = self.map.copy()

        new_s = State(new_map, new_p1_board, new_p2_board)
        if self.p1board == self.current_board:
            new_s.current_board = new_p1_board
        else:
            new_s.current_board = new_p2_board
        return new_s

    def to_dict(self):
        return {
            "p1board": self.p1board.to_dict(),
            "p2board": self.p2board.to_dict(),
            "current_board": "p1board" if self.current_board == self.p1board else "p2board",
            "map": self.map.to_dict()
        }
