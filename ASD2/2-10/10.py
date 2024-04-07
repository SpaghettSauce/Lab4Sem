def find_eulerian_cycle(adj_matrix):
    num_vertices = len(adj_matrix)
    cycle = []
    stack = []
    current_vertex = 0

    while True:
        cycle.append(current_vertex)
        unvisited_edges = False
        for v in range(num_vertices):
            if adj_matrix[current_vertex][v] > 0:
                unvisited_edges = True
                break

        if not unvisited_edges:
            if not stack:
                break
            else:
                current_vertex = stack.pop()
        else:
            stack.append(current_vertex)
            for v in range(num_vertices):
                if adj_matrix[current_vertex][v] > 0:
                    adj_matrix[current_vertex][v] -= 1
                    adj_matrix[v][current_vertex] -= 1
                    current_vertex = v
                    break

    return cycle

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        adj_matrix = [[int(x) for x in line.split()] for line in lines]
    return adj_matrix

def write_result_to_file(filename, eulerian_cycle):
    with open(filename, 'w') as file:
        for vertex in eulerian_cycle:
            file.write(str(vertex) + ' ')

input_filename = 'input.txt'
output_filename = 'output_10.txt'

adj_matrix = read_matrix(input_filename)
eulerian_cycle = find_eulerian_cycle(adj_matrix)
write_result_to_file(output_filename, eulerian_cycle)