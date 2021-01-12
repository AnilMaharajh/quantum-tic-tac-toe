from typing import List
BOARD = [[], [], [],
         [], [], [],
         [], [], [],]

class tic-tac-toe:
    """

    """
    board: List[List[List]]
    X: str
    Y: str
    subscript: int
    mark_counter: int
    def __init__(self):
        self.board = BOARD
        self.X = "X"
        self.Y = "Y"
        self.subscript = 1
        self.mark_counter = 0
    def whose_turn(self):
        """
        Checks whose turn it is by seeing if the subscript is even or odd
        return Y if subscript is even, otherwise return X
        """
        if self.subscript % 2 == 0:
            return self.Y
        else:
            return self.X

    def check_winner(self):

    def entangle(self):

    def place_piece(self):
        self.subscript += 1:
        self.mark_counter += 1:







