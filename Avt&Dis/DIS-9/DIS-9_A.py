from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v, w=1):
        self.graph[u].append((v, w))
        self.graph[v].append((u, 0)) # Residual graph initially 0 capacity for reverse edge

    def BFS(self, s, t, parent):
        visited = [False] * (self.V)
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v, w in self.graph[u]:
                if visited[v] == False and w > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.V)
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                for v, w in self.graph[parent[s]]:
                    if v == s:
                        path_flow = min(path_flow, w)
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                for i, (vertex, w) in enumerate(self.graph[u]):
                    if vertex == v:
                        self.graph[u][i] = (vertex, w - path_flow)
                for i, (vertex, w) in enumerate(self.graph[v]):
                    if vertex == u:
                        self.graph[v][i] = (vertex, w + path_flow)
                v = parent[v]

        return max_flow

edges = [(8, 1), (1, 14), (12, 5), (12, 11), (11, 10), (14, 4), (3, 6), (6, 14),
         (3, 5), (9, 15), (4, 8), (10, 4), (11, 8), (10, 13), (10, 6), (3, 7),
         (10, 5), (13, 15), (10, 9), (1, 15), (4, 15), (11, 15), (12, 2),
         (7, 12), (10, 1), (7, 14), (13, 12), (9, 14), (8, 13), (13, 14)]

# Create graph instance
graph = Graph(16) # Assuming 15 nodes indexed from 1 to 15

for u, v in edges:
    graph.add_edge(u, v)

# Ford-Fulkerson execution
max_matching = graph.ford_fulkerson(0, 15) # Assuming 0 as source and 15 as sink
print("The maximum matching is:", max_matching)
