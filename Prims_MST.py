import heapq
from collections import defaultdict

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    last_node = None

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))

            last_node = to

    return mst, last_node

if __name__ == "__main__":
    # Define the graph
    graph = {
        'A': {'H': 12, 'G': 5, 'D': 9, 'F': 3},
        'H': {'A': 12, 'G': 7},
        'G': {'A': 5, 'H': 7, 'D': 3},
        'D': {'A': 9, 'G': 3, 'F': 4},
        'F': {'A': 3, 'D': 4, 'E': 1, 'C': 6},
        'E': {'F': 1, 'I': 8, 'C': 11},
        'I': {'E': 8, 'B': 10, 'C': 13},
        'B': {'I': 10, 'C': 2},
        'C': {'F': 6, 'B': 2, 'I': 13, 'E': 11},
    }

    # Find the MST
    mst, last_node = create_spanning_tree(graph, 'A')
    total_cost = 0
    for node, edges in mst.items():
        for edge in edges:
            total_cost += graph[node][edge]

    print("Edges in the minimum spanning tree:")
    for node, edges in mst.items():
        print(f"{node} connected with {', '.join(edges)}")
        
    print("Total weight of the minimum spanning tree:", total_cost)
    print("Last node added to the MST:", last_node)
