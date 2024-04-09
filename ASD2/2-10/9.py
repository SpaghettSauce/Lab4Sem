INF = float('inf')

def bellman_ford(graph, start):
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0 and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0 and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                return "Oh oh, negative cycle"

    return dist

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


input_file = "input.txt"  
output_file = "output_9.txt" 

graph = read_matrix(input_file)
start_vertex = 0  

shortest_distances = bellman_ford(graph, start_vertex)
write_results(output_file, shortest_distances)
