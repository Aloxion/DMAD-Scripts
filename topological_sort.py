from collections import defaultdict

class Graph:
    def __init__(self, letters):
        self.letters = letters
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.letter_map = {letter: index for index, letter in enumerate(letters)}
        self.reverse_map = {index: letter for index, letter in enumerate(letters)}
        self.visited = [False]*len(self.letters)
        self.in_degree = {i: 0 for i in range(len(self.letters))}

    def add_edge(self, u, v):
        self.graph[self.letter_map[u]].append(self.letter_map[v])
        self.in_degree[self.letter_map[v]] += 1

    def all_topological_sorts(self, stack):
        flag = False

        for i in range(len(self.letters)):
            if self.in_degree[i] == 0 and not self.visited[i]:
                self.visited[i] = True
                stack.append(self.reverse_map[i])
                for node in self.graph[i]:
                    self.in_degree[node] -= 1

                self.all_topological_sorts(stack)

                for node in self.graph[i]:
                    self.in_degree[node] += 1
                stack.pop()
                self.visited[i] = False
                flag = True

        if not flag:
            print(' '.join(stack))

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

print("All possible Topological Sorts:")
g.all_topological_sorts([])
