# Structure for an item which stores weight and value
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sorting Items by value/weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True) 

    # Result(value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:
        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        # If we can't add current Item, add fractional part of it
        else:
            finalvalue += item.profit * W / item.weight
            break
    
    # Returning final value
    return finalvalue


# Driver Code
if __name__ == "__main__":
    W = int(input("Enter the maximum weight capacity of the knapsack: "))
    n = int(input("Enter the number of items: "))
    
    arr = []
    
    # Taking input for items
    for i in range(n):
        profit = float(input(f"Enter profit for item {i + 1}: "))
        weight = float(input(f"Enter weight for item {i + 1}: "))
        arr.append(Item(profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"The maximum value that can be obtained is: {max_val}")
