from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = []
        self.node_map = defaultdict(int)

    def add_node(self, node):
        if node not in self.node_map:
            self.node_map[node] = len(self.node_map)

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph.sort(key=lambda item: item[2])
        parent = {}
        rank = {}
        for node in self.node_map:
            parent[node] = node
            rank[node] = 0
        while e < len(self.node_map) - 1:
            u, v, w = self.graph[i]
            i += 1
            print(f"Checking edge {u} - {v}")
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        print("Edges in the minimum spanning tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

g = Graph()
for node in ['A', 'B', 'C', 'D','E','F','G','H','I']:
    g.add_node(node)
g.add_edge('A', 'B', 4)
g.add_edge('A', 'F', 3)
g.add_edge('F', 'B', 5)
g.add_edge('F', 'G', 8)
g.add_edge('G', 'C', 6)
g.add_edge('B', 'C', 1)
g.add_edge('C', 'H', 9)
g.add_edge('H', 'D', 6)
g.add_edge('D', 'I', 7)
g.add_edge('I', 'E', 1)
g.add_edge('D', 'E', 7)

g.kruskal()
print("Sammenlig -Checking edge- med -edges in the minium spanning tree- den første som ikke er med -spanning tree- er svaret")