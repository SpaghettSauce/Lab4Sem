#WARNING!! эта прога очень сомнительная, use with caution
def euler(adj_matrix):
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

def write_results(filename, eulerian_cycle):
    with open(filename, 'w') as file:
        for vertex in eulerian_cycle:
            file.write(str(vertex) + ' ')

input_file = 'input.txt'
output_file = 'output_10.txt'

graph = read_matrix(input_file)
eulerian_cycle = euler(graph)
write_results(output_file, eulerian_cycle)