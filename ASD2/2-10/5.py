def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [[int(x) for x in line.split()] for line in lines]

def write_results(components, output_file):
    with open(output_file, 'w') as f:
        for i, component in enumerate(components):
            vertex = ','.join(map(str,[vertex+1 for vertex in component]))
            f.write(f"Компонент связанности {i+1}: {vertex}\n")

def transpose_graph(graph):
    return [[graph[j][i] for j in range(len(graph))] for i in range(len(graph))]

def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for i in range(len(graph)):
        if graph[vertex][i] and not visited[i]:
            dfs(graph, i, visited, stack)
    stack.append(vertex)

def kosaraju(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    transposed_graph = transpose_graph(graph)
    visited = [False] * n
    scc_list = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs(transposed_graph, vertex, visited, component)
            scc_list.append(component)

    return scc_list


input_file = 'input.txt'
output_file = 'output_5.txt'

graph = read_matrix(input_file)
scc_list = kosaraju(graph)
write_results(scc_list, output_file)