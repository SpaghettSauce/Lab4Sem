def read_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return matrix

def write_results(file_path, connectcomp):
    with open(file_path, 'w') as f:
        for i, component in enumerate(connectcomp):
            f.write(f"Компонент связанности {i+1}: {component}\n")

def breadth_first_search(adj_matrix, start, visited):
    queue = [start]
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        for neighbor, connected in enumerate(adj_matrix[vertex]):
            if connected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def find_connect(adj_matrix):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    connect = []

    for vertex in range(num_vertices):
        if not visited[vertex]:
            component = []
            breadth_first_search(adj_matrix, vertex, visited)
            for i, v in enumerate(visited):
                if v:
                    component.append(i)
            connect.append(component)
    return connect




input_file = 'input.txt'
output_file = 'output.txt'

adj_matrix = read_adjacency_matrix(input_file)
connectivity_components = find_connect(adj_matrix)
write_results(output_file, connectivity_components)

