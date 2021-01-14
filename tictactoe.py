from typing import List, Optional

BOARD = [[], [], [],
         [], [], [],
         [], [], []]


class TicTacToe:
    """
    Creates a game of Quantum Tic-Tac-Toe
    """
    # board: List[Optional[str, List[str]]]
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

    def collapse(self, edges):
        pass

    def place_piece(self, position):
        """
        Places down a mark on the grid
        :param position: The position the player wants to place a mark in the grid.
        :return:
        """
        mark = self.whose_turn() + str(self.subscript)
        if 0 <= position <= 8 and mark not in self.board[position]:
            if type(self.board[position]) != str:
                self.board[position].append(mark)
                self.mark_counter += 1
                if self.mark_counter == 2:
                    self.mark_counter = 0
                    self.subscript += 1
                print(self.board)
                return mark
        return "F"

    def reset(self):
        self.board = BOARD
        self.subscript = 1
        self.mark_counter = 0
        self.subscript += 1
        self.mark_counter += 1
