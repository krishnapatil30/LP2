import heapq

def dijkstra(graph, start):
    # Priority queue (min-heap)
    pq = []
    heapq.heappush(pq, (0, start))

    # Distance dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            # Greedy relaxation step
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances


# Example graph
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

# Run
result = dijkstra(graph, 'A')

print("Shortest distances from A:")
for node in result:
    print(node, "=", result[node])