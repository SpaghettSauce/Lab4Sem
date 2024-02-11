from collections import deque

def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return matrix

def write_output(filename, distances, paths):
    with open(filename, 'w') as file:
        for vertex, distance in enumerate(distances):
            file.write(f"кратчайшее растояниие {vertex}: {distance}\n")
            file.write(f"пу ть: {'->'.join(map(str, paths[vertex]))}\n")

def breadth_first_search(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    paths = [[] for _ in range(n)]
    paths[start].append(start)  
    visited = [False] * n
    queue = deque([start])

    while queue:
        current = queue.popleft()
        visited[current] = True
        for neighbor, weight in enumerate(graph[current]):
            if weight > 0 and not visited[neighbor]:
                queue.append(neighbor)
                if distances[current] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current] + weight
                    paths[neighbor] = paths[current] + [neighbor]  

    return distances, paths


input_file = "input.txt"
output_file = "output.txt"
source_vertex = 0

graph = read_graph(input_file)
shortest_distances, shortest_paths = breadth_first_search(graph, source_vertex)
write_output(output_file, shortest_distances, shortest_paths)