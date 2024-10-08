
# W is total weight
# wt is list of weights

def knapSack(W, wt, val, n, dp):
    if n == 0 or W == 0:
        return 0

    # Check if the value is already computed
    if dp[n][W] != -1:
        return dp[n][W]

    if wt[n-1] > W:
        dp[n][W] = knapSack(W, wt, val, n-1, dp)
    else:
        dp[n][W] = max(val[n-1] + knapSack(W - wt[n-1], wt, val, n-1, dp),
                       knapSack(W, wt, val, n-1, dp))
    
    return dp[n][W]



if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    profit = []
    weight = []

    for i in range(n):
        p = int(input(f"Enter profit for item {i+1}: "))
        profit.append(p)
        w = int(input(f"Enter weight for item {i+1}: "))
        weight.append(w)

    W = int(input("Enter the maximum weight capacity of the knapsack: "))

    # Create a dp table initialized with -1
    dp = []
    for i in range(n + 1):
        row = []  
        for j in range(W + 1):
            row.append(-1) 
        dp.append(row) 
    
    max_profit = knapSack(W, weight, profit, n, dp)
    
    print(f"The maximum profit that can be obtained is: {max_profit}")
