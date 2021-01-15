from typing import List, Optional
from Graph import Graph

BOARD = [[], [], [],
         [], [], [],
         [], [], []]


class TicTacToe:
    """
    Creates a game of Quantum Tic-Tac-Toe
    """
    # board: List[Optional[str, List[str]]]
    X: str
    O: str
    subscript: int
    mark_pos: List[int]
    mark_counter: int
    graph: Graph
    num_class_moves: int

    def __init__(self):
        self.board = BOARD
        self.X = "X"
        self.O = "O"
        self.graph = Graph()
        self.subscript = 1
        self.mark_pos = []
        self.mark_counter = 0

    def whose_turn(self):
        """
        Checks whose turn it is by seeing if the subscript is even or odd
        :return:  O if subscript is even, otherwise return X
        """
        if self.subscript % 2 == 0:
            return self.O
        else:
            return self.X

    def check_winner(self):
        """
        Checks if there is a winning position by looking at the row and columns
        :return: the mark piece of either X or O if it satisfy a winning condition. Otherwise return None
        """
        wins = {"X": 0, "O": 0}
        marks = {"X": [], "O": []}
        # Checks which subscript is the largest for a comparision, if the other player gets a classical win
        # Horizontals
        if self.checks_str(0, 1, 2) and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            marks[self.board[0][0]].append(max(self.board[0][1], self.board[1][1], self.board[2][1]))
        if self.checks_str(3, 4, 5) and self.board[3][0] == self.board[4][0] == self.board[5][0]:
            marks[self.board[3][0]].append(max(self.board[3][1], self.board[4][1], self.board[5][1]))
        if self.checks_str(6, 7, 8) and self.board[6][0] == self.board[7][0] == self.board[8][0]:
            marks[self.board[6][0]].append(max(self.board[6][1], self.board[7][1], self.board[8][1]))
        # Verticals
        if self.checks_str(0, 3, 6) and self.board[0][0] == self.board[3][0] == self.board[6][0]:
            marks[self.board[0][0]].append(max(self.board[0][1], self.board[3][1], self.board[6][1]))
        if self.checks_str(1, 4, 7) and self.board[1][0] == self.board[4][0] == self.board[7][0]:
            marks[self.board[1][0]].append(max(self.board[1][1], self.board[4][1], self.board[7][1]))
        if self.checks_str(2, 5, 8) and self.board[2][0] == self.board[5][0] == self.board[8][0]:
            marks[self.board[2][0]].append(max(self.board[2][1], self.board[5][1], self.board[8][1]))
        # Diagonals
        if self.checks_str(0, 4, 8) and self.board[0][0] == self.board[4][0] == self.board[8][0]:
            marks[self.board[0][0]].append(max(self.board[0][1], self.board[4][1], self.board[8][1]))
        if self.checks_str(2, 4, 6) and self.board[2][0] == self.board[4][0] == self.board[6][0]:
            marks[self.board[2][0]].append(max(self.board[2][1], self.board[4][1], self.board[6][1]))

        x = marks["X"]
        o = marks["O"]
        num_x = len(x)
        num_o = len(o)
        num_compare = len(x)
        x.sort()
        o.sort()

        if num_x > num_o:
            num_compare = num_x - num_o
            wins["X"] += num_compare
        elif num_x < num_o:
            num_compare = num_o - num_x
            wins["O"] += num_compare
        for i in range(num_compare):
            if x[i] < o[i]:
                wins["X"] += 1
                wins["O"] += 0.5
            else:
                wins["O"] += 1
                wins["X"] += 0.5

        return wins

    def checks_str(self, one: int, two: int, three: int):
        """
        Checks if all the positions are type str. If it is all str,
        then return True otherwise return False
        :return:
        """
        return type(self.board[one]) == str and type(self.board[two]) == str and \
               type(self.board[three]) == str

    def entangle(self):
        '''
        Returns a list of boxes that are eligible for collapse
        iff there is a cyclic entanglement. Otherwise returns
        an empty list.

        :return: list boxes involved in cyclic entanglement eligible for collapse
        '''
        cycle = self.graph.cyclicEntanglement()
        boxes = []
        for edge in cycle:
            if edge[0] not in cycle:
                boxes.append(edge[0])
            if edge[1] not in cycle:
                boxes.append(edge[1])
        return boxes

    def collapse(self, box: int):
        '''
        Collapses all the boxes related to the cyclic entanglement
        into classical tictactoe boxes

        :param box: which box was chosen by player to start collapse
        :return: a dictionary mapping each box to a counter with subscripts
        '''
        return self.graph.collapse(box)

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
                self.mark_pos.append(position)
                self.mark_counter += 1
                if self.mark_counter == 2:
                    self.mark_counter = 0
                    self.subscript += 1
                    self.graph.addEdge(self.mark_pos.pop(0), self.mark_pos.pop(0))
                print(self.board)
                return mark
        return "F"

    def reset(self):
        self.board = BOARD
        self.subscript = 1
        self.mark_counter = 0
        self.subscript += 1
        self.mark_counter += 1
