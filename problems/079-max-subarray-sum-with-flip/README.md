# Maximum Subarray Sum with Flip

## Problem Description

Given an integer array, you may perform at most one flip operation. A flip operation selects any contiguous subarray and reverses its order. The goal is to find the maximum subarray sum achievable after performing the flip (or without performing it).

### Requirements

- `N`: the length of the array
- `data_array`: an array containing N integers

### Constraints

- Return the maximum possible subarray sum

## Examples

```python
Input: N = 5, data_array = [1, 2, 3, -1, 4]
Output: 10
Explanation: Flip the subarray [-1, 4] to get [1, 2, 3, 4, -1], maximum subarray sum is 10 ([1, 2, 3, 4])
```

## Solution Approach

### 1. Problem Analysis
This problem can be decomposed into two main parts:
1. Calculate the maximum subarray sum of the original array
2. Try all possible subarray flips and find the maximum subarray sum achievable after flipping

### 2. Key Algorithms
1. **Kadane's Algorithm**: Used to calculate the maximum subarray sum of an array
   - Maintain two variables: maximum sum ending at current position (`max_ending_here`) and global maximum sum (`max_so_far`)
   - For each element, choose to either extend the previous subarray or start a new one

2. **Exhaustive Flip Search**:
   - Use nested loops to determine all possible subarray ranges
   - For each range, perform the flip and calculate the resulting maximum subarray sum

### 3. Implementation Details

```python
def kadane(arr):
    # Initialize maximum to negative infinity
    max_so_far = float('-inf')
    # Initialize current position maximum sum to 0
    max_ending_here = 0
    
    for num in arr:
        # Either extend current subarray or start new
        max_ending_here = max(num, max_ending_here + num)
        # Update global maximum
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def solution(N, data_array):
    # 1. Calculate maximum subarray sum of original array
    original_max = kadane(data_array)
    
    # 2. Handle special case
    if N < 2:
        return original_max
    
    result = original_max
    
    # 3. Try all possible flips
    for i in range(N):
        for j in range(i + 1, N):
            # Create array copy
            flipped = data_array.copy()
            # Flip the subarray
            flipped[i:j+1] = flipped[i:j+1][::-1]
            # Calculate maximum subarray sum after flip
            current_max = kadane(flipped)
            # Update result
            result = max(result, current_max)
    
    return result
```

## Complexity Analysis
- Time Complexity: O(N^3)
  - Nested loops to enumerate all possible subarrays: O(N^2)
  - Kadane's algorithm for each subarray: O(N)
  - Total: O(N^3)
- Space Complexity: O(N)
  - A copy of the array is needed to store the flipped version

## Summary

This problem combines Kadane's algorithm for maximum subarray sum with an exhaustive search over all possible flip operations. Key considerations include:
1. Not forgetting the no-flip case
2. Correctly handling all-negative arrays
3. Proper implementation of the flip operation
4. Boundary condition handling
