def read_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = [[int(val) for val in line.split()] for line in lines]
    return matrix

def write_results(mst, output_file):
    with open(output_file, 'w') as file:
        file.write("Грани \tЦенв\n")
        for u, v, weight in mst:
            file.write(f"{u} - {v}\t{weight}\n")

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    result = []
    i = 0
    e = 0

    edges = []
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if adjacency_matrix[u][v] != 0:
                edges.append([u, v, adjacency_matrix[u][v]])
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    while e < num_vertices - 1:
        u, v, weight = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, weight])
            union(parent, rank, x, y)

    return result



input_file_path = "input.txt"  
output_file_path = "output_6.txt"

adjacency_matrix = read_matrix(input_file_path)
mst = kruskal(adjacency_matrix)
write_results(mst, output_file_path)