import abc
import numpy as np
from move import Move, PickAndPlaceMove, JumpMove
from state import State
from consts import BOARD_SIZE
from helpers import available_moves
from skimage import measure
import random

#random.seed(1)


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
            for i in range(1000):
                piece = random.choice(affordable_pieces)
                rotation = random.randrange(0, 4)
                flip = random.choice([True, False])

                position_x = random.randrange(0, BOARD_SIZE)
                position_y = random.randrange(0, BOARD_SIZE)
                position = (position_x, position_y)

                x, y = np.where(state.current_board.board == 0)

                i = random.randrange(0, len(x))
                extra_fabric_random = (x[i], x[i])

                move_to_be_made = PickAndPlaceMove(piece=piece, rotation=rotation, position=position, flip=flip,
                                                   extra_fabric_position=extra_fabric_random)
                if state.verify(move_to_be_made):
                    return move_to_be_made
            return JumpMove()
        else:
            return JumpMove()


h = []


class EducatedRandomStrategy(Strategy):
    def get_move(self, state: State) -> Move:
        from helpers import available_moves

        m = available_moves(state)
        #print(f"Buttons {state.current_board.buttons}")
        print(f"Number {len(m)}")
        h.append(len(m))
        print(f"Average moves per game: {sum(h)/len(h)}")

        move_to_do = random.choice(m)
        if isinstance(move_to_do, PickAndPlaceMove):
            print(f"Piece name: {move_to_do.piece.name}")

        return move_to_do


class AlphaBeta(Strategy):
    MINVALUE = -1000000
    MAXVALUE = 1000000

    def get_move(self, state: State) -> Move:
        from helpers import available_moves

        eval, move = self.search_outer(state)
        print(f"Evaluation: {eval}")
        return move

    def search_outer(self, state: State):
        for i in range(1,2):
            eval, move = self.search(state, i, AlphaBeta.MINVALUE, AlphaBeta.MAXVALUE)

        return eval, move

    def search(self, state: State, depth: int, alpha: float, beta: float):
        if depth == 0:
            return self.eval(state), None

        moves = available_moves(state)
        #print(f"Moves: {len(moves)}")
        value_max = AlphaBeta.MINVALUE
        best_move = None

        for move in moves:
            state_copy = state.copy()
            state_copy.apply(move)
            value, _ = self.search(state_copy, depth-1, -beta, -alpha)
            value = -value
            value = max(alpha, value)
            alpha = max(alpha, value)
            if value > value_max:
                value_max = value
                best_move = move
            if alpha >= beta:
                break

        return value_max, best_move

    def eval(self, state: State):
        multiplier = 1
        if state.current_board == state.p1board:
            multiplier = -1

        eval = 0

        for (board, multiplier, offset) in [(state.p1board, 1, state.map.player1_offset), (state.p2board, -1, state.map.player2_offset)]:
            labeled = measure.label(board.board-1, connectivity=1)
            no_classes = np.max(labeled)+1

            #bboxes = [area.bbox for area in measure.regionprops(labeled)]

            #print(f"Labeled: {no_classes} {labeled}")
            if state.current_board.has_bonus:
                eval += 7 * multiplier
            eval += (board.buttons - 2*len(np.where(board.board == 0)[0]) - no_classes*0.1 - offset*0.005 + board.buttons_on_board*0.1) * multiplier

        return eval * multiplier



