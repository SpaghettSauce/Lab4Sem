MAXN = 1e5
g = [[] for _ in range(MAXN)]
used = [False] * MAXN
comp = []

def dfs(v):
    used[v] = True
    comp.append(v)
    for to in g[v]:
        if not used[to]:
            dfs(to)

def find_comps(n):
    for i in range(n):
        used[i] = False
    for i in range(n):
        if not used[i]:
            comp.clear()
            dfs(i)
 
            print("Component:", end="")
            for j in range(len(comp)):
                print(' ', comp[j], end="")
            print()