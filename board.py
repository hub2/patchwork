from consts import BOARD_SIZE, STARTING_BUTTONS
import numpy as np


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((self.size, self.size))
        self.buttons = STARTING_BUTTONS
        self.button_on_board = 0

    def show(self):
        print(self.board)
