import numpy as np
import matplotlib.pyplot as plt

BOUNDS = [10, 10]
NEIGHBOURS = [[1, 0], [-1, 0], [0, 1], [0, -1]] #right, left, forward, backward.
OBSTACLES = [[1, 4], [2, 5]]
"""
    x, y
    Neighbours:
        forward Y: x, y + 1
        backeard Y: x, y - 1
        left X: x - 1, y
        right X: x + 1, y

"""

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # List of Children
        self.adjacent_nodes = []

        # parent for backtracking
        self.parent = None

        # set all the cost to infinity
        self.g = np.inf
        self.h = np.inf
        self.f = np.inf

        # self.addAdjacentNodes()

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def addAdjacentNodes(self):
        for tf in NEIGHBOURS:
            if self.x + tf[0] <= BOUNDS[0] and self.y + tf[1] <= BOUNDS[1]:
                self.adjacent_nodes.append(Node(self.x + tf[0], self.y + tf[1]))

class AStar:
    def __init__(self, start: list, goal: list):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])

    def search(self):
        self.nodes = []
        
        # Modify the start
        self.start.g = 0
        self.start.h = self.heuristic(self.start)
        self.f = self.g + self.h

        self.nodes.append(self.start)

        # Search
        while len(self.nodes) != 0:
            current = sorted(self.nodes, key= lambda node: node.f)[0]

            # For Dijkstra's
            # current = sorted(self.nodes, key= lambda node: node.f)[0]

            self.nodes.remove(current)

            if current == self.goal:
                print("Goal found")
                self.backtrack(current)
                return True
            
            self.expandNode(current)

            for child in current.adjacent_nodes:
                if child.g > current.g + self.cost(current, child):
                    child.g = current.g + self.cost(current, child)
                    child.h = self.heuristic(child)
                    child.f = child.g + child.h

                    # For Dijkstra's
                    # child.h = self.heuristic(child)
                    # child.f = child.g + child.h

                    child.parent = current

                if child not in self.nodes:
                    self.nodes.append(child)

    def expandNode(self, node: Node):
        for tf in NEIGHBOURS:
            node.adjacent_nodes.append(Node(node.x + tf[0], node.y + tf[1]))

    def cost(self, node1: Node, node2: Node)->float:
        if self.checkNodeValidity(node1) and self.checkNodeValidity(node2):
            # Euclidean dist cost
            X = node1.x - node2.x
            Y = node1.y - node2.y

            return np.sqrt(X**2 + Y**2)
        
        else :
            np.inf

    def heuristic(self, node: Node)->float:
        # Calculated wrt Goal
        # Manhattan distance

        X = node.x - self.goal.x
        Y = node.y - self.goal.y

        return abs(X) + abs(Y)

    def checkNodeValidity(self, node):
        for obst in OBSTACLES:
            if obst[0] == node.x and obst[1] == node.y:
                return False
        return True

    def backtrack(self, current):
        self.X = [current.x]
        self.Y = [current.y]

        while current.parent is not None:
            self.X.append(current.parent.x)
            self.Y.append(current.parent.y)

        return self.X, self.Y
 