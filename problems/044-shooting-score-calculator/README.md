# Shooting Score Calculator

## Problem Description

Xiao E is practicing shooting at a training range. The target has 10 rings, with the bullseye located at coordinates (0, 0). Each ring corresponds to a different scoring rule:
- Within the bullseye (radius 1): 10 points
- Each successive ring outward reduces the score by 1 point
- If the shooting point is within a circle of radius i, the score is (11 - i) points
- If the shooting point is outside all rings, the score is 0 points

Given shooting coordinates (x, y), calculate Xiao E's shooting score.

## Examples

```python
Input: x = 1, y = 0
Output: 10
Explanation: The shooting point is at distance 1 from the bullseye, within ring 1, score is 11 - 1 = 10 points.

Input: x = 1, y = 1
Output: 9
Explanation: The shooting point is at distance sqrt(2) ~ 1.414 from the bullseye, within ring 2, score is 11 - 2 = 9 points.

Input: x = 0, y = 5
Output: 6
Explanation: The shooting point is at distance 5 from the bullseye, within ring 5, score is 11 - 5 = 6 points.

Input: x = 3, y = 4
Output: 6
Explanation: The shooting point is at distance 5 from the bullseye, within ring 5, score is 11 - 5 = 6 points.
```

## Solution Approach

1. **Calculate the Distance**
   - Use the Euclidean distance formula to calculate the distance from the shooting point (x, y) to the bullseye (0, 0)
   - Distance formula: distance = sqrt(x^2 + y^2)
   - Python implementation: `distance = (x * x + y * y) ** 0.5`

2. **Check if Out of Bounds**
   - If the distance exceeds 10 (the radius of the outermost ring), the shot is outside the target
   - In this case, return 0 points directly

3. **Determine the Ring Number**
   - The key is to determine which ring the shooting point falls within
   - Ceiling is needed because:
     - If the distance is 1.5, the point is within ring 2
     - If the distance is 2.0, the point is within ring 2
   - Python implementation: `ring = int(distance) + (1 if distance > int(distance) else 0)`

4. **Calculate the Score**
   - Scoring rule: 11 minus the ring number
   - Python implementation: `return 11 - ring`

## Implementation

```python
def solution(x: int, y: int) -> int:
    # Calculate the distance from the shooting point to the bullseye
    distance = (x * x + y * y) ** 0.5

    # If the distance exceeds 10, it is outside all rings, score is 0
    if distance > 10:
        return 0

    # Round up to get the ring number, then subtract from 11 to get the score
    ring = int(distance) + (1 if distance > int(distance) else 0)
    return 11 - ring
```

## Complexity Analysis

- **Time Complexity**: O(1), only constant-time arithmetic operations are performed.
- **Space Complexity**: O(1), only a fixed number of variables are used.

## Summary

This problem tests mathematical knowledge (Euclidean distance, ceiling function) and the ability to translate a real-world scenario into a mathematical model. The solution computes the distance from the shot to the bullseye, determines the ring via ceiling, and applies the scoring formula. No external libraries are needed since `** 0.5` handles the square root.
