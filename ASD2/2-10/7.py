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
        file.write("Кратчайший путь:\n")
        for u, v in mst:
            file.write(f"{u+1} - {v+1}\t\n")


def prim(graph):
    num_vertices = len(graph)
    selected = set()
    selected.add(0)
    min_tree = []
    
    while len(selected) < num_vertices:
        min_weight = float('inf')
        min_edge = None

        for vertex in selected:
            for neighbor in range(num_vertices):
                if neighbor not in selected and graph[vertex][neighbor] != 0:
                    if graph[vertex][neighbor] < min_weight:
                        min_weight = graph[vertex][neighbor]
                        min_edge = (vertex, neighbor)

        min_tree.append(min_edge)
        selected.add(min_edge[1])

    return min_tree

filename = 'input.txt' 
output_file = 'output_7.txt'

matrix = read_matrix(filename)
mst = prim(matrix)
write_results(mst, output_file)

