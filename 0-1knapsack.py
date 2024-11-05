def zero_one_knapsack(W,wt,p,n,dp):
    if n==0 or W==0:
        return 0
    
    if (dp[n][W]!=-1):
        return dp[n][W]
    
    
    if(wt[n-1]>W):
        dp[n][W]=zero_one_knapsack(W,wt,p,n-1,dp)
    
    else:
        dp[n][W]=max(p[n-1]+zero_one_knapsack(W-wt[n-1],wt,p,n-1,dp),zero_one_knapsack(W,wt,p,n-1,dp))
        
    return dp[n][W]

if __name__=="__main__":
    
    n=int(input("Enter the number of items:"))
    W=int(input("Enter the maximum weight of knapsack:"))
    
    wt=[]
    p=[]
    
    for i in range(n):
        weight=int(input(f"Enter the weight of item {i+1}:"))
        wt.append(weight)
        
        profit=int(input(f"Enter the profit of item {i+1}:"))
        p.append(profit)
        
    
    dp=[]
    for i in range(n+1):
        row=[]
        for j in range(W+1):
            row.append(-1)
        dp.append(row)
        
    
    max_value=zero_one_knapsack(W,wt,p,n,dp)
    
    print(f"The maximum profit from the knapsack with least weight is: {max_value}")