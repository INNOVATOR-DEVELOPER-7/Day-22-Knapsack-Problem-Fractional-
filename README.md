# Day-22-Knapsack-Problem-Fractional-
Here's Python Program for Knapsack Problem Fractional. Day 22 of Day 365.

 Problem Statement
You are given:
- A set of items, each with a weight and a value.
- A knapsack with a maximum capacity.

The goal is to determine the maximum value you can obtain by putting items into the knapsack, where you can take fractions of items.

 Steps to Solve the Fractional Knapsack Problem

1. Understand the Items and Capacity:
   - Let's say you have `n` items, each item `i` has a weight `w_i` and value `v_i`.
   - The knapsack has a maximum weight capacity `W`.

2. Calculate Value-to-Weight Ratio:
   - Compute the value-to-weight ratio `r_i = v_i / w_i` for each item.
   - This ratio helps in deciding which items to take first.

3. Sort Items by Ratio:
   - Sort the items in descending order based on their value-to-weight ratio `r_i`.

4. Initialize Total Value and Capacity:
   - Set `total_value = 0` and `remaining_capacity = W`.

5. Iterate Over Sorted Items:
   - For each item in the sorted list:
     - If the item's weight `w_i` is less than or equal to the remaining capacity, take the whole item:
       ``` 
       if w_i <= remaining_capacity:
           total_value += v_i
           remaining_capacity -= w_i
       ```
     - Otherwise, take as much as possible of the item to fill the remaining capacity:
       ```
       else:
           fraction = remaining_capacity / w_i
           total_value += v_i * fraction
           remaining_capacity = 0
           break
       ```

6. Result:
   - The `total_value` now represents the maximum value that can be obtained with the given knapsack capacity.

 Example

Let's say we have the following items and a knapsack with a capacity of 50:

| Item | Weight (w) | Value (v) | Value-to-Weight Ratio (v/w) |
|------|------------|-----------|----------------------------|
| A    | 10         | 60        | 6                          |
| B    | 20         | 100       | 5                          |
| C    | 30         | 120       | 4                          |

1. Sort by Ratio:
   - Sorted items: A, B, C.

2. Iteration:
   - Item A: Take all (remaining capacity: 40, total value: 60).
   - Item B: Take all (remaining capacity: 20, total value: 160).
   - Item C: Take 2/3 (20/30) of item C (total value: 160 + 80 = 240).

So, the maximum value is 240.

I hope this helps! Let me know if you need any more details.
