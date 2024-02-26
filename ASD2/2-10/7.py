import numpy as np

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append(list(map(int, line.strip().split())))
    return np.array(matrix)

def write_results(components, output_file):
    with open(output_file, 'w',encoding='cp1251') as f:
        for i, component in enumerate(components):
            vertex = ','.join(map(str,[vertex+1 for vertex in component]))
            f.write(f"Компонент связанности {i+1}: {vertex}\n")


def prim_algorithm(adj_matrix):
    num_vertices = len(adj_matrix)
    # Initialize an empty set to store selected vertices
    selected_vertices = set()
    # Select the first vertex arbitrarily
    selected_vertices.add(0)
    # Initialize an empty list to store the edges of the minimum spanning tree
    min_spanning_tree = []
    
    while len(selected_vertices) < num_vertices:
        min_weight = float('inf')
        min_edge = None
        # Find the minimum weight edge with exactly one endpoint in the selected set
        for vertex in selected_vertices:
            for neighbor in range(num_vertices):
                if neighbor not in selected_vertices and adj_matrix[vertex][neighbor] != 0:
                    if adj_matrix[vertex][neighbor] < min_weight:
                        min_weight = adj_matrix[vertex][neighbor]
                        min_edge = (vertex, neighbor)
        # Add the selected edge to the minimum spanning tree
        min_spanning_tree.append(min_edge)
        # Add the newly selected vertex to the set of selected vertices
        selected_vertices.add(min_edge[1])
    
    return min_spanning_tree

filename = 'input.txt' 
output_file = 'output_7.txt'

matrix = read_matrix(filename)
min_spanning_tree = prim_algorithm(matrix)
write_results(min_spanning_tree, output_file)
