def count_paths(m, n, blocked_vertical=[]):
    paths = [[0] * (n + 1) for _ in range(m + 1)]
    paths[n-1][m-1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            if j in blocked_vertical:
                continue
            if i > 0:
                paths[i][j] += paths[i - 1][j]
            if j > 0:
                paths[i][j] += paths[i][j - 1]
    return paths[m][n]


m = 15  
n = 14  
blocked_vertical = [1]
total_paths = count_paths(m, n, blocked_vertical)
print("Total paths:", total_paths)