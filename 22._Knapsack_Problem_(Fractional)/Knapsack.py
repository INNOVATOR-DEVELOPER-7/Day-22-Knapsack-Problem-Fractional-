class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(values, weights, capacity):
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the item
            total_value += item.ratio * capacity
            break

    return total_value

# Get the number of items from the user
num_items = int(input("Enter the number of items: "))

# Get the values of the items from the user
values = list(map(int, input("Enter the values of the items separated by space: ").split()))

# Get the weights of the items from the user
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))

# Get the maximum capacity of the knapsack from the user
capacity = int(input("Enter the maximum capacity of the knapsack: "))

# Perform the fractional knapsack algorithm
max_value = fractional_knapsack(values, weights, capacity)

# Print the maximum value that can be obtained
print("The maximum value that can be obtained is:", max_value)
