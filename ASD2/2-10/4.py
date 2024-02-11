def read_matrix(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        graph = [[int(val) for val in line.split()] for line in lines]
    return graph

def write_results(components, output_file):
    with open(output_file, 'w') as f:
        for i, component in enumerate(components):
            vertex = ','.join(map(str,[vertex+1 for vertex in component]))
            f.write(f"Компонент связанности {i+1}: {vertex}\n")


def dfs(graph, visited, v, component):
    visited[v] = True
    component.append(v)
    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)

def find_connect(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    components = []

    for v in range(num_vertices):
        if not visited[v]:
            component = []
            dfs(graph, visited, v, component)
            components.append(component)

    return components



input_file = "input.txt"
output_file = "output_4.txt"

adjacency_matrix = read_matrix(input_file)
connectivity_components = find_connect(adjacency_matrix)
write_results(connectivity_components, output_file)