from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, stack_member, st):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        st.append(u)

        for v in self.graph[u]:
            if v not in disc:
                self.SCCUtil(v, low, disc, stack_member, st)
                low[u] = min(low[u], low[v])
            elif stack_member[v] == True:
                low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=' ')
                stack_member[w] = False
            print()

    def SCC(self):
        disc = {}
        low = {}
        stack_member = defaultdict(lambda: False)
        st = []
        count = 0 # counter for SCCs

        for i in list(self.graph.keys()):  # Create a list from keys
            if i not in disc:
                self.SCCUtil(i, low, disc, stack_member, st)
                count += 1 # increment the counter for each SCC

        return count

# Create a graph
g1 = Graph()
g1.add_edge('b', 'a')
g1.add_edge('b', 'f')
g1.add_edge('b', 'c')
g1.add_edge('c', 'g')
g1.add_edge('c', 'd')
g1.add_edge('d', 'h')
g1.add_edge('e', 'i')
g1.add_edge('e', 'd')
g1.add_edge('f', 'a')
g1.add_edge('g', 'b')
g1.add_edge('g', 'f')
g1.add_edge('h', 'c')
g1.add_edge('i', 'd')
g1.add_edge('i', 'h')
<<<<<<< HEAD
g1.add_edge('a','e')
print("Strongly connected components in the graph are:")
=======
print("Strongly connected components in the graph are - Each line is a strongly connected component:")
>>>>>>> a6ee31e5b95958fbbeb6cf10248279b3da99ef86
SCC_count = g1.SCC()