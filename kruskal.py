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
            edges.append(f"{u} - {v}")
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        print("Edges in the minimum spanning tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
            edgesInMinumum.append(f"{u} - {v}")

def compare_arrays(array1, array2):
    mismatched_values = []
    
    # Check the elements at each index
    for i in range(min(len(array1), len(array2))):
        if array1[i] != array2[i]:
            mismatched_values.append((array1[i], array2[i]))
    
    # Check if one array is longer than the other
    if len(array1) > len(array2):
        mismatched_values.extend(array1[len(array2):])
    elif len(array1) < len(array2):
        mismatched_values.extend(array2[len(array1):])
    
    return mismatched_values[0]

edges = []
edgesInMinumum = []
g = Graph()
for node in ['A', 'B', 'C', 'D','E','F','G','H']:
    g.add_node(node)
g.add_edge('A', 'C', 6)
g.add_edge('A', 'G', 9)
g.add_edge('A', 'E', 8)
g.add_edge('B', 'D', 5)
g.add_edge('B', 'H', 11)
g.add_edge('B', 'G', 3)
g.add_edge('C', 'F', 12)
g.add_edge('C', 'D', 2)
g.add_edge('D', 'G', 7)
g.add_edge('E', 'F', 0)
g.add_edge('H', 'G', 10)

g.kruskal()
print("Sammenlig -Checking edge- med -edges in the minium spanning tree- den første som IKKE er med i -spanning tree- er svaret")
notInMst = str(compare_arrays(edges,edgesInMinumum)).split(',')[0].replace('(', '')
print(notInMst, 'or', notInMst[::-1] )