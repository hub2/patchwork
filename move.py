from piece import Piece
from state import State
from consts import SINGLE_FABRIC_PLACEMENT, BUTTONS_PLACEMENT
import numpy as np
import abc


class Move:
    @abc.abstractmethod
    def apply(self, state: State):
        pass

    @abc.abstractmethod
    def verify(self, state: State):
        pass

    def collect_bonuses(self, state: State, start: int, end: int) -> tuple:
        buttons = sum(BUTTONS_PLACEMENT[start:end+1])
        fabrics = sum(SINGLE_FABRIC_PLACEMENT[start:end+1])

        state.current_board.buttons += buttons*state.current_board.buttons_on_board

        return fabrics

    def move_fields(self, state: State, how_much: int):
        board = state.current_board
        if board == state.p1board:
            fabric = self.collect_bonuses(state, state.map.player1_offset, state.map.player1_offset+how_much)
            state.map.player1_offset += how_much
            return fabric
        else:
            fabric = self.collect_bonuses(state, state.map.player2_offset, state.map.player2_offset+how_much)
            state.map.player2_offset += how_much
            return fabric


class PickAndPlaceMove(Move):
    def __init__(self, piece: Piece, position: tuple, rotation: int, flip: bool, extra_fabric_position: tuple=None):
        self.piece = piece
        self.position = position
        self.rotation = rotation
        self.flip = flip
        self.extra_fabric_position = extra_fabric_position

    def apply(self, state: State):
        board = state.current_board
        if not self.verify(state):
            raise ValueError("This move cannot be made")

        pieces_names = [piece.name for piece in state.map.pieces]
        off = pieces_names.index(self.piece.name)
        state.map.pointer_offset = off
        del state.map.pieces[off]

        board.buttons -= self.piece.price
        board.buttons_on_board += self.piece.buttons
        fabric = self.move_fields(state, self.piece.moves)

        layout = self.piece.layout.copy()
        if self.flip:
            layout = np.flip(layout)

        layout = np.rot90(layout, k=-self.rotation)

        x, y = self.position
        width, height = layout.shape

        for i_layout, i in enumerate(range(x, x+width)):
            for j_layout, j in enumerate(range(y, y+height)):
                if layout[i_layout, j_layout] == 1:
                    if board.board[i, j] == 1:
                        raise ValueError("You can not put a piece there")

                    board.board[i, j] = 1

        if fabric:
            if self.extra_fabric_position is None:
                print("Warning: You have to define fabric position in this move!")
            else:
                if state.current_board.board[self.extra_fabric_position] == 1:
                    raise ValueError("Cant put fabric here")
                extra_x, extra_y = self.extra_fabric_position
                state.current_board.board[extra_x, extra_y] = 1

    def verify(self, state: State) -> bool:
        board = state.current_board
        if board.buttons < self.piece.price:
            print("biedak")
            return False

        layout = np.rot90(self.piece.layout, k=-self.rotation)

        x, y = self.position
        width, height = layout.shape

        right_boundary = x + width
        down_boundary = y + height

        if right_boundary > state.current_board.size:
            print("out of bounds width")
            return False

        if down_boundary > state.current_board.size:
            print("out of bounds height")
            return False

        if self.extra_fabric_position:
            extra_x, extra_y = self.extra_fabric_position
            if board.board[extra_x, extra_y] == 1:
                print("fabric")
                return False

        for i_layout, i in enumerate(range(x, right_boundary)):
            for j_layout, j in enumerate(range(y, down_boundary)):
                if layout[i_layout, j_layout] == 1:
                    if board.board[i, j] == 1:
                        print("overlap")
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
            buttons_bonus = other_players_offset - my_offset
            board.buttons += buttons_bonus

            # perform jump
            state.map.player1_offset = other_players_offset+1
        else:
            my_offset = state.map.player2_offset
            other_players_offset = state.map.player1_offset

            buttons_bonus = other_players_offset - my_offset
            board.buttons += buttons_bonus

            # perform jump
            state.map.player2_offset = other_players_offset+1

    def verify(self, state: State) -> bool:
        return True



