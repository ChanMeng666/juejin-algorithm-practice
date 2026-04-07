# Stone Jumping Game

## Problem Description

Given a list of stone positions on a number line, you can perform the following operation: move one of the two endpoint stones (the stone at the minimum or maximum position) to any unoccupied position strictly between the current minimum and maximum positions. Count the maximum number of moves that can be made until no more moves are possible (i.e., all stones are in consecutive positions with no gaps).

### Requirements

- Each move must relocate one of the endpoint stones (leftmost or rightmost) to a gap between the current endpoints
- The game ends when no valid moves can be made (all stones occupy consecutive positions)
- Return the total number of moves performed

### Constraints

- The stone positions are distinct integers
- There are at least 2 stones

## Examples

### Example 1:
- Input: stones = [7, 4, 9]
- Output: 2
- Explanation: Stones are at positions 4, 7, 9. Move the stone at 4 to position 5 (between 4 and 9), then move the stone at 9 to position 6. Now stones are at 5, 6, 7 — no gaps remain. Total moves: 2.

### Example 2:
- Input: stones = [6, 5, 4, 3, 10]
- Output: 3
- Explanation: Stones are at positions 3, 4, 5, 6, 10. The stone at 10 can be moved inward repeatedly to fill gaps until all stones are consecutive. Total moves: 3.

### Example 3:
- Input: stones = [1, 2, 3, 4, 5]
- Output: 0
- Explanation: All stones are already in consecutive positions, so no moves are needed.

## Solution Approach

1. **Convert to a set**: Store stone positions in a set for O(1) lookup and efficient insertion/removal.

2. **Greedy simulation**: Repeatedly attempt to move an endpoint stone:
   - First, try to move the minimum endpoint to the first available gap scanning from left to right.
   - If the minimum endpoint cannot be moved, try to move the maximum endpoint to the first available gap scanning from right to left.
   - If neither endpoint can be moved, all stones are consecutive and the game ends.

3. **Count moves**: Increment the move counter each time a stone is successfully relocated.

## Implementation

```python
def solution(stones: list) -> int:
    # Convert stone positions to a set for efficient lookup and removal
    stone_positions = set(stones)
    moves = 0
    
    while True:
        # Find the current minimum and maximum positions
        min_pos = min(stone_positions)
        max_pos = max(stone_positions)
        
        # Try to move an endpoint
        moved = False
        
        # Check if the minimum endpoint can be moved
        for pos in range(min_pos + 1, max_pos):
            if pos not in stone_positions:
                stone_positions.remove(min_pos)
                stone_positions.add(pos)
                moves += 1
                moved = True
                break
                
        if not moved:
            # If the minimum endpoint cannot be moved, check the maximum endpoint
            for pos in range(max_pos - 1, min_pos, -1):
                if pos not in stone_positions:
                    stone_positions.remove(max_pos)
                    stone_positions.add(pos)
                    moves += 1
                    moved = True
                    break
        
        if not moved:
            break
    
    return moves
```

## Complexity Analysis

- Time complexity: O(k * n) where k is the number of moves and n is the range of positions. Each iteration scans for the first gap between the endpoints.
- Space complexity: O(n) for storing the set of stone positions.

## Summary

This problem uses a greedy simulation approach. At each step, an endpoint stone is moved to the nearest available gap. The process continues until all stones are in consecutive positions with no gaps remaining. The key insight is that moving endpoint stones inward always reduces the total span, guaranteeing termination.
