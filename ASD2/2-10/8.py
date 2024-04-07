INF = float('inf')

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = []
        for line in lines:
            graph.append(list(map(int, line.split())))
    return graph

def write_results(filename, result):
    with open(filename, 'w') as file:
        for dist in result:
            file.write(str(dist) + '\n')

def dijkstra(graph, start):
    n = len(graph)
    d = [INF] * n
    d[start] = 0
    visited = [False] * n

    for i in range(n):
        u = min_dist(d, visited)
        visited[u] = True

        for v in range(n):
            if graph[u][v] and not visited[v] and d[u] != INF and d[u] + graph[u][v] < d[v]:
                d[v] = d[u] + graph[u][v]
    return d

def min_dist(dist, visited):
    min_dist = INF
    min_index = -1
    for v in range(len(dist)):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_index = v
    return min_index






input_file = "input.txt"  
output_file = "output_8.txt"  

graph = read_matrix(input_file)
start_vertex = 0  

short = dijkstra(graph, start_vertex)
write_results(output_file, short)