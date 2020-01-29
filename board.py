from consts import BOARD_SIZE, STARTING_BUTTONS
import numpy as np


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((self.size, self.size))
        self.buttons = STARTING_BUTTONS
        self.buttons_on_board = 0
        self.has_bonus = False

    def show(self):
        print(self.board)

    def to_dict(self):
        return {
            "size": self.size,
            "board": self.board.tolist(),
            "buttons": self.buttons,
            "buttons_on_board": self.buttons_on_board,
            "has_bonus": self.has_bonus
        }

    def copy(self):
        new_b = Board()
        new_b.size = self.size
        new_b.board = np.copy(self.board)
        new_b.buttons_on_board = self.buttons_on_board
        new_b.buttons = self.buttons
        new_b.has_bonus = self.has_bonus

        return new_b
