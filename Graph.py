#This takes inspiration from the idea demonstrated in https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

from typing import Tuple, List

'''
Graph keeps track of all the edges that 
are present in the graph and checks the presence of 
a cycle in the graph.
'''


class Graph():
    def __init__(self):
        self.visited = []
        self.edges = []

    def addEdge(self, x: int, y:int):
        '''
        Adds coord to the list of edges
        present in the Graph. Each edge will always
        have the lower vertice first.
        :param coord: The edge that has to be added
        to the Graph
        :return:
        '''
        if x > y:
            self.edges.append((y,x))
        else:
            self.edges.append((x,y))

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
        self.addVisited(major)
        v1,v2 = major
        for edge in self.edges:
            if edge not in self.visited:
                if v1 == edge[0] or v2 == edge[0]:
                    neighbors.append((edge,1))
                elif v1 == edge[1] or v2 == edge[1]:
                    neighbors.append((edge,0))
        return neighbors

    def cyclicEntanglement(self):
        '''
        Checks to see if there is a cycle in the
        Graph. If there is a cycle it returns a list
        with the edges that make the cycle, else it returns an
        empty list.
        :return: list of edges that make the cycle
        '''
        for coord in self.edges:
            stack = self.neighbors(coord)
            found = False
            points = [coord]
            while len(stack) > 0 and found == False:
                neighbor,compare = stack.pop(0)
                points.append(neighbor)
                if neighbor[compare] == coord[0] or neighbor[compare]== coord[1]:
                    found = True
                else:
                    more_neighbors = self.neighbors(neighbor)
                    for n in more_neighbors:
                        stack.insert(0, n)
                    if len(more_neighbors) == 0:
                        points = [coord]
            if found:
                return points
            self.clearVisited()
        return []

    def removeDuplicates(self):
        temp = []
        for edge in self.edges:
            if edge in temp:
                pass
            else:
                temp.append(edge)
        self.edges = temp

def equals(one:tuple,two:tuple):
    return one==two or (one[1] == two[0] and one[0] == two[1])

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 5)
    g.addEdge(0, 2)
    g.addEdge(2, 5)
    #g.addEdge(4, 1)
    print(g.cyclicEntanglement())
