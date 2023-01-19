"""
@author: TMartin
@edit IM


"""

import re  # library for regular expression operations
import pandas as pd
import networkx as nx  # library for graphs (that have nodes & edges) or networks
import csv
import matplotlib.pyplot as plt


def create_tree(node_list):
    df = pd.DataFrame(node_list, columns=['City1', 'City2', 'cost'])
    G = nx.from_pandas_edgelist(df, 'City1', 'City2', edge_attr='cost')

    return G  # a graph object from the networkx library


class Node(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name


class Search(Node):
    """
    A Python class to implement various search procedures, such as BFS.
    """

    def __init__(self):
        self.visited = []  # the list of nodes that have been visited thus far
        self.queue = []  # a First-In-First-Out (FIFO) queue
        self.weightedQueue = {}  # a weighted queue for priorities (currently not used)
        self.newNodes = []  # (currently not used)
        self.neighborL = []
        self.return_path = []

    def bfs(self, startCity, goalCity, G):
        """
        Breadth-First Search (BFS).
        """
        self.queue.append(startCity)
        self.startCity = str(startCity)
        self.neighborList = (G.adj[startCity])
        while self.queue:
            node = self.queue.pop(0)
            self.visited.append(node)
            nList = self.getNeighbor(node)
            if (node == goalCity):
                print("Found:", goalCity, "")
                print("These are visited nodes\n >>>", self.visited, "\n")

                self.return_path.append(goalCity)
                break
            else:
                for neighbor in nList:
                    if neighbor not in self.visited and neighbor not in self.queue:
                        self.queue.append(neighbor)

    def getNeighbor(self, CurrNode):
        """
        A class method that returns a list of nodes that are the neighbor,
        or adjacent, to the given current node.
        """
        new_nodes = []
        inpt = str(CurrNode)
        neighbor = list(G.adj[inpt])  # find all the nodes adjacent to the current node
        for n in neighbor:
            if n not in self.queue:  # if the neighbor isn't already waiting in the queue
                if n not in self.visited:  # ... and if we haven't already visited it
                    new_nodes.append(n)  # then add it to the list of "new nodes"

        newNeighbor = new_nodes
        self.neighborL.append(new_nodes)
        return newNeighbor


def callingSearch(startCity, goalCity, typeOfSearch, G):
    g = Search()
    if typeOfSearch == "bfs":
        g.bfs(startCity, goalCity, G)

def import_csv(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

if __name__ == "__main__":
    in_file = "data.csv"

    StartCity = "SITE1"
    GoalCity = "SITE5"
    type_of_search = "bfs"

    road_list = import_csv(in_file)

    G = create_tree(road_list)

    print("Starting Node: " + StartCity)
    callingSearch(StartCity, GoalCity, type_of_search, G)

    G = nx.Graph(G)
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw(G, pos,with_labels=True)
    plt.axis('off')
    plt.show()