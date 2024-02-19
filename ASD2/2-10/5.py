def read_matrix(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        graph = [[int(val) for val in line.split()] for line in lines]
    return graph

def write_results(filename, components):
    with open(filename, 'w') as f:
        f.write(f"Колво сильно связанных комп: {len(components)}\n")
        for component in components:
            vertex = ','.join(map(str,[vertex+1 for vertex in component]))
            f.write(" ".join(map(str, vertex)) + "\n")

def transpose(graph):
    return [[graph[j][i] for j in range(len(graph))] for i in range(len(graph[0]))]

def dfs(graph, v, visited, stack):
    visited[v] = True
    for neighbor in range(len(graph)):
        if graph[v][neighbor] == 1 and not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)

def dfs_util(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in range(len(graph)):
        if graph[v][neighbor] == 1 and not visited[neighbor]:
            dfs_util(graph, neighbor, visited, component)

def strongly_connected_components(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    stack = []

    for v in range(num_vertices):
        if not visited[v]:
            dfs(graph, v, visited, stack)

    transposed_graph = transpose(graph)
    visited = [False] * num_vertices
    components = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_util(transposed_graph, v, visited, component)
            components.append(component)

    return components


input_file = "input.txt"
output_file = "output_5.txt"

graph = read_matrix(input_file)
components = strongly_connected_components(graph)
write_results(output_file, components)