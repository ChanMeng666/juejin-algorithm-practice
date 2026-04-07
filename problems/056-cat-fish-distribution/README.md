# Cat Fish Distribution

## Problem Description

On Cat Planet, Xiao R is responsible for distributing fish treats to a row of cats standing in line. Each cat has a level value, and treats must be distributed according to the following rules:

1. Each cat must receive at least 1 unit of fish treats
2. If a cat has a higher level than its neighbor, that cat must receive more treats than the neighbor

The goal is to calculate the minimum total number of fish treats needed to satisfy the above conditions.

### Requirements
- Each cat receives at least 1 unit of fish treats
- A cat with a higher level than an adjacent cat must receive more treats than that neighbor
- Minimize the total number of treats distributed

### Constraints
- Cats with equal levels may receive different amounts of treats

## Examples

### Example 1
Input:
- n = 3
- cats_levels = [1, 2, 2]

Output: 4

Explanation: The optimal distribution is [1, 2, 1]
- The first cat receives 1 unit of treats
- The second cat receives 2 units of treats (higher level than the first cat)
- The third cat receives 1 unit of treats (same level as the second cat, so it can receive fewer)

### Example 2
Input:
- n = 6
- cats_levels = [6, 5, 4, 3, 2, 16]

Output: 17

Explanation: The optimal distribution is [4, 3, 2, 1, 1, 6]

## Solution Approach

This is a classic greedy algorithm problem that can be solved with two passes:

1. **Initialization**
   - Assign 1 unit of treats to each cat, satisfying the first condition

2. **Left-to-right pass**
   - Compare each cat's level with its left neighbor
   - If the current cat's level is higher than the left neighbor, give it one more treat than the left neighbor
   - This ensures the relationship with the left neighbor is correct

3. **Right-to-left pass**
   - Compare each cat's level with its right neighbor
   - If the current cat's level is higher than the right neighbor, ensure it has at least one more treat than the right neighbor
   - Use the `max` operation to avoid overwriting values established during the left pass

4. **Compute the total**
   - Sum up all treats assigned to get the answer

## Implementation

```python
def solution(n, cats_levels):
    # Initialize the amount of fish treats each cat receives to 1
    candies = [1] * n

    # Traverse left to right, ensuring higher-level cats get more treats than the cat on the left
    for i in range(1, n):
        if cats_levels[i] > cats_levels[i-1]:
            candies[i] = candies[i-1] + 1

    # Traverse right to left, ensuring higher-level cats get more treats than the cat on the right
    for i in range(n-2, -1, -1):
        if cats_levels[i] > cats_levels[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    # Return the total number of fish treats needed
    return sum(candies)
```

## Complexity Analysis

- **Time Complexity**: O(n), requires two passes over the array
- **Space Complexity**: O(n), requires an extra array to store the number of treats for each cat

## Code Explanation

1. **A single pass is not sufficient**
   - Only a left-to-right pass may fail to handle right-neighbor relationships
   - Only a right-to-left pass may fail to handle left-neighbor relationships

2. **The second pass must use `max`**
   - Cannot simply assign `candies[i] = candies[i+1] + 1`
   - Must preserve the ordering established during the first pass

3. **Handling equal levels**
   - When two adjacent cats have the same level, they may receive the same or different amounts of treats
   - To minimize the total, cats with equal levels should receive as few treats as possible

## Summary

The key insights for this problem are:
1. Understanding that two passes can solve the problem
2. Correctly handling neighbor relationships and equal-level cases
3. Minimizing the total while satisfying all rules

Mastering this problem is helpful for understanding greedy algorithms and problems involving adjacent element relationships.
