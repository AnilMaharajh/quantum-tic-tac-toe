# Uses a depth-first search approach through a stack implementation to find cycle in a graph

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

    def addEdge(self, x: int, y:int, counter:str):
        '''
        Adds coord to the list of edges
        present in the Graph. Each edge will always
        have the lower vertice first.
        :param coord: The edge that has to be added
        to the Graph
        :return:
        '''
        if x > y:
            self.edges.append((y,x,counter))
        else:
            self.edges.append((x,y,counter))

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
        v1,v2,counter = major
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
                self.clearVisited()
                return points
            self.clearVisited()
        return []

    def findEdge(self,box:int):

        found = []
        for edge in self.edges:
            if edge[1] == box and edge not in self.visited:
                self.visited.append(edge)
                found.append((edge,box))
            elif edge[0] == box and edge not in self.visited:
                self.visited.append(edge)
                found.append((edge,box))
        return found

    def collapse(self,box: int):
        '''
         Collapses all the boxes related to the cyclic entanglement
        into classical tictactoe boxes

        :param box: which box was chosen by player to start collapse
        :return: a dictionary mapping each box to a counter with subscripts
        '''
        mapping = {}
        queue = self.findEdge(box)
        while queue != []:
            current, pos = queue.pop(0)
            if current[0] in mapping:
                mapping[current[1]] = current[2]
                queue.extend(self.findEdge(current[1]))
            else:
                mapping[current[0]] = current[2]
                queue.extend(self.findEdge(current[0]))

        # Remove the collapsed edges from the graph
        for edge in self.visited:
            self.edges.remove(edge)
        #Clear the visited edges
        self.clearVisited()
        return mapping

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,0,"X1")
    g.addEdge(1,0,"X2")
    g.addEdge(1,2,"Y2")
    g.addEdge(3,4,"Y3")
    print(g.cyclicEntanglement())
    print(g.collapse(1))
    print(g.edges)
