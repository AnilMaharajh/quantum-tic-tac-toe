# Inspired from Tutorials Point:
# https://www.tutorialspoint.com/python-program-for-detect-cycle-in-a-directed-graph

from typing import Tuple, Set, List

'''
Graph keeps track of all the edges that 
are present in the graph and checks the presence of 
a cycle in the graph.

'''


class Graph():
    def __init__(self):
        self.visited = []
        self.edges = []

    def addEdge(self, coord: tuple):
        '''
        Adds coord to the list of edges
        present in the Graph
        :param coord: The edge that has to be added
        to the Graph
        :return:
        '''
        if tuple not in self.edges:
            self.edges.append(coord)

    def addVisited(self, coord: tuple):
        '''
        Adds coord to the list of visited
        edges.
        :param coord: The edge that has been visited
        :return:
        '''
        self.visited.append(coord)

    def clearVisited(self):
        '''
        Removes all edges from visited
        :return: None
        '''
        self.visited = []

    def clearEdges(self):
        '''
        Removes all pre-existing edges in
        Graph
        :return: None
        '''
        self.edges = []

    def neighbors(self, major: tuple) -> List[Tuple]:
        '''
        Returns possible edges that neighbor edge
        major
        :param major: A tuple that represents an edge
        '''
        neighbors = []
        for edge in self.edges:
            if edge != major and (major[1] != edge[0] and major[0] != edge[1]):
                if edge[0] == major[0] or edge[0] == major[1]:
                    neighbors.append(edge)
                elif edge[1] == major[1] or edge[1] == major[0]:
                    neighbors.append(edge)
        return neighbors

    def cyclicEntanglement(self):
        '''
        Checks to see if there is a cycle in the
        Graph. If there is it returns True, else
        it returns False
        :return:
        '''
        for coord in self.edges:
            stack = self.neighbors(coord)
            found = False
            while len(stack) > 0 and found == False:
                neighbor = stack.pop(0)
                if neighbor in self.visited:
                    found = True
                else:
                    self.addVisited(neighbor)
                    more_neighbors = self.neighbors(neighbor)
                    for n in more_neighbors:
                        stack.insert(0, n)
            if found:
                return True
            self.clearVisited()
        return False


if __name__ == "__main__":
    g = Graph()
    g.addEdge((1, 5))
    g.addEdge((2, 4))
    g.addEdge((2, 5))
    g.addEdge((4, 1))
    print(g.cyclicEntanglement())
