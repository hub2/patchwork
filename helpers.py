from state import State
from typing import List
from piece import Piece
from board import Board
from move import PickAndPlaceMove, JumpMove, Move
import numpy as np


def get_points(board: Board):
    x, y = np.where(board.board == 0)
    blanks = len(x)

    return board.buttons - (2*blanks) + (int(board.has_bonus) * 7)

def can_be_placed(layout: np.array, position: tuple, board: Board) -> bool:
    x, y = position
    width, height = layout.shape
    if x + width > board.size or y + height > board.size:
        return False
    for i_layout, i in enumerate(range(x, x + width)):
        for j_layout, j in enumerate(range(y, y + height)):
            if layout[i_layout, j_layout] == 1 and board.board[i, j] == 1:
                return False
    return True


def available_moves(state: State) -> List[Move]:
    moves: List[Move] = list()

    moves.append(JumpMove())
    for piece in state.map.available_pieces():
        #print(f"Pieces {piece} {state.current_board.board}")
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

                    for x in range(state.current_board.size - layout.shape[0] + 1):
                        for y in range(state.current_board.size - layout.shape[1] + 1):
                            if can_be_placed(layout, (x, y), state.current_board):
                                fabric = Move.collect_bonuses(state, state.current_player_offset,
                                                              state.current_player_offset + piece.moves,
                                                              apply_to_state=False)
                                if fabric:
                                    fabric_x, fabric_y = np.where(state.current_board.board == 0)
                                    for i in range(len(fabric_x)):
                                        extra_fabric_position = (fabric_x[i], fabric_y[i])
                                        width, height = layout.shape

                                        local_x = extra_fabric_position[0] - x
                                        local_y = extra_fabric_position[1] - y

                                        if 0 <= local_x < width and 0 <= local_y < height:
                                            if layout[local_x, local_y] == 1:
                                                continue

                                        moves.append(PickAndPlaceMove(piece, (x, y), rotation, flipped,
                                                                      extra_fabric_position=extra_fabric_position))

                                else:
                                    moves.append(PickAndPlaceMove(piece, (x, y), rotation, flipped))
                    layouts.append(layout)

    return moves
