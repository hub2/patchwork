import numpy as np


class Piece:
    def __init__(self, name, price, moves, buttons, layout):
        self.name = name
        self.moves = moves
        self.price = price
        self.buttons = buttons

        width = len(layout[0])
        height = len(layout)
        self.layout = np.zeros((width, height))
        for i in range(width):
            for j in range(height):
                if layout[j][i] == "#":
                    self.layout[i, j] = 1

    def to_dict(self):
        return {
            "name": self.name,
            "moves": self.moves,
            "price": self.price,
            "buttons": self.buttons,
            "layout": self.layout.tolist()
        }

    def copy(self):
        return Piece(self.name, self.moves, self.price, self.buttons, np.copy(self.layout))
