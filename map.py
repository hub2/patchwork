from consts import MAP_LENGTH
from pieces import pieces_types
from board import Board
import random

random.seed(1)


class Map:
    def __init__(self, pieces: list = None, pointer_offset: int = 1, player1_offset: int = 0, player2_offset: int = 0):
        self.length = MAP_LENGTH
        self.player1_offset = player1_offset
        self.player2_offset = player2_offset
        self.pointer_offset = pointer_offset
        if not pieces:
            self.pieces = pieces_types
            starting_piece = self.pieces[0]
            random.shuffle(self.pieces)
            self.pointer_offset = self.pieces.index(starting_piece)

    def get_further_player(self, player1: Board, player2: Board) -> Board:
        # TODO: what if they overlap
        if self.player1_offset < self.player2_offset:
            return player1
        else:
            return player2

    def available_pieces(self) -> list:
        return self.pieces[self.pointer_offset:self.pointer_offset+3]

    def show(self):
        print("Pieces:")
        for idx, piece in enumerate(self.pieces):
            if idx == self.pointer_offset:
                print("==POINTER==")
            print(piece.name, end=" ")
        print("")

        print("Player 1 is at {self.player1_offset}")
        print("Player 2 is at {self.player2_offset}")
