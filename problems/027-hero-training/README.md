# Hero Training

## Problem Description

In an idle game, you have n heroes. The game has a training mechanism: each day you can choose two heroes to train together. If both heroes have the same level, neither level changes. If the heroes have different levels, the higher-level hero gains 1 level while the lower-level hero remains unchanged.

The goal is for at least one hero to reach level 2000000000000000. Determine how many heroes have the potential to reach this level through training.

### Constraints

- n >= 1
- 1 <= u[i] <= 100000

## Examples

### Example 1
Input: n = 5, u = [1, 2, 3, 1, 2]
Output: 3
Explanation:
- The minimum level is 1
- Three heroes have levels higher than 1 (two at level 2 and one at level 3)
- These 3 heroes can continuously level up by training with level-1 heroes

### Example 2
Input: n = 4, u = [100000, 100000, 100000, 100000]
Output: 0
Explanation:
- All heroes have the same level
- No hero can level up

### Example 3
Input: n = 6, u = [1, 1, 1, 2, 2, 2]
Output: 3
Explanation:
- The minimum level is 1
- Three heroes are at level 2
- These 3 level-2 heroes can continuously level up by training with level-1 heroes

## Solution Approach

### 1. Key Observations
1. When two heroes train together:
   - If their levels are equal, neither changes
   - If their levels differ, the higher-level hero gains +1 and the lower-level hero stays the same
2. Important finding: **the lowest-level heroes can never level up through training**
3. Therefore, the lowest-level heroes can only serve as "stepping stones" to help other heroes level up

### 2. Solution Steps
1. Edge case handling:
   - If there is only 1 hero, training is impossible, return 0
   - If all heroes have the same level, no leveling up is possible, return 0

2. Main logic:
   - Find the minimum level among all heroes
   - Count all heroes with levels higher than the minimum
   - These heroes can all continuously level up by training with the minimum-level heroes

## Implementation

```python
def solution(n: int, u: list) -> int:
    # If there is only one hero, training is not possible
    if n <= 1:
        return 0
        
    # Find all distinct levels and sort them
    levels = sorted(set(u))
    
    # If all heroes have the same level, no level-up is possible
    if len(levels) == 1:
        return 0
    
    # Find the minimum level
    min_level = levels[0]
    
    # Count all heroes with levels higher than the minimum
    result = sum(1 for x in u if x > min_level)
            
    return result
```

## Complexity Analysis

- Time complexity: O(n log n) for sorting, O(n) for counting
- Space complexity: O(n) for storing the set of distinct levels

## Summary

Key takeaways:
1. Understanding the game mechanism: higher-level heroes can level up by training with lower-level heroes
2. Key insight: the lowest-level heroes can never level up, but they can help other heroes grow
3. Core solution: simply count all heroes with levels above the minimum
4. Watch for edge cases: a single hero or all heroes at the same level

## Common Pitfalls

1. Mistakenly thinking only the highest-level hero can continue to level up
2. Overlooking the fact that the minimum-level hero can be used repeatedly as a "stepping stone"
3. Failing to consider the special case where all heroes have the same level
