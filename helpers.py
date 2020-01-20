from state import State
from typing import List
from piece import Piece
from board import Board
from move import PickAndPlaceMove, JumpMove, Move
import numpy as np


def can_be_placed(layout: np.array, position: tuple, board: Board) -> bool:
    x, y = position
    width, height = layout.shape
    if x + width > board.size or y + height > board.size:
        return False
    for i_layout, i in enumerate(range(x, x+width)):
        for j_layout, j in enumerate(range(y, y+height)):
            if layout[i_layout, j_layout] == 1 and board.board[i, j] == 1:
                    return False
    return True


def available_moves(state: State) -> List[Move]:
    moves: List[Move] = list()

    for piece in state.map.available_pieces():
        layouts = []
        if piece.price <= state.current_board.buttons:
            for flipped in [True, False]:
                for rotation in range(0, 4):
                    layout = piece.layout

                    if flipped:
                        layout = np.flip(layout)

                    layout = np.rot90(layout, k=-rotation)
                    for l in layouts:
                        if np.array_equal(l, layout):
                            continue

                    for x in range(state.current_board.size - layout.shape[0]+1):
                        for y in range(state.current_board.size - layout.shape[1]+1):
                            if can_be_placed(layout, (x, y), state.current_board):
                                moves.append(PickAndPlaceMove(piece, (x, y), rotation, flipped))
                    layouts.append(layout)


    moves.append(JumpMove())
    return moves
