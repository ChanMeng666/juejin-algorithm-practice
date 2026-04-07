# Arena Escape

## Problem Description

In an N x M arena maze, find the number of all "dangerous positions." A "dangerous position" is one where, regardless of the movement strategy taken, it is impossible to reach the exit.

### Requirements

Determine how many cells in the arena are dangerous (cannot reach the exit under any strategy).

### Map Elements
- `.`: Normal floor, can move in all four directions (up, down, left, right)
- `O`: Exit position
- `U`: Upward teleporter, stepping on it forces teleportation to the cell above
- `D`: Downward teleporter, stepping on it forces teleportation to the cell below
- `L`: Leftward teleporter, stepping on it forces teleportation to the cell to the left
- `R`: Rightward teleporter, stepping on it forces teleportation to the cell to the right

Note: If a teleporter sends you outside the arena boundaries, it results in death.

### Constraints

- 1 <= N, M <= 100

## Examples

### Example 1
```python
pattern = [
    [".", ".", ".", ".", "."],
    [".", "R", "R", "D", "."],
    [".", "U", ".", "D", "R"],
    [".", "U", "L", "L", "."],
    [".", ".", ".", ".", "O"]
]
Output: 10
```
Explanation: 10 positions cannot reach the exit. Positions marked X are dangerous:
```
['.', '.', '.', '.', '.']
['.', 'X', 'X', 'X', '.']
['.', 'X', 'X', 'X', 'X']
['.', 'X', 'X', 'X', '.']
['.', '.', '.', '.', 'O']
```

### Example 2
```python
pattern = [[".", "R", ".", "O"], 
           ["U", ".", "L", "."], 
           [".", "D", ".", "."], 
           [".", ".", "R", "D"]]
Output: 2
```

### Example 3
```python
pattern = [[".", "U", "O"],
           ["L", ".", "R"],
           ["D", ".", "."]]
Output: 8
```

## Solution Approach

This is a typical graph theory problem that can be solved with the following approach:

### 1. Reverse Thinking
Instead of directly finding dangerous positions, find all safe positions that can reach the exit. The remaining positions are dangerous.

### 2. BFS (Breadth-First Search)
Starting from the exit position, search in reverse to find all positions that can reach the exit.

### 3. Detailed Steps

1. **Find the exit position**
   - Scan the map to find the position of 'O'

2. **Define helper functions**
   - `is_valid(x, y)`: Check if a position is within map boundaries
   - `get_prev_positions(x, y)`: Get all predecessor positions that can reach the current position

3. **Handle different cell types**
   - Normal floor (.): Can be reached from all four directions
   - Teleporters (U/D/L/R): Can only be reached from specific directions
   - Teleporter direction and map boundaries must be considered

4. **BFS traversal**
   - Start from the exit and use a queue to store positions to process
   - Use a set to record discovered safe positions
   - Continuously find predecessor positions that can reach the current position

5. **Calculate the result**
   - Number of dangerous positions = total cells - number of safe positions

## Implementation

```python
def solution(N, M, data):
    # Find the exit position
    exit_pos = None
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'O':
                exit_pos = (i, j)
                break
        if exit_pos:
            break
    
    # Check if a position is valid
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M
    
    # Get all predecessor positions that can reach the current position
    def get_prev_positions(x, y):
        positions = []
        for px, py in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not is_valid(px, py):
                continue
            curr = data[px][py]
            # Check teleporter direction
            if curr == 'U' and x == px-1:
                positions.append((px, py))
            elif curr == 'D' and x == px+1:
                positions.append((px, py))
            elif curr == 'L' and y == py-1:
                positions.append((px, py))
            elif curr == 'R' and y == py+1:
                positions.append((px, py))
            elif curr in '.O':
                positions.append((px, py))
        return positions
    
    # BFS to find safe positions
    safe_positions = set([exit_pos])
    queue = [exit_pos]
    
    while queue:
        curr_x, curr_y = queue.pop(0)
        for px, py in get_prev_positions(curr_x, curr_y):
            if (px, py) not in safe_positions:
                safe_positions.add((px, py))
                queue.append((px, py))
    
    return N * M - len(safe_positions)
```

## Complexity Analysis

- Time complexity: O(N x M), where N and M are the number of rows and columns of the map
- Space complexity: O(N x M), mainly used for the safe positions set and BFS queue

## Summary

1. Pay special attention to teleporter directions when processing them
2. Consider the case of teleporting outside the map boundaries
3. Avoid revisiting the same position during BFS traversal
4. Proper handling of boundary conditions is important
