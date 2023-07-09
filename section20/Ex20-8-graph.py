'''

그래프(Graph)
    노드(vertice)와 간선(정점/edge/arcs)로
    이루어진 자료구조
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for vertex in vertices:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end=' -> ')
            print(' -> '.join(str(node) for node in self.adj_list[vertex]))

#실행코드
vertices = ['A','B','C','D','E']
graph = Graph(vertices)
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('B','D')
graph.add_edge('A','E')
graph.add_edge('C','D')

graph.print_graph()