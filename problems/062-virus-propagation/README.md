# Virus Propagation

## Problem Description

In an enclosed room, there are n rows and m columns of seats, with each seat spaced 1 meter apart. Every seat in the room is occupied, with some people wearing masks (represented by 1) and some not wearing masks (represented by 0). One person in the room is already infected with a virus, which can spread 1 meter per second to adjacent seats.

### Requirements

For people wearing masks:
1. The virus takes two seconds to successfully infect them
2. If there are multiple infection sources simultaneously (at least one adjacent infected person), it only takes 1 second to be infected

Design an algorithm to calculate the minimum time required for the virus to infect everyone in the room. If it is impossible to infect everyone, return 0.

### Constraints
- The room has n rows and m columns
- Each seat is either 0 (no mask) or 1 (wearing mask)
- The patient's position must be within valid bounds

## Examples

### Example 1
```
Input:
row_n = 4, column_m = 4
seats = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,1,1],
    [0,0,0,1]
]
patient = [2,2]

Output: 6

Explanation: Starting from position [2,2], considering that some people wearing masks take 2 seconds to infect, it takes 6 seconds to infect everyone.
```

### Example 2
```
Input:
row_n = 4, column_m = 4
seats = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,1,1],
    [0,0,0,1]
]
patient = [2,5]

Output: 0

Explanation: The initial infected person's position is outside the array bounds, so propagation cannot begin, thus returning 0.
```

## Solution Approach

This is a classic graph search problem that can be solved using Breadth-First Search (BFS). The main difficulty lies in handling the propagation time calculation for people wearing masks.

### Algorithm Steps

1. **Initialization**
   - Create a distance array `dist`, using `float('inf')` to represent unvisited positions
   - Use a deque to store positions to process
   - Add the initial infected person's position to the queue with distance 0

2. **BFS Traversal**
   - Dequeue the current position and time
   - Iterate through four directions (up, down, left, right)
   - For each new position, calculate propagation time based on mask status:
     - Not wearing a mask: propagation time + 1
     - Wearing a mask: check if there are other infection sources nearby
       - At least one other infection source: propagation time + 1
       - No other infection source: propagation time + 2

3. **Update Propagation Time**
   - If a shorter propagation time is found, update the `dist` array
   - Add the new position to the queue to continue propagation

4. **Result Determination**
   - Traverse all positions; if any position is unreachable (dist value is inf), return 0
   - Otherwise, return the maximum propagation time

## Implementation

```python
from collections import deque

def solution(row_n, column_m, seats, patient):
    if not seats or not seats[0]:
        return 0

    # Check if the patient position is valid
    if patient[0] < 0 or patient[0] >= row_n or patient[1] < 0 or patient[1] >= column_m:
        return 0

    # Initialize the distance array
    dist = [[float('inf')] * column_m for _ in range(row_n)]

    # Direction array: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Use a deque for BFS
    queue = deque()
    queue.append((patient[0], patient[1]))
    dist[patient[0]][patient[1]] = 0

    while queue:
        curr_row, curr_col = queue.popleft()
        curr_time = dist[curr_row][curr_col]

        for dx, dy in directions:
            new_row, new_col = curr_row + dx, curr_col + dy

            if 0 <= new_row < row_n and 0 <= new_col < column_m:
                # Calculate the time to reach the new position
                if seats[new_row][new_col] == 1:  # Wearing a mask
                    # Check if there are multiple infection sources
                    infected_count = 0
                    for dx2, dy2 in directions:
                        r2, c2 = new_row + dx2, new_col + dy2
                        if (0 <= r2 < row_n and 0 <= c2 < column_m and
                            dist[r2][c2] <= curr_time and (r2, c2) != (curr_row, curr_col)):
                            infected_count += 1

                    new_time = curr_time + (1 if infected_count >= 1 else 2)
                else:  # Not wearing a mask
                    new_time = curr_time + 1

                if new_time < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_time
                    queue.append((new_row, new_col))

    # Find the maximum infection time and check if everyone is infected
    max_time = 0
    for i in range(row_n):
        for j in range(column_m):
            if dist[i][j] == float('inf'):
                return 0  # Someone was not infected
            max_time = max(max_time, dist[i][j])

    return max_time
```

## Complexity Analysis

- Time Complexity: O(N * M * K), where N and M are the number of rows and columns of the room, and K is the constant time for checking surrounding infection sources
- Space Complexity: O(N * M), mainly for the distance array and queue storage

## Summary

1. Boundary conditions need special attention, including:
   - Empty input array
   - Invalid initial infected person position
   - Cases where not everyone can be infected

2. For people wearing masks, the multiple infection source scenario must be handled correctly:
   - Check whether there are other infection sources besides the current propagation source
   - Determine propagation time based on the number of infection sources

3. Using `float('inf')` as the initial value conveniently identifies unvisited positions and facilitates shortest time updates

4. BFS guarantees that we find the shortest propagation time path
