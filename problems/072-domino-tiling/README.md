# Domino Tiling

## Problem Description

Player S is playing with dominoes. He arranges a row of dominoes and may push some of them to the left or right. As the chain reaction progresses, some dominoes may remain standing due to balanced forces from both sides. The task is to determine which dominoes remain standing after all actions are completed.

### Requirements

- First parameter `num`: the total number of dominoes
- Second parameter `data`: a string representing the initial state of the dominoes
  - `'L'`: the domino at this position will fall to the left
  - `'R'`: the domino at this position will fall to the right
  - `'.'`: the domino at this position is initially standing

### Constraints

- If no dominoes remain standing, return the string `"0"`
- If some dominoes remain standing, return a string in the format `"count:pos1,pos2,..."`, where positions are 1-based

## Examples

```python
Input: num = 14, data = ".L.R...LR..L.."
Output: "4:3,6,13,14"

Input: num = 5, data = "R...."
Output: "0"

Input: num = 1, data = "."
Output: "1:1"
```

## Solution Approach

### 1. Problem Analysis
This is a physics simulation problem. The key is understanding how forces act on dominoes:
1. Each domino is affected by forces from both the left and right sides
2. If the left and right forces are equal, the domino remains standing
3. Force transmission weakens with distance

### 2. Algorithm
We use a "force propagation" approach:

1. Use a `forces` array to record the net force at each position
2. Perform two scans:
   - Left to right: process rightward force (influence of `R`)
   - Right to left: process leftward force (influence of `L`)
3. Check the `forces` array to find balanced positions

### 3. Implementation Details

1. **Initialization**
   ```python
   dominoes = list(data)  # Convert input string to a list
   forces = [0] * len(dominoes)  # Initialize the forces array
   ```

2. **Left-to-right scan for R influence**
   - On encountering `'R'`, set maximum force
   - On encountering `'L'`, reset force to zero
   - For `'.'`, force gradually decreases
   ```python
   force = 0
   for i in range(n):
       if dominoes[i] == 'R': force = n
       elif dominoes[i] == 'L': force = 0
       else: force = max(force - 1, 0)
       forces[i] += force
   ```

3. **Right-to-left scan for L influence**
   - On encountering `'L'`, set maximum force
   - On encountering `'R'`, reset force to zero
   - For `'.'`, force gradually decreases
   ```python
   force = 0
   for i in range(n-1, -1, -1):
       if dominoes[i] == 'L': force = n
       elif dominoes[i] == 'R': force = 0
       else: force = max(force - 1, 0)
       forces[i] -= force
   ```

4. **Find standing dominoes**
   - Traverse the `forces` array
   - If a position has force 0 and its original state is `'.'`, the domino remains standing
   ```python
   standing = []
   for i in range(n):
       if forces[i] == 0 and dominoes[i] == '.':
           standing.append(i + 1)  # Convert to 1-based index
   ```

## Complexity Analysis
- Time Complexity: O(n) - two passes through the array
- Space Complexity: O(n) - storage for the forces array

## Summary
This problem is a physics simulation exercise. The key points are:
1. Understanding force propagation rules
2. Processing forces from both left and right directions separately
3. Determining the final state of each domino through force balance

Using this approach, we can accurately simulate the domino falling process and identify the positions of dominoes that remain standing.
