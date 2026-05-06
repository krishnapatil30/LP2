INF = 9999999

# Number of vertices
N = 5

# Adjacency matrix
G = [
    [0, 9, 75,  0,  0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51,  0, 31],
    [0, 42, 66, 31,  0]
]

selected = [False] * N

# Node 0 पासून सुरुवात
selected[0] = True

print("Edge : Weight")

total_cost = 0

for _ in range(N - 1):      # N-1 edges निवडतो
    minimum = INF
    x = 0
    y = 0

    for i in range(N):
        if selected[i]:             # selected node
            for j in range(N):
                if (not selected[j]) and G[i][j]:   # unselected neighbour
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {G[x][y]}")
    total_cost += G[x][y]
    selected[y] = True              # node select करतो

print(f"Total MST Cost: {total_cost}")

# Output: Edge : Weight
#0 - 1 : 9
#1 - 3 : 19
#3 - 4 : 31
#3 - 2 : 51
#Total MST Cost: 110