def knapsack(resources, revenue, W):
    n = len(resources)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if resources[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], 
                               revenue[i-1] + dp[i-1][w-resources[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
                
    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i)
            w -= resources[i-1]
            
    return dp, dp[n][W], selected[::-1]

if __name__ == "__main__":
    resources = [2, 3, 4, 5]
    revenue = [3, 4, 5, 6]
    capacity = 5
    
    dp, best, selected = knapsack(resources, revenue, capacity)
    print("Maximum revenue:", best)
    print("Selected applications:", selected)
