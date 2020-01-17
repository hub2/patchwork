from piece import Piece

pieces_types = [
Piece("2x1 line (starting Piece)", 2, 1, 0, ["##"]),
Piece("3x1 line", 2, 2, 0, ["###"]),
Piece("4x1 line", 3, 3, 1, ["####"]),
Piece("5x1 line", 7, 1, 1, ["#####"]),
Piece("2x2 square", 6, 5, 2,
      ["##",
       "##"]),
Piece("2x2 square (one stick out variant)", 2, 2, 0,
      ["## ",
       "###"]),

Piece("2x2 square (two stick out variant)", 10, 5, 3,
      [
          "##  ",
          "####"
      ]),

Piece("2x2 square (one stick out each side variant)", 7, 4, 2,
      [
          " ## ",
          "####"
      ]),

Piece("2x2 square (one stick out each side alternating variant)", 4, 2, 0,
      [
          "### ",
          " ###"
      ]),

Piece("2x2 square (two under sideways variant)", 8, 6, 3,
      [
          " ##",
          " ##",
          "## "
      ]),

Piece("u", 1, 2, 0,
      [
          "# #",
          "###"
      ]),

Piece("u (wide variant)", 1, 5, 1,

      [
          "#  #",
          "####"
      ]),

Piece("Y", 3, 6, 2,
      [
          "# #",
          "###",
          " # "
      ]),

Piece("small T (1)", 2, 2, 0,
      [
          "###",
          " # "
      ]),

Piece("medium T (2)", 5, 5, 2,
      [
          "###",
          " # ",
          " # "
      ]),

Piece("long T (3)", 7, 2, 2,
      [
          "###",
          " # ",
          " # ",
          " # "
      ]),

Piece("free cross (medium t (2) with a double top)", 0, 3, 1,
      [
          " # ",
          "###",
          " # ",
          " # "
      ]),

Piece("L (low cost variant)", 4, 2, 1,
      [
          "# ",
          "# ",
          "##"
      ]),

Piece("L (high cost variant)", 4, 6, 2,
      [
          "# ",
          "# ",
          "##"
      ]),

Piece("L (long variant)", 10, 3, 2,
      [
          "# ",
          "# ",
          "# ",
          "##"
      ]),

Piece("L (one extra same line variant)", 3, 4, 1,
      [
          "# ",
          "# ",
          "##",
          "# "
      ]),

Piece("+", 5, 4, 2,
      [
          " # ",
          "###",
          " # "
      ]),

Piece("+ (long variant)", 1, 4, 1,
      [
          " # ",
          " # ",
          "###",
          " # ",
          " # "
      ]),

Piece("+ (double width variant)", 5, 3, 1,
      [
          " ## ",
          "####",
          " ## "
      ]),

Piece("H", 2, 3, 0,
      [
          "# #",
          "###",
          "# #"
      ]),

Piece("corner (button variant)", 3, 1, 0,
      [
          " #",
          "##"
      ]),

Piece("corner (time variant)", 1, 3, 0,
      [
          " #",
          "##"
      ]),

Piece("s (cheap variant)", 3, 2, 1,
      [
          " #",
          "##",
          "# "
      ]),

Piece("s (expensive variant)", 7, 6, 3,
      [
          " #",
          "##",
          "# "
      ]),

Piece("s (long variant)", 2, 3, 1,
      [
          " #",
          " #",
          "##",
          "# "
      ]),

Piece("s (wide variant)", 1, 2, 0,
      [
          "   #",
          "####",
          "#   "
      ]),

Piece("s (wings variant)", 2, 1, 0,
      [
          "  # ",
          "####",
          " #  "
      ]),

Piece("w", 10, 4, 3,
      [
          "  #",
          " ##",
          "## "
      ])]
