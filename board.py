from consts import BOARD_SIZE, STARTING_BUTTONS
import numpy as np
from move import Move


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = np.zeros((self.size, self.size))
        self.buttons = STARTING_BUTTONS

