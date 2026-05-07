def is_safe(node, graph, colors, current_color):
    for neighbor in graph.get(node, []):
        if neighbor in colors and colors[neighbor] == current_color:
            return False
    return True


def graph_coloring(graph, m, nodes, index, colors):
    if index == len(nodes):
        return True

    current_node = nodes[index]

    for color_id in range(1, m + 1):
        if is_safe(current_node, graph, colors, color_id):
            colors[current_node] = color_id

            if graph_coloring(graph, m, nodes, index + 1, colors):
                return True

            del colors[current_node]

    return False


# --- Built-in Input ---
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B']
}

m = 3  # number of colors
nodes = list(graph.keys())
colors = {}

# --- Execution ---
if graph_coloring(graph, m, nodes, 0, colors):
    print("Coloring possible:")
    for node in colors:
        print(f"{node} -> Color {colors[node]}")
else:
    print("Coloring not possible")
