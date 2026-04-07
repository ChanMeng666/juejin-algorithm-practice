# Supermarket Product Arrangement Optimization

## Problem Description

In a supermarket, there is a shelf with n slots, each containing one product represented by a lowercase letter from a to z. When customers enter the supermarket, they search from the first slot to the n-th slot for the product they want to buy.

Shopping rules:
1. If the desired product is found in a slot, the customer buys it and leaves
2. If an empty slot is encountered along the way, the customer leaves
3. If the customer finishes checking all slots without finding the desired product, they leave

As the supermarket manager, you can rearrange the product order before customers arrive to sell as many products as possible. Note: Once the first customer enters, the product positions can no longer be adjusted.

### Requirements
- n: Number of slots on the shelf
- m: Number of product types customers want to buy
- s: Initial order of products on the shelf
- c: Product types customers want to buy

## Examples

**Example 1:**
```python
Input: n = 3, m = 4, s = "abc", c = "abcd"
Output: 3
Explanation: Arrange as "abc", so the first three customers can all buy their products; the fourth customer cannot find 'd'
```

**Example 2:**
```python
Input: n = 4, m = 2, s = "abbc", c = "bb"
Output: 2
Explanation: Arrange the products as "bbac", so both customers looking for 'b' can buy it
```

**Example 3:**
```python
Input: n = 5, m = 4, s = "bcdea", c = "abcd"
Output: 4
Explanation: Arrange the products as "abcde", so the first four customers can all buy their products
```

## Solution Approach

1. **Problem Analysis**
   - This is an optimization problem where we need to find the optimal product arrangement order
   - The key is understanding customer purchasing behavior: searching left to right, buying and leaving when found
   - Once a product is purchased, that position becomes empty, potentially affecting subsequent customers

2. **Solution**
   - Count the demand for each product
   - Sort products in descending order by demand (alphabetical order for equal demand)
   - Simulate the customer purchasing process and track sold positions

3. **Optimization Strategy**
   - Products with higher demand should be placed first
   - Products with equal demand are sorted alphabetically for easier lookup
   - Use a set to track sold positions and prevent duplicate sales

## Implementation

```python
def solution(n: int, m: int, s: str, c: str) -> int:
    # Convert the product list to a list for manipulation
    items = list(s)
    
    # Count the quantity of products each customer wants to buy
    customer_wants = {}
    for char in c:
        customer_wants[char] = customer_wants.get(char, 0) + 1
    
    # Count the quantity of each product on the shelf
    shelf_items = {}
    for char in s:
        shelf_items[char] = shelf_items.get(char, 0) + 1
    
    # Sort products based on customer demand
    # Prioritize products that more customers want
    items.sort(key=lambda x: (-customer_wants.get(x, 0), x))
    
    # Simulate the customer purchasing process
    sold = 0
    used_positions = set()
    
    for customer_item in c:
        found = False
        # Iterate through all positions
        for pos in range(n):
            if pos in used_positions:
                continue
            if items[pos] == customer_item:
                sold += 1
                used_positions.add(pos)
                found = True
                break
            # If an empty slot is encountered, the customer leaves
            if items[pos] == ' ':
                break
        # If the desired product was not found, move to the next customer
        if not found:
            continue
            
    return sold
```

## Code Explanation

1. **Data Preprocessing**
   ```python
   items = list(s)
   customer_wants = {}
   for char in c:
       customer_wants[char] = customer_wants.get(char, 0) + 1
   ```
   - Convert the input string to a list for easy modification
   - Count the demand for each product type

2. **Product Sorting**
   ```python
   items.sort(key=lambda x: (-customer_wants.get(x, 0), x))
   ```
   - Use a custom sorting rule
   - `-customer_wants.get(x, 0)` ensures higher-demand products come first
   - The second sort key `x` ensures alphabetical order for equal demand

3. **Simulating the Purchase Process**
   ```python
   sold = 0
   used_positions = set()
   
   for customer_item in c:
       found = False
       for pos in range(n):
           if pos in used_positions:
               continue
           if items[pos] == customer_item:
               sold += 1
               used_positions.add(pos)
               found = True
               break
   ```
   - Iterate through each customer's demand
   - Check each position for the desired product
   - Track sold positions
   - Count total sales

## Complexity Analysis

- Time complexity: O(n * m), where n is the number of shelf slots and m is the number of customers
- Space complexity: O(n), mainly for storing the product list and the set of sold positions

## Summary

This problem tests the greedy algorithm approach, maximizing sales by strategically arranging product positions. The key points are:
1. Recognizing that higher-demand products should be placed first
2. Correctly handling sold product positions
3. Simulating customer purchasing behavior

For algorithm beginners, this problem is excellent practice as it combines a real-world scenario, helping to understand how to translate practical problems into algorithmic solutions.
