from queue import PriorityQueue

# Graph (Romania map - distances in km)
graph = {
    'Arad':      {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind':    {'Arad': 75, 'Oradea': 71},
    'Oradea':    {'Zerind': 71, 'Sibiu': 151},
    'Sibiu':     {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj':     {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia':   {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta':   {'Mehadia': 75, 'Craiova': 120},
    'Craiova':   {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu':   {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras':   {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti':   {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {}
}

# Heuristic - straight line distance to Bucharest
heuristic = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253,
    'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
    'Craiova': 160, 'Rimnicu': 193, 'Fagaras': 176,
    'Pitesti': 100, 'Bucharest': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g_cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        _, current = pq.get()

        if current == goal:
            break

        for neighbour in graph[current]:
            new_cost = g_cost[current] + graph[current][neighbour]

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                f_cost = new_cost + heuristic[neighbour]
                pq.put((f_cost, neighbour))
                parent[neighbour] = current

    # Path reconstruct करतो
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, g_cost[goal]

# Run करा
path, cost = a_star('Arad', 'Bucharest')
print("Path:", " -> ".join(path))
print("Total Cost:", cost)

# Output: Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
# Total Cost: 418