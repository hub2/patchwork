import abc
import numpy as np
from move import Move, PickAndPlaceMove, JumpMove
from state import State
from consts import BOARD_SIZE
import random

random.seed(1)


class Strategy:
    @abc.abstractmethod
    def get_move(self, state: State) -> Move:
        pass


class RandomStrategy(Strategy):
    def get_move(self, state: State) -> Move:
        move_to_do = random.choice([PickAndPlaceMove, JumpMove])
        available_pieces = state.map.available_pieces()
        affordable_pieces = [piece for piece in available_pieces if piece.price <= state.current_board.buttons]
        print(affordable_pieces)
        if PickAndPlaceMove == move_to_do and len(affordable_pieces) > 0:
            for i in range(10000):
                piece = random.choice(affordable_pieces)
                rotation = random.randrange(0, 4)

                position_x = random.randrange(0, BOARD_SIZE)
                position_y = random.randrange(0, BOARD_SIZE)
                position = (position_x, position_y)

                x, y = np.where(state.current_board.board == 0)

                i = random.randrange(0, len(x))
                extra_fabric_random = (x[i], x[i])

                move_to_be_made = PickAndPlaceMove(piece=piece, rotation=rotation, position=position,
                                                   extra_fabric_position=extra_fabric_random)
                if state.verify(move_to_be_made):
                    return move_to_be_made
            return JumpMove()
        else:
            return JumpMove()
