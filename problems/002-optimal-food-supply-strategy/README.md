# Optimal Food Supply Strategy

## Problem Description

Xiao R is planning a hiking trip from location A to location B, which takes N days in total. To maintain sufficient energy during the trip, Xiao R must consume 1 portion of food each day. Fortunately, Xiao R passes through a supply station every day, where he can first purchase food and then consume 1 portion for the day. However, the price per portion of food may vary at each supply station, and after purchasing, Xiao R can carry at most K portions of food at the same time.

Now, Xiao R wants to complete the hiking trip with the minimum cost while ensuring daily food consumption. Can you help Xiao R calculate the minimum cost?

### Requirements
- n: Total number of days for the trip
- k: Maximum number of food portions Xiao R can carry at once
- data[i]: Price per portion of food at the supply station on day i

### Constraints
- 1 < n,k < 1000
- 1 < data[i] < 10000

## Examples
**Example 1:**
```python
Input: n = 5, k = 2, data = [1, 2, 3, 3, 2]
Output: 9
```

**Example 2:**
```python
Input: n = 6, k = 3, data = [4, 1, 5, 2, 1, 3]
Output: 9
```

**Example 3:**
```python
Input: n = 4, k = 1, data = [3, 2, 4, 1]
Output: 10
```

## Solution Approach

This is a classic dynamic programming problem. We need to make optimal decisions each day: whether to buy food and how many portions to buy.

### Key Analysis

1. **State Definition**
   - Use a 2D array dp[i][j] to represent the minimum cost at the start of day i with j food portions on hand
   - i ranges from [0, n], j ranges from [0, k]

2. **State Transition**
   - For each day, we need to consider two cases:
     1. No food on hand (j=0): Must buy at least 1 portion
     2. Has food on hand (j>0): Can choose not to buy, or buy some to replenish

3. **Boundary Conditions**
   - Initial state: dp[0][0] = 0
   - Other initial states: dp[0][j] = infinity (j > 0)

## Implementation

```python
def solution(n, k, data):
    # dp[i][j] represents the minimum cost at the start of day i with j food portions on hand
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Initial state
    
    # Iterate through each day
    for i in range(n):
        # Iterate through current food quantities
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue
            
            # Not enough food for today's consumption
            if j == 0:
                # Must buy at least 1 portion of food
                for buy in range(1, k + 1):
                    dp[i + 1][buy - 1] = min(
                        dp[i + 1][buy - 1],
                        dp[i][j] + buy * data[i]
                    )
            else:
                # Enough food available, can choose not to buy
                dp[i + 1][j - 1] = min(
                    dp[i + 1][j - 1],
                    dp[i][j]
                )
                # Can also choose to buy more
                for buy in range(1, k - j + 1):
                    dp[i + 1][j + buy - 1] = min(
                        dp[i + 1][j + buy - 1],
                        dp[i][j] + buy * data[i]
                    )
    
    return dp[n][0]
```

## Code Explanation

1. **Initialization**
   ```python
   dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
   dp[0][0] = 0  # Initial state
   ```
   - Create a (n+1) x (k+1) 2D array
   - Set initial states to infinity, except dp[0][0] = 0

2. **Main Loop**
   ```python
   for i in range(n):
       for j in range(k + 1):
   ```
   - Iterate through each day and possible food quantities

3. **Handling the No-Food Case**
   ```python
   if j == 0:
       for buy in range(1, k + 1):
           dp[i + 1][buy - 1] = min(
               dp[i + 1][buy - 1],
               dp[i][j] + buy * data[i]
           )
   ```
   - When there is no food, must buy at least 1 portion
   - The purchase range is [1, k]

4. **Handling the Has-Food Case**
   ```python
   else:
       # Case: no purchase
       dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
       # Case: purchase
       for buy in range(1, k - j + 1):
           dp[i + 1][j + buy - 1] = min(
               dp[i + 1][j + buy - 1],
               dp[i][j] + buy * data[i]
           )
   ```
   - When there is food, can choose not to buy
   - Can also choose to buy some, but must consider the capacity limit

### Detailed Walkthrough of Example 1
For input: n = 5, k = 2, data = [1, 2, 3, 3, 2]

The optimal strategy is:
1. Day 1: Buy 2 portions, cost 2 (consume 1, 1 remaining)
2. Day 2: Buy 2 portions, cost 4 (consume 1, 2 remaining)
3. Day 3: Don't buy, consume 1 (1 remaining)
4. Day 4: Don't buy, consume 1 (0 remaining)
5. Day 5: Buy 1 portion, cost 3 (consume 1, 0 remaining)

Total cost: 2 + 4 + 0 + 0 + 3 = 9

## Summary

This problem is a classic dynamic programming problem. The key lies in:
1. Correctly defining the state (meaning of the dp array)
2. Identifying the state transition equations
3. Properly handling boundary conditions
4. Carefully considering each day's decision choices

Special attention is needed for:
- 1 portion of food must be consumed each day
- The purchase quantity limit
- Must buy when there is no food on hand
- The final state must have no remaining food
