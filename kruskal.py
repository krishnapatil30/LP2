# Kruskal's Algorithm

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
    edges.sort(key=lambda x: x[2])   # sort by weight

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


# Example graph (u, v, weight)
edges = [
    (0, 1, 9),
    (0, 2, 75),
    (1, 2, 95),
    (1, 3, 19),
    (1, 4, 42),
    (2, 3, 51),
    (2, 4, 66),
    (3, 4, 31)
]

mst, cost = kruskal(5, edges)

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

print("Total Cost:", cost)