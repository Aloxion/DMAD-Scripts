import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    visited = {start: 0}
    relax_count = 1
    while queue:
        (dist, current) = heapq.heappop(queue)
        print(f"Node removed from the list: {current}")
        for neighbor, neighbor_dist in graph[current].items():
            old_cost = visited.get(neighbor, float('inf'))
            new_cost = dist + neighbor_dist
            if new_cost < old_cost:
                visited[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
                relax_count += 1
    print(f"Relax operation was used {relax_count} times.")
    return visited

# Define the graph
graph = {
    'A': {'B': 4, 'G': 7},
    'B': {'C': 1, 'D': 2},
    'C': {'A': 2, 'F': 6},
    'D': {'C': 1, 'D': 4},
    'E': {'C': 8},
    'F': {'E': 1},
    'G': {'C': 4, 'E': 6}
}

print(dijkstra(graph, 'A'))
