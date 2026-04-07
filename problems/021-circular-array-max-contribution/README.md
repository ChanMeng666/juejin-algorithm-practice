# Maximum Contribution Value in a Circular Array

## Problem Description

Given a circular array of length n, define the contribution value of two indices i and j as:
```
f(i, j) = (a_i + a_j) * dist(i, j)
```
where `dist(i, j)` is the shortest distance between indices i and j in the array. Find a pair of indices that maximizes the contribution value. In a circular array, the leftmost and rightmost elements are also adjacent.

### Requirements

- Find the pair of indices (i, j) that maximizes f(i, j)

### Constraints

- n >= 1
- 1 <= a[i] <= 1000

## Examples

### Example 1:
Input: n = 3, a = [1, 2, 3]
Output: 5
Explanation: Since this is a circular array, the distance between any two indices is 1, so f(2,3) = (2 + 3) * 1 = 5.

### Example 2:
Input: n = 4, a = [4, 1, 2, 3]
Output: 12

### Example 3:
Input: n = 5, a = [1, 5, 3, 7, 2]
Output: 24

## Solution Approach

1. **Understanding Circular Array Properties**
   - In a circular array, there are two paths between any two positions: clockwise and counterclockwise
   - We need to take the shorter of these two paths as dist(i, j)

2. **Distance Calculation**
   - For positions i and j, the clockwise distance is `(j - i) % n`
   - The counterclockwise distance is `(i - j) % n`
   - Take the minimum of the two as the actual distance

3. **Solution Steps**
   - Iterate over all possible pairs (i, j)
   - Calculate the contribution value for each pair
   - Maintain the maximum contribution value
   - Return the final maximum

## Implementation

```python
def solution(n: int, a: list) -> int:
    def dist(i, j):
        # Calculate the shortest distance between two points in the circular array
        distance = min((i - j) % n, (j - i) % n)
        return (a[i] + a[j]) * distance
    
    max_contribution = 0
    
    # Iterate over all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            contribution = dist(i, j)
            max_contribution = max(max_contribution, contribution)
    
    return max_contribution
```

## Code Explanation

1. **Helper function dist(i, j)**
   - Calculates the shortest distance between two positions
   - Uses modulo operation to handle the circular property
   - Returns the contribution value computed by the formula

2. **Main function logic**
   - Initializes the maximum contribution value to 0
   - Uses nested loops to iterate over all possible pairs
   - j starts from i+1 to avoid duplicate calculations
   - Continuously updates the maximum contribution value

## Complexity Analysis

- Two nested loops iterate over all pairs, giving a time complexity of O(n^2)
- Space complexity is O(1), only constant extra space is used

## Summary

This problem mainly tests the understanding and handling of circular array properties. The key points are:
1. Correctly calculating the shortest distance between two points in a circular array
2. Understanding and implementing the contribution value formula
3. Finding the maximum contribution value by iterating over all possible pairs

Through this problem, we can learn techniques for handling circular arrays and how to find optimal solutions in cyclic structures.
