# Dot Counter

## Problem Description

Xiao Ming is designing a dot counter that accepts multiple incrementing number ranges and marks a dot for each unique number within those ranges. If multiple ranges overlap, the counter merges them and marks each unique number only once. Calculate how many dots the counter will mark for the given set of number ranges.

### Requirements
- Input: an array of intervals, each represented as `[start, end]`
- Output: the total count of unique integers covered by all intervals
- Overlapping or adjacent intervals should be merged

### Constraints
- Each interval is represented as a pair `[start, end]` where `start <= end`
- Intervals may overlap or be adjacent

## Examples

**Example 1:**
```python
Input: [[1, 4], [7, 10], [3, 5]]
Output: 9
Explanation:
- Intervals [1,4] and [3,5] overlap, merged into [1,5], containing numbers: 1,2,3,4,5
- Interval [7,10] remains unchanged, containing numbers: 7,8,9,10
- Total of 9 unique numbers
```

**Example 2:**
```python
Input: [[1, 2], [6, 10], [11, 15]]
Output: 12
Explanation:
- The three intervals do not overlap, containing respectively:
  [1,2]: 2 numbers
  [6,10]: 5 numbers
  [11,15]: 5 numbers
- Total of 12 unique numbers
```

## Solution Approach

This problem can be solved in the following steps:

1. **Preprocessing**:
   - First check if the input array is empty; if so, return 0
   - Sort the input intervals by their start position to facilitate subsequent merging

2. **Merge Overlapping Intervals**:
   - Starting from the first interval, process each subsequent interval
   - If the current interval's start position is less than or equal to the previous interval's end position + 1, the two intervals overlap or are adjacent
   - When merging overlapping intervals, the new interval's end position takes the maximum of the two intervals' end positions
   - If they do not overlap, add the current interval to the result

3. **Calculate Total Dots**:
   - Traverse all merged intervals
   - For each interval, calculate the count of numbers it contains (end - start + 1)
   - Sum up the counts from all intervals to get the final result

## Implementation

```python
def solution(inputArray):
    if not inputArray:
        return 0

    # Sort by interval start position
    intervals = sorted(inputArray, key=lambda x: x[0])

    # Merge overlapping intervals
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1] + 1:  # If the current interval overlaps with or is adjacent to the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    # Calculate the total count of numbers across all intervals
    total_points = 0
    for start, end in merged:
        total_points += end - start + 1

    return total_points
```

## Complexity Analysis

- **Time Complexity**: O(n log n), where n is the number of input intervals. The main cost comes from sorting the intervals.
- **Space Complexity**: O(n), for storing the merged intervals.

## Summary

This problem is a classic interval processing problem. The core ideas are:
1. Understanding how to determine interval overlap or adjacency
2. Mastering the interval merging technique
3. Correctly calculating the count of numbers within merged intervals

The general approach for solving such problems is: sort first, then merge, and finally compute. This methodology can also be applied to other similar interval processing problems.

### Related Problems
- Interval merging
- Interval overlap problems
- Interval scheduling problems
