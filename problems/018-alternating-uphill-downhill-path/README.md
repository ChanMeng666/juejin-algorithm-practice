# Alternating Uphill-Downhill Path

## Problem Description

Little U needs to walk on an m x n map. Each position on the map has a height value representing the elevation at that location. Little U's movement must follow these rules:

1. Can only go uphill or downhill; cannot move to a point with the same height
2. Movement must alternate: after going uphill, must go downhill; after going downhill, must go uphill
3. Each position can only be visited once; no revisiting

### Requirements

Calculate the maximum number of moves Little U can make on the map.

### Constraints

The map dimensions are m x n, and each cell has a distinct height value.

## Examples

**Example 1:**
```
Input: m = 2, n = 2, a = [[1, 2], [4, 3]]
Output: 3
Explanation: Can move in the order 3 -> 4 -> 1 -> 2, totaling 3 moves
```

**Example 2:**
```
Input: m = 3, n = 3, a = [[10, 1, 6], [5, 9, 3], [7, 2, 4]]
Output: 8
```

## Solution Approach

This is a typical DFS (Depth-First Search) problem that requires considering the following key points:

1. **State Tracking**:
   - Need to track visited positions
   - Need to track whether the current state is uphill or downhill
   - Need to track the current number of steps

2. **Search Strategy**:
   - Try each position as a starting point
   - Each starting point needs to try two initial states: uphill and downhill
   - Search in all four directions from each position

3. **Pruning Conditions**:
   - Stop when position is out of bounds
   - Stop when position has already been visited
   - Stop when height does not satisfy the uphill/downhill requirement

## Implementation

```python
def solution(m: int, n: int, a: list) -> int:
    # Define directions: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    max_steps = [0]  # Use a list to store max steps for easy modification in recursion

    def dfs(x: int, y: int, going_up: bool, steps: int):
        max_steps[0] = max(max_steps[0], steps)

        # Traverse all four directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if the new position is valid
            if (new_x < 0 or new_x >= m or
                new_y < 0 or new_y >= n or
                (new_x, new_y) in visited):
                continue

            # Check if the height difference meets the uphill/downhill requirement
            if going_up and a[new_x][new_y] <= a[x][y]:
                continue
            if not going_up and a[new_x][new_y] >= a[x][y]:
                continue

            # Continue searching
            visited.add((new_x, new_y))
            dfs(new_x, new_y, not going_up, steps + 1)
            visited.remove((new_x, new_y))

    # Try starting from each position
    for i in range(m):
        for j in range(n):
            visited.add((i, j))
            # Try starting with both uphill and downhill
            dfs(i, j, True, 0)
            dfs(i, j, False, 0)
            visited.remove((i, j))

    return max_steps[0]
```

## Code Explanation

1. **Function Parameters**:
   - `m, n`: Number of rows and columns of the map
   - `a`: 2D array representing the height at each position on the map

2. **Global Variables**:
   - `directions`: Defines four movement directions (right, left, down, up)
   - `visited`: Uses a set to track visited positions
   - `max_steps`: Uses a list to store the maximum number of steps (a list is used so it can be modified within recursion)

3. **DFS Function Parameters**:
   - `x, y`: Coordinates of the current position
   - `going_up`: Boolean indicating whether the next move should be uphill
   - `steps`: Number of moves made so far

4. **Main Logic**:
   - Iterates through each position on the map as a starting point
   - For each starting point, tries both starting uphill and starting downhill
   - During DFS, selects the next feasible position based on the uphill/downhill requirement
   - Uses backtracking to undo the visit marker when returning from recursion

5. **Pruning Conditions**:
   - Position out of bounds
   - Position already visited
   - Height does not satisfy the uphill/downhill requirement

## Complexity Analysis

- Time Complexity: O(4^(m*n)), since each position has 4 directions to choose from
- Space Complexity: O(m*n), mainly for the visited set and recursion stack depth

## Summary

This problem is a fairly typical DFS search problem. The key challenges are:
1. Handling the alternating uphill-downhill constraint
2. Trying each position as a starting point
3. Correctly managing visited position marking and backtracking

The keys to solving this type of problem are:
1. Clearly defining the search state
2. Correctly handling constraint conditions
3. Appropriately using pruning to optimize search efficiency
