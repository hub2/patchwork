from consts import MAP_LENGTH
from pieces import pieces_types
from board import Board
from piece import Piece
from typing import List
import random

#random.seed(1)


class Map:
    def __init__(self, pieces: List[Piece] = None, pointer_offset: int = 1, player1_offset: int = 0, player2_offset: int = 0):
        self.length = MAP_LENGTH
        self.player1_offset = player1_offset
        self.player2_offset = player2_offset
        self.pointer_offset = pointer_offset
        if not pieces:
            self.pieces = pieces_types[:]
            starting_piece = self.pieces[0]
            random.shuffle(self.pieces)
            self.pointer_offset = self.pieces.index(starting_piece) + 1

    def get_further_player(self, player1: Board, player2: Board) -> Board:
        if self.player1_offset == self.player2_offset:
            return None
        if self.player1_offset < self.player2_offset:
            return player1
        else:
            return player2

    def available_pieces(self) -> list:
        end = (self.pointer_offset+3) % len(self.pieces)
        if end < self.pointer_offset:
            return self.pieces[self.pointer_offset:] + self.pieces[:end]
        else:
            return self.pieces[self.pointer_offset:end]

    def show(self):
        print("Pieces:")
        for idx, piece in enumerate(self.pieces):
            if idx == self.pointer_offset:
                print("==POINTER==", end="")
            print(piece.name, end=" ")
        print("")

        print("Player 1 is at {self.player1_offset}")
        print("Player 2 is at {self.player2_offset}")

    def to_dict(self):
        return {
            "length": self.length,
            "player1_offset": self.player1_offset,
            "player2_offset": self.player2_offset,
            "pointer_offset": self.pointer_offset,
            "pieces": [piece.to_dict() for piece in self.pieces]
        }
