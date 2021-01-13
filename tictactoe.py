from typing import List, Optional

BOARD = [[], [], [],
         [], [], [],
         [], [], []]


class TicTacToe:
    """

    """
    board: List[Optional[str, List[str]]]
    X: str
    Y: str
    subscript: int
    mark_counter: int
    x_wins: int
    y_wins: int

    def __init__(self):
        self.board = BOARD
        self.X = "X"
        self.Y = "Y"
        self.subscript = 1
        self.mark_counter = 0
        self.x_wins = 0
        self.y_wins = 0

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
        wins = {"X": 0, "Y": 0}
        # Horizontals
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            wins[self.board[0][0]] += 1
        if self.board[3][0] == self.board[4][0] == self.board[5][0]:
            wins[self.board[3][0]] += 1
        if self.board[6][0] == self.board[7][0] == self.board[8][0]:
            wins[self.board[6][0]] += 1
        # Verticals
        if self.board[0][0] == self.board[3][0] == self.board[6][0]:
            wins[self.board[0][0]] += 1
        if self.board[1][0] == self.board[4][0] == self.board[7][0]:
            wins[self.board[1][0]] += 1
        if self.board[2][0] == self.board[5][0] == self.board[8][0]:
            wins[self.board[2][0]] += 1
        # Diagonals
        if self.board[0][0] == self.board[4][0] == self.board[8][0]:
            wins[self.board[0][0]] += 1
        if self.board[2][0] == self.board[4][0] == self.board[6][0]:
            wins[self.board[2][0]] += 1
        return wins

    def entangle(self):
        """

        :return:
        """

    def place_piece(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3:
            if type(self.board[row][col]) != str:
                self.board[row][col].append(self.whose_turn() + str(self.subscript))
                self.subscript += 1
                self.mark_counter += 1

    def reset(self):
        self.board = BOARD
        self.subscript = 1
        self.mark_counter = 0
