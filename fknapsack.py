class Item:
    def __init__(self,weight,profit):
        self.weight=weight
        self.profit=profit
        
def fractionKnapsack(W,arr):
    totalProfit=0.0
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True) 
    for item in arr:
        if item.weight <=W:
            W-=item.weight
            totalProfit+=item.profit
        else:
            totalProfit+=item.profit*W/item.weight
            break
        
    return totalProfit

if __name__=="__main__":
    n=int(input("Enter the number of items:"))
    W=int(input("Enter the maximum weight of knapsack:"))
    
    arr=[]
    for i in range(n):
        weight=float(input(f"Enter the weight of the {i+1} item:"))
        profit=float(input(f"Enter the profit of the {i+1} item:"))
        arr.append(Item(weight,profit))
        
    max_val=fractionKnapsack(W,arr)
    print("The maximum value of profit is",max_val)