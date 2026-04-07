# Optimal Flight Route

## Problem Description

Xiao C and his manager Xiao F are planning a flight, but due to strict air traffic control, their aircraft can only fly along specific routes. The aircraft can only fly to adjacent airports or airports managed by the same airline. To minimize the number of takeoffs, Xiao C needs to find the optimal flight route.

### Requirements
- Airports are represented by an array `airports`, where each element represents a unique airport and the value represents a different airline
- `airports[0]` is the starting point, and `airports[airports.length - 1]` is the destination
- If currently at airport `i`, then `i-1` and `i+1` (if they exist) are adjacent airports that the aircraft can fly to directly
- If at airport `i` and `airports[i] == airports[j]`, then airports `i` and `j` belong to the same airline and can be flown to directly
- Find the minimum number of takeoffs to reach the destination

## Examples

```python
Example 1:
Input: airports = [10, 12, 13, 12, 14]
Output: 3
Explanation: 10 -> 12 -> 12 -> 14, requires 3 takeoffs

Example 2:
Input: airports = [10, 11, 12, 13, 14]
Output: 4
Explanation: Can only fly through adjacent airports one by one, requires 4 takeoffs

Example 3:
Input: airports = [7, 7, 7, 8, 9, 7]
Output: 1
Explanation: Fly directly from the first 7 to the last 7, requires only 1 takeoff
```

## Solution Approach

### 1. Problem Analysis
This is a classic shortest path problem where we need to find the minimum number of jumps from the start to the destination. Each airport can:
1. Fly to an adjacent airport (one on each side)
2. Fly to other airports belonging to the same airline

### 2. Solution
Use Breadth-First Search (BFS) to solve this problem because:
- BFS guarantees that the first path found to the destination is the shortest
- Each takeoff corresponds to an edge in the graph, and we need to find the minimum number of edges from start to destination

### 3. Implementation Steps

1. Initialization:
   - Use a queue to store positions to visit and their corresponding takeoff counts
   - Use a set to track visited airports to avoid revisiting

2. BFS Main Loop:
   - Dequeue the current position and the number of takeoffs used
   - If the destination is reached, return the current takeoff count
   - Otherwise, find all possible next airports:
     - Adjacent airports (if they exist)
     - Other airports of the same airline

3. For each possible next airport:
   - If not yet visited, add it to the queue
   - Record the new position and the incremented takeoff count

## Implementation

```python
def solution(airports):
    from collections import deque
    n = len(airports)

    # Use BFS to find the shortest path
    queue = deque([(0, 0)])  # (position, number of flights)
    visited = {0}  # Track visited positions

    while queue:
        pos, flights = queue.popleft()

        # If we reached the destination, return the number of flights needed
        if pos == n - 1:
            return flights

        # Try all possible next moves
        next_positions = set()

        # Add adjacent airports
        if pos + 1 < n:
            next_positions.add(pos + 1)
        if pos - 1 >= 0:
            next_positions.add(pos - 1)

        # Add other airports operated by the same airline
        for i in range(n):
            if airports[i] == airports[pos] and i != pos:
                next_positions.add(i)

        # Iterate through all possible next positions
        for next_pos in next_positions:
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, flights + 1))

    return -1  # If the destination is unreachable
```

## Complexity Analysis

- Time Complexity: O(n^2), where n is the number of airports. In the worst case, we need to traverse all airports to find others belonging to the same airline.
- Space Complexity: O(n), for storing the visited node set and the queue.

### Optimization Suggestions
- For larger datasets, a preprocessing step can build a mapping from airlines to airports, enabling faster lookup of airports belonging to the same airline
- Bidirectional BFS can be used to further optimize search efficiency

## Summary

This is a classic problem combining graph theory and search algorithms. BFS effectively finds the shortest path, and using a visited set avoids redundant visits, improving efficiency. Understanding this solution is valuable for mastering graph search algorithms and shortest path problems.
