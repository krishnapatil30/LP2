import heapq

# -------------------------------
# 1. Selection Sort (Greedy)
# -------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# -------------------------------
# 2. Job Scheduling (Greedy)
# -------------------------------
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    slots = [-1] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for j in range(deadline, 0, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                break

    return slots[1:], total_profit


# -------------------------------
# 3. Prim’s MST (Greedy)
# -------------------------------
def prim(graph, N):
    INF = 9999999
    selected = [False] * N
    selected[0] = True

    total_cost = 0
    edges = []

    for _ in range(N - 1):
        minimum = INF
        x = y = 0

        for i in range(N):
            if selected[i]:
                for j in range(N):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j

        edges.append((x, y, graph[x][y]))
        total_cost += graph[x][y]
        selected[y] = True

    return edges, total_cost


# -------------------------------
# 4. Kruskal’s MST (Greedy)
# -------------------------------
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(V)]
    rank = [0] * V

    mst = []
    total_cost = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            total_cost += w

    return mst, total_cost


# -------------------------------
# 5. Dijkstra (Greedy)
# -------------------------------
def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances


# ===============================
# 🔹 DRIVER CODE (Run All)
# ===============================
if __name__ == "__main__":

    # Selection Sort
    print("Selection Sort:")
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))

    # Job Scheduling
    print("\nJob Scheduling:")
    jobs = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27),
            ('J4', 1, 25), ('J5', 3, 15)]
    schedule, profit = job_scheduling(jobs)
    print("Jobs:", schedule)
    print("Profit:", profit)

    # Prim’s MST
    print("\nPrim’s MST:")
    G = [
        [0, 9, 75, 0, 0],
        [9, 0, 95, 19, 42],
        [75, 95, 0, 51, 66],
        [0, 19, 51, 0, 31],
        [0, 42, 66, 31, 0]
    ]
    edges, cost = prim(G, 5)
    print("Edges:", edges)
    print("Cost:", cost)

    # Kruskal MST
    print("\nKruskal MST:")
    edge_list = [
        (0, 1, 9), (0, 2, 75), (1, 2, 95),
        (1, 3, 19), (1, 4, 42),
        (2, 3, 51), (2, 4, 66), (3, 4, 31)
    ]
    mst, cost = kruskal(5, edge_list)
    print("Edges:", mst)
    print("Cost:", cost)

    # Dijkstra
    print("\nDijkstra:")
    graph = {
        'A': {'B': 4, 'C': 1},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    print(dijkstra(graph, 'A'))