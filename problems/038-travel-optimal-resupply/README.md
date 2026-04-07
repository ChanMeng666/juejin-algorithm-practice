# Travel Optimal Resupply - Dynamic Programming

## Problem Description

### Background
Xiao U plans to go on a hiking trip from location A to location B and needs to solve the food supply problem during the journey.

### Requirements
- The trip takes a total of `M` days
- One unit of food is consumed each day
- There are `N` supply stations along the way
- The location and food price of each supply station are known
- Day 0 (departure) always has a supply station
- Supply stations appear in chronological order

### Constraints
Find the optimal purchasing strategy to minimize total cost while ensuring food is available every day.

### Input Format
- `M`: Total number of travel days (integer)
- `N`: Number of supply stations (integer)
- `p`: Supply station information list, each element is `[A, B]`
  - `A`: The day the supply station appears
  - `B`: The price per unit of food at that station

## Examples
```python
# Example 1
Input: m = 5, n = 4, p = [[0, 2], [1, 3], [2, 1], [3, 2]]
Output: 7

# Example 2
Input: m = 6, n = 5, p = [[0, 1], [1, 5], [2, 2], [3, 4], [5, 1]]
Output: 6

# Example 3
Input: m = 4, n = 3, p = [[0, 3], [2, 2], [3, 1]]
Output: 9
```

## Solution Approach

### Problem Analysis
1. **Key characteristics**
   - Food must be consumed every day
   - Multiple days' worth of food can be purchased at a supply station
   - Prices vary across supply stations
   - Planning is needed for how much food to buy at each station

2. **Decision process**
   - At each supply station, decide whether to buy food
   - If buying, decide how many days' worth to purchase
   - Purchasing decisions affect the state of subsequent days

### Dynamic Programming Design

1. **State definition**
   - Use a one-dimensional array `dp[i]` to represent the minimum cost to reach day i
   - `i` ranges from [0, M]

2. **State transition analysis**
   - When encountering a supply station, food can be purchased to cover subsequent days
   - For a supply station on day i, food can be purchased to supply up to any subsequent day j
   - The cost of purchasing (j-i) units of food is: (j-i) * price
   - State transition equation: `dp[j] = min(dp[j], dp[i] + (j-i) * price)`

3. **Initialization**
   - dp[0] = 0: no cost at the start
   - All other positions initialized to infinity

4. **Final result**
   - dp[M] is the required minimum total cost

## Implementation

```python
def solution(m: int, n: int, p: list[list[int]]) -> int:
    """
    Calculate the minimum cost to complete the journey.
    
    Args:
        m (int): Total number of travel days
        n (int): Number of supply stations
        p (list[list[int]]): Supply station information, each element is [day, price]
    
    Returns:
        int: Minimum cost
    """
    # Create dp array, dp[i] represents the minimum cost to reach day i
    dp = [float('inf')] * (m + 1)
    
    # Record supply station positions and prices
    stations = {day: price for day, price in p}
    
    # Initialize the state for day 0
    dp[0] = 0
    
    # Dynamic programming process
    for i in range(m):
        # If there is a supply station on the current day
        if i in stations:
            price = stations[i]
            # Buy food from the current station to sustain for each subsequent day
            for j in range(i + 1, m + 1):
                # dp[j] can transition from dp[i], requiring (j-i) units of food
                dp[j] = min(dp[j], dp[i] + (j - i) * price)
    
    return dp[m]
```

## Code Explanation

Let us take Example 1 as a detailed walkthrough:

Input: `m = 5, n = 4, p = [[0, 2], [1, 3], [2, 1], [3, 2]]`

**Execution process**:
1. Initial state:
   - dp[0] = 0, all other positions are infinity

2. Process day 0 supply station (price=2):
   - Can purchase food for days 1 through 5
   - dp[1] = min(inf, 0 + 1x2) = 2
   - dp[2] = min(inf, 0 + 2x2) = 4
   - dp[3] = min(inf, 0 + 3x2) = 6
   - dp[4] = min(inf, 0 + 4x2) = 8
   - dp[5] = min(inf, 0 + 5x2) = 10

3. Process day 1 supply station (price=3):
   - Can purchase food for days 1 through 4
   - dp[2] = min(4, 2 + 1x3) = 4
   - dp[3] = min(6, 2 + 2x3) = 6
   - dp[4] = min(8, 2 + 3x3) = 8
   - dp[5] = min(10, 2 + 4x3) = 10

4. Process day 2 supply station (price=1):
   - Can purchase food for days 1 through 3
   - dp[3] = min(6, 4 + 1x1) = 5
   - dp[4] = min(8, 4 + 2x1) = 6
   - dp[5] = min(10, 4 + 3x1) = 7

5. Process day 3 supply station (price=2):
   - Can purchase food for days 1 through 2
   - dp[4] = min(6, 5 + 1x2) = 6
   - dp[5] = min(7, 5 + 2x2) = 7

6. Final result:
   - dp[5] = 7 is the required minimum cost

## Complexity Analysis

- **Time complexity**: O(M^2) in the worst case, iterating through all days and for each supply station extending to all subsequent days
- **Space complexity**: O(M), for the dp array

## Summary

### Key Points
1. **State design**
   - Choosing an appropriate state representation is the key to solving the problem
   - This problem uses a one-dimensional DP array to simplify the state transition process

2. **Transition equation**
   - A clear transition equation ensures correctness
   - All possible purchasing strategies must be considered

3. **Boundary handling**
   - Correct initialization ensures proper starting conditions
   - Proper iteration range avoids array out-of-bounds errors

### Further Considerations
1. What if the supply stations have limited food quantities? How should the algorithm be modified?
2. What if the food has an expiration date? How should the approach be adjusted?
3. If discarding food at non-station locations is allowed, would it affect the result?

### Notes
1. Ensure all constraints in the problem are understood
2. Carefully handle boundary cases in dynamic programming
3. Pay attention to default value settings during array initialization
4. Verify the code's behavior across various test cases
