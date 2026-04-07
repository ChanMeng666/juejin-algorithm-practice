# Group Familiarity Optimization

## Problem Description

Given N people (where N is a multiple of 3) and a familiarity matrix between each pair, divide all people into groups of exactly 3. The familiarity of a group is the sum of pairwise familiarity values among its three members. The goal is to find the grouping arrangement that minimizes the total familiarity across all groups.

### Requirements

- Input:
  - `N`: the number of people (a multiple of 3)
  - `familiar_matrix`: an N x N matrix where `familiar_matrix[i][j]` represents the familiarity between person `i` and person `j`
- Output: the minimum possible total familiarity when all people are divided into groups of 3

### Constraints

- N is always a multiple of 3
- The familiarity matrix is symmetric: `familiar_matrix[i][j] == familiar_matrix[j][i]`
- Diagonal values are 100 (self-familiarity) but are not used in group calculations

## Examples

```
Input: N = 3, familiar_matrix = [[100, 78, 97], [78, 100, 55], [97, 55, 100]]
Output: 230
Explanation: Only one possible group (0, 1, 2) with familiarity 78 + 55 + 97 = 230.

Input: N = 6, familiar_matrix = [[100,56,19,87,38,61],[56,100,70,94,88,94],[19,70,100,94,43,95],[87,94,94,100,85,11],[38,88,43,85,100,94],[61,94,95,11,94,100]]
Output: 299
```

## Solution Approach

This problem is solved using DFS (Depth-First Search) with backtracking to explore all possible groupings:

1. **Group Formation**: For each grouping attempt, pick the first unused person as a "leader," then try all pairs of remaining unused people to form a group of 3.

2. **Pruning via Order**: By always selecting the smallest-indexed unused person as the leader, we avoid generating duplicate groupings.

3. **Familiarity Calculation**: For each complete grouping (all N people assigned), compute the total familiarity as the sum of pairwise familiarity values within each group.

4. **Minimization**: Track the minimum total familiarity across all valid groupings.

## Implementation

```python
def calculate_group_familiarity(group, familiar_matrix):
    i, j, k = group
    return familiar_matrix[i][j] + familiar_matrix[j][k] + familiar_matrix[i][k]

def dfs(people, familiar_matrix, used, current_groups):
    n = len(people)
    if len(current_groups) * 3 == n:
        total_familiarity = sum(calculate_group_familiarity(group, familiar_matrix) 
                              for group in current_groups)
        return total_familiarity
    
    min_familiarity = float('inf')
    first = -1
    for i in range(n):
        if not used[i]:
            first = i
            break
    if first == -1:
        return float('inf')
    
    used[first] = True
    for j in range(first + 1, n):
        if used[j]:
            continue
        for k in range(j + 1, n):
            if used[k]:
                continue
            used[j] = used[k] = True
            current_groups.append((first, j, k))
            
            familiarity = dfs(people, familiar_matrix, used, current_groups)
            min_familiarity = min(min_familiarity, familiarity)
            
            current_groups.pop()
            used[j] = used[k] = False
    
    used[first] = False
    return min_familiarity

def solution(N, familiar_matrix):
    people = list(range(N))
    used = [False] * N
    return dfs(people, familiar_matrix, used, [])
```

## Complexity Analysis

- **Time Complexity**: O((N-1)!! / (3!)^(N/3)) in the worst case, which is the number of ways to partition N items into groups of 3. For small N this is tractable.
- **Space Complexity**: O(N) for the recursion stack and the `used` array.

## Summary

This problem uses exhaustive DFS with backtracking to find the optimal grouping that minimizes total familiarity. The key optimization is fixing the first unused person as the group leader at each recursion level, which eliminates redundant permutations and significantly reduces the search space.
