def greedy_graph_coloring(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices
    colors[0] = 0
    available_colors = [False] * num_vertices
    
    for u in range(1, num_vertices):
        for i in graph[u]:
            if colors[i] != -1:
                available_colors[colors[i]] = True
        cr = 0
        while cr < num_vertices and available_colors[cr]:
            cr += 1
        colors[u] = cr
        
        for i in graph[u]:
            if colors[i] != -1:
                available_colors[colors[i]] = False
    return colors


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

result = greedy_graph_coloring(graph)
print("Vertex Colors:")
for vertex, color in enumerate(result):
    print(f"Vertex {vertex}: Color {color}")
