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

def bfs(graph, start, visited,component):
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        component.append(vertex)
        for neighbor, connected in enumerate(graph[vertex]):
            if connected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    

def find_connect(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    connect = []
    for v in range(num_vertices):
        if not visited[v]:
            component = []
            bfs(graph, v,visited,  component)
            connect.append(component)
    return connect




input_file = 'input.txt'
output_file = 'output_3.txt'

graph = read_matrix(input_file)
connect_comp = find_connect(graph)
write_results(connect_comp,output_file)

