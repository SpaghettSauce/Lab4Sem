import numpy as np

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append(list(map(int, line.strip().split())))
    return np.array(matrix)

def write_results(mst, output_file):
    with open(output_file, 'w') as file:
        file.write("Грани \tЦенв\n")
        for u, v in mst:
            file.write(f"{u} - {v}\t\n")


def prim(adj_matrix):
    num_vertices = len(adj_matrix)
    selected_vertices = set()
    selected_vertices.add(0)
    min_spanning_tree = []
    
    while len(selected_vertices) < num_vertices:
        min_weight = float('inf')
        min_edge = None

        for vertex in selected_vertices:
            for neighbor in range(num_vertices):
                if neighbor not in selected_vertices and adj_matrix[vertex][neighbor] != 0:
                    if adj_matrix[vertex][neighbor] < min_weight:
                        min_weight = adj_matrix[vertex][neighbor]
                        min_edge = (vertex, neighbor)

        min_spanning_tree.append(min_edge)
        selected_vertices.add(min_edge[1])
    
    return min_spanning_tree

filename = 'input.txt' 
output_file = 'output_7.txt'

matrix = read_matrix(filename)
mst = prim(matrix)
write_results(mst, output_file)

