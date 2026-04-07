# Largest Rectangle Area

## Problem Description

Given an array h1, h2, ..., hn, where each element represents a certain height. We need to find the maximum rectangle area that can be formed by any k adjacent elements in this array.

For k adjacent elements, the maximum rectangle area is calculated as:
R(k) = k * min(h[i], h[i+1], ..., h[i+k-1])

Where:
- k is the number of selected adjacent elements
- min() returns the minimum value among these k elements

## Examples

### Example 1
```python
Input: n = 5, array = [1, 2, 3, 4, 5]
Output: 9
Explanation: When selecting the last three elements [3,4,5], the minimum is 3, k=3, so the area is 3*3=9
```

### Example 2
```python
Input: n = 6, array = [5, 4, 3, 2, 1, 6]
Output: 9
```

### Example 3
```python
Input: n = 4, array = [4, 4, 4, 4]
Output: 16
Explanation: When selecting all elements, the minimum is 4, k=4, so the area is 4*4=16
```

## Solution Approach

1. The key to this problem is to consider all possible combinations of adjacent elements. We need to:
   - Consider all possible window sizes (k from 1 to n)
   - For each window size, consider all possible starting positions

2. For each window:
   - Find the minimum value within the window
   - Calculate the rectangle area for the current window (minimum value * window size)
   - Update the global maximum area

3. Time complexity analysis:
   - Outer loop: O(n)
   - Inner loop: O(n)
   - Finding minimum operation: O(k)
   - Overall time complexity: O(n^3)

## Implementation

```python
def solution(n, array):
    max_area = 0

    # Iterate through all possible window sizes k
    for k in range(1, n + 1):
        # Iterate through all possible starting positions
        for i in range(n - k + 1):
            # Get the minimum value in the current window
            min_height = min(array[i:i + k])
            # Calculate the rectangle area for the current window
            area = k * min_height
            # Update the maximum area
            max_area = max(max_area, area)

    return max_area
```

## Code Explanation

1. `max_area = 0`: Initialize the maximum area to 0

2. First loop `for k in range(1, n + 1)`:
   - Iterates through all possible window sizes
   - k starts from 1 up to n (the entire array length)

3. Second loop `for i in range(n - k + 1)`:
   - Iterates through all possible starting positions
   - `n - k + 1` ensures the window does not exceed the array bounds

4. `min_height = min(array[i:i + k])`:
   - Uses slicing to get the elements within the current window
   - Calculates the minimum value among these elements

5. `area = k * min_height`:
   - Calculates the rectangle area for the current window
   - Area = window size * minimum height

6. `max_area = max(max_area, area)`:
   - Updates the global maximum area
   - If the current area is larger, update max_area

## Solution Approach (Optimization)

The current solution has O(n^3) time complexity, which may be slow in practice. Consider the following optimization directions:

1. Use a monotonic stack to optimize the minimum value operation
2. Use a sliding window to maintain the minimum value
3. Preprocess the array, recording the minimum value range extending left and right from each position

These optimizations can reduce the time complexity to O(n^2) or lower.

## Summary

This problem tests:
1. Array traversal and slicing operations
2. The concept of sliding windows
3. Dynamic maintenance of maximum/minimum values
4. Rectangle area calculation

For algorithm beginners, this is a great practice problem that helps understand array operations and the sliding window concept. Although the initial solution may not be optimal, it is easy to understand and implement, making it suitable as an introductory problem.
