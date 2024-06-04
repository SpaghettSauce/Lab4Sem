def read_incidence_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        incidence_matrix = [list(map(int, line.strip().split())) for line in lines]
    return incidence_matrix

def incidence_to_adjacency(incidence_matrix):
    num_vertices = len(incidence_matrix)
    num_edges = len(incidence_matrix[0])
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for j in range(num_edges):
        start = end = -1
        for i in range(num_vertices):
            if incidence_matrix[i][j] == -1:
                start = i
            elif incidence_matrix[i][j] == 1:
                end = i
        if start != -1 and end != -1:
            adjacency_matrix[start][end] = 1

    return adjacency_matrix

def write_adjacency_matrix(adjacency_matrix, output_file_path):
    with open(output_file_path, 'w') as file:
        for row in adjacency_matrix:
            file.write(' '.join(map(str, row)) + '\n')


input_file_path = 'input.txt'
output_file_path = 'output.txt'

incidence_matrix = read_incidence_matrix(input_file_path)
adjacency_matrix = incidence_to_adjacency(incidence_matrix)
write_adjacency_matrix(adjacency_matrix, output_file_path)
