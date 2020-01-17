from map import Map
from board import Board


class State:
    def __init__(self, map: Map, p1board: Board, p2board: Board):
        self.map = map
        self.current_board = p1board
        self.p1board = p1board
        self.p2board = p2board

    def get_further_player(self):
        player = self.map.get_further_player(self.p1board, self.p2board)
        if not player:
            return self.current_board
        return player

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

