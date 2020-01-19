import numpy as np


class Piece:
    def __init__(self, name, moves, price, buttons, layout):
        self.name = name
        self.moves = moves
        self.price = price
        self.buttons = buttons

        width = len(layout[0])
        height = len(layout)
        self.layout = np.zeros((width, height))
        for i in range(width):
            for j in range(height):
                self.layout[i, j] = 1

    def to_dict(self):
        return {
            "name": self.name,
            "moves": self.moves,
            "price": self.price,
            "buttons": self.buttons,
            "layout": self.layout.tolist()
        }
