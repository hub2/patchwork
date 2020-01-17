from piece import Piece
from state import State
from board import Board
import numpy as np
import abc


class Move:
    @abc.abstractmethod
    def apply(self, state: State):
        pass

    @abc.abstractmethod
    def verify(self, state: State):
        pass

    def collect_bonuses(self, start: int, end: int):
        pass


class PickAndPlaceMove(Move):
    def __init__(self, piece: Piece, position: tuple, rotation: int, extra_fabric_position: tuple=None):
        self.piece = piece
        self.position = position
        self.rotation = rotation
        self.extra_fabric_position = extra_fabric_position

    def apply(self, state: State):
        board = state.current_board
        if not self.verify(self, state):
            raise ValueError("This move cannot be made")

        board.buttons -= self.piece.price

        layout = np.rot90(self.piece.layout, k=-self.rotation)

        x, y = self.position
        width, height = layout.shape

        for i_layout, i in enumerate(range(x, x+width)):
            for j_layout, j in enumerate(range(y, y+height)):
                if layout[i_layout, j_layout] == 1:
                    if board.board[i, j] == 1:
                        raise ValueError("You can not put a piece there")

                    board.board[i, j] = 1

        # TODO: handle collecting bonuses

    def verify(self, state: State) -> bool:
        board = state.current_board
        if board.buttons > self.piece.price:
            return False

        layout = np.rot90(self.piece.layout, k=-self.rotation)

        x, y = self.position
        width, height = layout.shape

        right_boundary = x + width
        down_boundary = y + height

        if right_boundary >= state.current_board.size[0]:
            return False

        if down_boundary >= state.current_board.size[1]:
            return False

        for i_layout, i in enumerate(range(x, right_boundary)):
            for j_layout, j in enumerate(range(y, down_boundary)):
                if layout[i_layout, j_layout] == 1:
                    if board.board[i, j] == 1:
                        return False

        return True


class JumpMove(Move):
    def __init__(self):
        pass

    def apply(self, state: State):
        board = state.current_board

        if board == state.p1board:
            my_offset = state.map.player1_offset
            other_players_offset = state.map.player2_offset
        else:
            my_offset = state.map.player2_offset
            other_players_offset = state.map.player1_offset

        buttons_bonus = other_players_offset - my_offset
        board.buttons += buttons_bonus

        # perform jump
        my_offset = other_players_offset+1

        # TODO: handle collecting bonuses

    def verify(self, state: State) -> bool:
        return True



