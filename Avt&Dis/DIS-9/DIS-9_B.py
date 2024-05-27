from collections import deque, defaultdict

class BipartiteGraph:
    def __init__(self, U, V):
        self.U = U
        self.V = V
        self.pair_U = {}
        self.pair_V = {}
        self.dist = {}
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def BFS(self):
        queue = deque()
        for u in self.U:
            if u not in self.pair_U:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        self.dist[None] = float('inf')

        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[None]:
                for v in self.adj[u]:
                    if self.dist.get(self.pair_V.get(v, None), float('inf')) == float('inf'):
                        self.dist[self.pair_V.get(v, None)] = self.dist[u] + 1
                        queue.append(self.pair_V.get(v, None))
        return self.dist[None] != float('inf')

    def DFS(self, u):
        if u:
            for v in self.adj[u]:
                if self.dist.get(self.pair_V.get(v, None), float('inf')) == self.dist[u] + 1:
                    if self.DFS(self.pair_V.get(v, None)):
                        self.pair_V[v] = u
                        self.pair_U[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def hopcroft_karp(self):
        for u in self.U:
            self.pair_U[u] = None
        for v in self.V:
            self.pair_V[v] = None
        matching = 0
        while self.BFS():
            for u in self.U:
                if self.pair_U[u] is None:
                    if self.DFS(u):
                        matching += 1
        return matching

U = {1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
V = {15, 2}

edges = [(8, 1), (1, 14), (12, 5), (12, 11), (11, 10), (14, 4), (3, 6), (6, 14),
         (3, 5), (9, 15), (4, 8), (10, 4), (11, 8), (10, 13), (10, 6), (3, 7),
         (10, 5), (13, 15), (10, 9), (1, 15), (4, 15), (11, 15), (12, 2),
         (7, 12), (10, 1), (7, 14), (13, 12), (9, 14), (8, 13), (13, 14)]

bipartite_graph = BipartiteGraph(U, V)
for u, v in edges:
    bipartite_graph.add_edge(u, v)

max_matching = bipartite_graph.hopcroft_karp()
print("The maximum matching using Hopcroft-Karp is:", max_matching)
