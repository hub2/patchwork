from consts import BOARD_SIZE, STARTING_BUTTONS
import numpy as np


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((self.size, self.size))
        self.buttons = STARTING_BUTTONS
        self.buttons_on_board = 0

    def show(self):
        print(self.board)

    def to_dict(self):
        return {
            "size": self.size,
            "board": self.board.tolist(),
            "buttons": self.buttons,
            "buttons_on_board": self.buttons_on_board
        }
