import random
from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    residual_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow, residual_graph

def find_min_cut(graph, source):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and not visited[v]:
                queue.append(v)
                visited[v] = True

    return [i for i, x in enumerate(visited) if x]

graph = [
    [0, 3, 0, 0, 5, 0, 7, 0],
    [0, 0, 6, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 1, 0, 0, 0, 0, 4],
    [0, 0, 0, 6, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 3, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

source = 0  
sink = 7    

max_flow, residual_graph = edmonds_karp(graph, source, sink)
min_cut = find_min_cut(residual_graph, source)

print(f"Максимальный поток: {max_flow}")
print(f"Минимальный разрез: {min_cut}")

random_graph = [[random.randint(100, 1000) if graph[i][j] > 0 else 0 for j in range(len(graph))] for i in range(len(graph))]

max_flow_random, residual_graph_random = edmonds_karp(random_graph, source, sink)
min_cut_random = find_min_cut(residual_graph_random, source)

print(f"Максимальынй поток для рандомных значений: {max_flow_random}")
print(f"Минимальный поток для рандомных занчений: {min_cut_random}")
