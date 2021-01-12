from typing import List, Optional

BOARD = [[], [], [],
         [], [], [],
         [], [], [],]

class tic-tac-toe:
    """

    """
    board: List[Optional[str, List[str]]]
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
        :return:  Y if subscript is even, otherwise return X
        """
        if self.subscript % 2 == 0:
            return self.Y
        else:
            return self.X

    def check_winner(self):
        """
        Checks if there is a winning position by looking at the row and columns
        :return: the mark piece of either X or O if it satisfy a winning condition. Otherwise return None
        """
        # Horizontals
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        # Verticals
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        # Diagonals
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        else:
            return None


    def entangle(self):
        """

        :return:
        """

    def place_piece(self, row, col):
        self.subscript += 1
        self.mark_counter += 1







