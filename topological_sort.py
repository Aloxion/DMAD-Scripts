from collections import defaultdict

class Graph:
    def __init__(self, letters):
        self.letters = letters
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.letter_map = {letter: index for index, letter in enumerate(letters)}

    def add_edge(self, u, v):
        self.graph[self.letter_map[u]].append(self.letter_map[v])

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = [False]*len(self.letters)
        stack = []

        for i in range(len(self.letters)):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print([self.letters[i] for i in stack])  # convert numeric indices back to letters

# Create a graph
g = Graph(['a', 'b', 'c', 'd', 'e', 'f'])
g.add_edge('b', 'd')
g.add_edge('b', 'a')
g.add_edge('b', 'e')
g.add_edge('b', 'c')
g.add_edge('d', 'a')
g.add_edge('d', 'e')
g.add_edge('c', 'e')
g.add_edge('f', 'e')
g.add_edge('f', 'c')

print("Topological Sort:")
g.topological_sort()
