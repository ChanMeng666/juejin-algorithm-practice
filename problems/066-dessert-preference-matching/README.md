# Dessert Preference Matching

## Problem Description

### Background
Xiao R wants to select some desserts such that the sum of their preference values equals exactly his target value S. He has some magic wands that can change a dessert's preference value.

### Requirements
1. There are N desserts, each with an initial preference value
2. There are M magic wands, each of which can transform a dessert's preference value to its factorial
3. Each dessert can have at most one magic wand used on it
4. You may choose to use or not use magic wands
5. The goal is to make the sum of selected desserts' preference values equal exactly S

### Constraints
- If different desserts are selected, they count as different solutions
- If a magic wand is used on a different dessert, it counts as a different solution
- The same dessert at different positions is considered a different selection

## Examples

```python
Input: n = 3, m = 2, s = 6, like = [1, 2, 3]
Output: 5

Explanation: There are 5 possible solutions:
1. Select [1,2,3]: 1 + 2 + 3 = 6
2. Select [1,2] and use magic wand on 1: 1! + 2 = 1 + 2 = 3
3. Select [1,3] and use magic wand on 1: 1! + 3 = 1 + 3 = 4
4. Select [2,3] and use magic wand on 2: 2! + 3 = 2 + 3 = 5
5. Select [3] and use magic wand on 3: 3! = 6
```

## Solution Approach

### Problem Analysis
1. Each dessert has three possible states:
   - Do not select this dessert
   - Select this dessert without using a magic wand
   - Select this dessert and use a magic wand
2. Constraints to consider:
   - The number of magic wands used cannot exceed M
   - The sum of selected desserts' preference values must equal S
   - Each dessert position needs to be considered independently

### Dynamic Programming Solution
This is a classic dynamic programming problem because:
1. It has optimal substructure: each dessert's choice depends on previous choices
2. It has overlapping subproblems: different selection paths may lead to the same state

#### State Definition
Use a 3D dynamic programming array: `dp[i][j][k]`
- i: considering up to the i-th dessert
- j: having used j magic wands
- k: current sum of preference values
- The value of `dp[i][j][k]` represents the number of ways to reach that state

#### State Transition
For each dessert, consider three possible choices:
1. Do not select the current dessert:
   ```python
   dp[i+1][j][k] += dp[i][j][k]
   ```
2. Select the current dessert without using a magic wand:
   ```python
   dp[i+1][j][k + like[i]] += dp[i][j][k]
   ```
3. Select the current dessert and use a magic wand:
   ```python
   dp[i+1][j+1][k + factorial(like[i])] += dp[i][j][k]
   ```

## Implementation

```python
def solution(n, m, s, like):
    # Helper function to calculate factorial
    def factorial(x):
        if x == 0: return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    # Initialize the dp array
    dp = [[[0] * (s + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1  # Initial state: one way to select nothing

    # Iterate through each dessert
    for i in range(n):
        # Iterate through the number of magic wands used
        for j in range(m + 1):
            # Iterate through the current sum
            for k in range(s + 1):
                if dp[i][j][k] == 0:
                    continue

                # Case 1: Do not select the current dessert
                dp[i + 1][j][k] += dp[i][j][k]

                # Case 2: Select without using a magic wand
                if k + like[i] <= s:
                    dp[i + 1][j][k + like[i]] += dp[i][j][k]

                # Case 3: Select and use a magic wand
                if j < m:
                    fact = factorial(like[i])
                    if k + fact <= s:
                        dp[i + 1][j + 1][k + fact] += dp[i][j][k]

    # Count all possible ways
    result = 0
    for j in range(m + 1):
        result += dp[n][j][s]

    return result
```

## Complexity Analysis

### Time Complexity
- Overall: O(n * m * s)
  - n: number of desserts
  - m: number of magic wands
  - s: target sum
- Factorial computation is already included in the above complexity

### Space Complexity
- O(n * m * s), mainly for the 3D dp array

## Summary

1. Problem Characteristics
   - Combinatorial counting problem
   - Multi-dimensional constraints
   - Clear state transitions

2. Key to the Solution
   - Correct state definition
   - Complete state transitions
   - Boundary condition handling

3. Optimization Suggestions
   - Space can be optimized using rolling arrays, needing only two layers of state
   - Precompute all possible factorial values
   - Add pruning conditions during traversal
   - Return 0 early when S is very large
   - Simplify computation when M is 0
