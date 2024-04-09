def rec(n):
    fib = [5, 6] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = 7 * fib[i - 1] - 12 * fib[i - 2]
    return fib[n]

def don(n):
    return 14*3**n+(-9)*4**n

n = 100
print("100:     ", rec(n))
print(don(n))