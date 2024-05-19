def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = values[i - 1] + dp[i - 1][w - weights[i - 1]] or dp[i - 1][w] #  dp[i][j] = dp[i - 1][j - numbers[i - 1]] or dp[i - 1][j]  # Обновление значения в таблице dp.
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [0, 3, 0, 5]
values = [2, 4, 5, 6]
capacity = 12
print(knapsack(weights, values, capacity))