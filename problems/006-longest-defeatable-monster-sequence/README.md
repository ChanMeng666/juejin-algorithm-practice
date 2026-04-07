# Longest Defeatable Monster Sequence

## Problem Description

Xiao E encounters n monsters appearing in sequence in a game. Each monster has a specific health value hi and attack power ai. Xiao E's initial health is H and attack power is A. The game rules are as follows:

1. Xiao E can defeat monsters whose health and attack power are both less than her current stats
2. For each monster, Xiao E can choose to fight it or skip it
3. To maintain battle rhythm, the defeated monster sequence must have strictly increasing health and attack power for each subsequent monster

Find the maximum number of monsters Xiao E can defeat.

### Requirements
- n: Number of monsters
- H: Xiao E's health
- A: Xiao E's attack power
- h[i]: Health of the i-th monster
- a[i]: Attack power of the i-th monster

### Constraints
- 1 < n < 100
- 1 < H,A,h[i],a[i] < 1000

## Examples
**Example 1:**
```
Input: n = 3, H = 4, A = 5, h = [1, 2, 3], a = [3, 2, 1]
Output: 1
```

**Example 2:**
```
Input: n = 5, H = 10, A = 10, h = [6, 9, 12, 4, 7], a = [8, 9, 10, 2, 5]
Output: 2
```

**Example 3:**
```
Input: n = 4, H = 20, A = 25, h = [10, 15, 18, 22], a = [12, 18, 20, 26]
Output: 3
```

## Solution Approach

This is a classic dynamic programming problem. We need to consider the following points:

1. **State Definition**:
   - Use dp[i] to represent the length of the longest defeatable sequence ending at the i-th monster

2. **State Transition**:
   - For each monster i, first check if it can be defeated (both health and attack power must be less than Xiao E's stats)
   - If it can be defeated, it can form a sequence of at least length 1
   - Then check all previous monsters j: if
     * j was defeated (dp[j] > 0)
     * The current monster's stats are strictly greater than j's stats
     * Then the current monster can be appended after j, forming a longer sequence

3. **Initialization**:
   - Initialize the dp array to all zeros
   - When a defeatable monster is found, set its position to at least 1

## Implementation

```python
def solution(n: int, H: int, A: int, h: list, a: list) -> int:
    # Create an array to store the length of the longest defeatable sequence ending at each monster
    dp = [0] * n
    
    # Iterate through each monster
    for i in range(n):
        # If the current monster can be defeated
        if H > h[i] and A > a[i]:
            # Initialize to 1, meaning at least the current monster can be defeated
            dp[i] = 1
            # Check previous monsters
            for j in range(i):
                # If the previous monster was also defeated and satisfies the sequence requirement
                if dp[j] > 0 and h[i] > h[j] and a[i] > a[j]:
                    # Update the longest sequence length
                    dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the longest sequence length
    return max(dp) if any(dp) else 0
```

## Complexity Analysis

- Time complexity: O(n^2), where n is the number of monsters. Two nested loops are needed to iterate through all monsters.
- Space complexity: O(n), a dp array of length n is needed to store the state.

## Detailed Walkthrough

Let's analyze Example 2 step by step:
```
Input: n = 5, H = 10, A = 10, h = [6, 9, 12, 4, 7], a = [8, 9, 10, 2, 5]
```

1. Processing monster 1 (6,8):
   - Can be defeated, since 10>6 and 10>8
   - dp[0] = 1

2. Processing monster 2 (9,9):
   - Can be defeated, since 10>9 and 10>9
   - Checking previous monsters: 9>6 and 9>8
   - dp[1] = 2

3. Processing monster 3 (12,10):
   - Cannot be defeated, since 10<12
   - dp[2] = 0

4. Processing monster 4 (4,2):
   - Can be defeated, since 10>4 and 10>2
   - dp[3] = 1

5. Processing monster 5 (7,5):
   - Can be defeated, since 10>7 and 10>5
   - Checking previous monsters: can only follow (4,2)
   - dp[4] = 2

The final result is the maximum value in the dp array: 2.

## Summary

This problem is a variant of the Longest Increasing Subsequence (LIS) problem in dynamic programming. The main differences are:
1. Need to first determine whether a monster can be defeated
2. Need to consider strict increase in two attributes simultaneously (health and attack power)

The key to solving such problems is:
1. Correctly define the state
2. Find the transition relationship between states
3. Properly handle boundary conditions
