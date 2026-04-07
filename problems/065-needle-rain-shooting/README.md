# Needle Rain Shooting

## Problem Description

In the world of "Soul Land", Tang San, an outer disciple of the Tang Sect, has discovered a hidden weapon technique called "Needle Rain" (Rainstorm Pear Blossom Needles). This weapon can destroy all targets along a straight line. To practice this technique, Tang San has set up multiple targets for training. Each target is a line segment perpendicular to the X-axis. We need to help Tang San calculate the minimum number of Needle Rain shots needed to hit all targets.

### Requirements

- `k`: the number of targets
- `p`: the modulo value
- `target`: an array of targets, where each target is described by three parameters `[x_left, x_right, y]`
  - `x_left`: the starting position of the segment on the X-axis
  - `x_right`: the ending position of the segment on the X-axis
  - `y`: the fixed height of the segment

### Constraints
- The Needle Rain is fired from a certain `x` coordinate and can travel vertically up to `y = 100` height
- Any target on this vertical line will be hit
- Return the minimum number of shots needed to hit all targets, with the result taken modulo `p`

## Examples

```python
Example 1:
Input: k = 4, p = 100
target = [[10, 26, 3], [4, 8, 29], [1, 5, 8], [9, 9, 9]]
Output: 3

Example 2:
Input: k = 3, p = 100
target = [[10, 26, 3], [4, 8, 29], [1, 5, 8]]
Output: 2
```

## Solution Approach

### Problem Essence
1. Although the problem description involves a 2D plane, since the Needle Rain can reach a height of `y = 100`, the `y` values of all targets do not actually affect the result
2. We can simplify the problem to a 1D interval covering problem: cover all intervals with the minimum number of points

### Greedy Strategy
1. Project all targets onto the X-axis to obtain a series of intervals `[x_left, x_right]`
2. Sort by the right endpoint of each interval
3. For each uncovered interval, place a Needle Rain shot at its right endpoint
4. This ensures that:
   - The current interval is covered
   - Other intervals extending to this point or beyond may also be covered

### Algorithm Correctness
This greedy strategy is correct because:
1. If we place the shot at a point other than the right endpoint within an interval, the range of covered intervals can only be smaller
2. Sorting by the right endpoint ensures we always select the position that covers the most unprocessed intervals

## Implementation

```python
def solution(k, p, target):
    if not target:
        return 0

    # Convert to intervals and sort by right endpoint
    intervals = [(t[0], t[1]) for t in target]
    intervals.sort(key=lambda x: x[1])

    count = 0
    pos = float('-inf')

    # Greedy: place line at rightmost point when needed
    for left, right in intervals:
        if left > pos:
            pos = right
            count += 1

    return count % p
```

## Code Explanation

1. **Edge Case Handling**:
   - If the target array is empty, return 0 directly

2. **Data Preprocessing**:
   - Convert each target to an interval `[x_left, x_right]`
   - Ignore the `y` value since it does not affect the result
   - Sort by the right endpoint of each interval

3. **Greedy Processing**:
   - `pos` records the position of the last Needle Rain shot placed
   - For each interval, if its left endpoint is greater than `pos`, the current interval is uncovered
   - A new Needle Rain shot needs to be placed at the current interval's right endpoint
   - Update `pos` and the counter `count`

4. **Result Processing**:
   - Return the number of shots modulo `p`

## Complexity Analysis

- Time Complexity: O(n log n), primarily from the sorting operation
- Space Complexity: O(n), for storing the interval array

## Summary

1. Do not be misled by the 2D nature of the problem; learn to simplify the problem
2. Interval covering problems can typically be solved using a greedy strategy
3. Sorting by the right endpoint is a common technique for solving such problems
4. Handle edge cases carefully in the implementation, such as empty input

### Extended Thinking
1. What if the targets are arbitrary shapes instead of vertical line segments?
2. How would the problem change if the Needle Rain could be fired at an angle instead of vertically?
3. How should the algorithm be modified if some targets have heights exceeding 100?

These extended questions help deepen understanding of the problem's essence and cultivate algorithmic thinking.
