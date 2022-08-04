# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Create Graph
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Graph:
    def __init__(self, vertices):
        self.map = {}
        self.vertices = vertices
        for i in range(self.vertices):
            self.map[i]=[]

    def add_edge(self, u, v):
        self.map[u].append(v)
        self.map[v].append(u)

    def prit_graph(self):
        for i in range(self.vertices):
            print(i, '--->---: ', self.map[i])


if __name__ == '__main__':
    g = Graph(6)
    print(g.map)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.prit_graph()
