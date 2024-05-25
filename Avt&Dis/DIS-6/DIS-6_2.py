def adj(file_name):
    with open(file_name, 'r') as file:
        incident_matrix = [list(map(int, line.split())) for line in file.readlines()]
    #num_vertices = int(input("Вершин:"))
    #num_edges = int(input("Граней "))
    incident_matrix = []
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        incident_matrix.append(row)

    matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for vertex in range(num_edges):
        incident_vertices = [vertex for vertex in range(num_vertices) if incident_matrix[vertex][vertex] != 0]
        
        if len(incident_vertices) == 2:
            matrix[incident_vertices[0]][incident_vertices[1]] = 1
            matrix[incident_vertices[1]][incident_vertices[0]] = 1

    return matrix

file = "input.txt"
matrix = adj(file)
for row in matrix:
    print(row)