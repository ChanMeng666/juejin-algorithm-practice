# Best Sightseeing Pair

## Problem Description

Little R is studying a group of sightseeing spots, each with a score stored in the array values, where values[i] represents the score of the i-th sightseeing spot. The distance between spots is represented by their index difference j - i.

The sightseeing combination score for a pair of spots (i < j) is calculated as: values[i] + values[j] + i - j

Find the highest possible sightseeing combination score.

### Constraints
- 2 <= values.length
- 1 <= values[i] <= 1000

## Examples
**Example 1:**
```python
Input: values = [8, 3, 5, 5, 6]
Output: 11
Explanation: When i = 0, j = 2, the highest score is: 8 + 5 + 0 - 2 = 11
```

**Example 2:**
```python
Input: values = [10, 4, 8, 7]
Output: 16
Explanation: When i = 0, j = 2, the highest score is: 10 + 8 + 0 - 2 = 16
```

**Example 3:**
```python
Input: values = [1, 2, 3, 4, 5]
Output: 8
Explanation: When i = 2, j = 4, the highest score is: 3 + 5 + 2 - 4 = 8
```

## Solution Approach

This problem may seem complex at first glance. Let's analyze it step by step:

1. **Formula Transformation**
   - Original formula: values[i] + values[j] + i - j
   - Can be rewritten as: (values[i] + i) + (values[j] - j)
   - This transformation reveals the essence of the problem

2. **Key Insight**
   - For any position j, we need to find the maximum (values[i] + i) before it
   - This transforms the problem into maintaining a prefix maximum

3. **Solution**
   - Use a variable to track the maximum (values[i] + i) among previous positions
   - Iterate through each position j, calculate the current score, and update the maximum score
   - Simultaneously update the maximum of (values[i] + i)

## Implementation

```python
def solution(values: list) -> int:
    max_score = float('-inf')  # Initialize max score to negative infinity
    max_value_plus_i = values[0] + 0  # Initialize values[i] + i for the first position

    # Iterate through all sightseeing spots starting from the second position
    for j in range(1, len(values)):
        # Calculate the current combination score
        current_score = max_value_plus_i + (values[j] - j)
        max_score = max(max_score, current_score)

        # Update max_value_plus_i for the next iteration
        max_value_plus_i = max(max_value_plus_i, values[j] + j)

    return max_score
```

## Code Explanation

1. **Initialization**
   ```python
   max_score = float('-inf')
   max_value_plus_i = values[0] + 0
   ```
   - Initialize the maximum score to negative infinity
   - Initialize the values[i] + i value for the first position

2. **Main Loop**
   ```python
   for j in range(1, len(values)):
       current_score = max_value_plus_i + (values[j] - j)
   ```
   - Start iterating from the second position
   - Calculate the score using the current position j and the previous maximum values[i] + i

3. **Updating Maximum Values**
   ```python
   max_score = max(max_score, current_score)
   max_value_plus_i = max(max_value_plus_i, values[j] + j)
   ```
   - Update the global maximum score
   - Update the maximum of values[i] + i for the next iteration

## Complexity Analysis

- **Time Complexity**: O(n), where n is the array length; only one pass through the array is needed
- **Space Complexity**: O(1), only a constant number of variables are used

## Summary

1. Do not attempt to use a brute-force double loop, which would result in O(n^2) time complexity
2. Understanding the formula transformation is key: (values[i] + i) + (values[j] - j) is crucial for solving this problem
3. Initialize max_score with negative infinity, not 0
4. Remember to update max_value_plus_i in each iteration

Related problems:
- Best Time to Buy and Sell Stock
- Maximum Subarray Sum
- Prefix Sum related problems

This is an excellent dynamic programming thinking exercise. By transforming the formula and maintaining the maximum value, a seemingly complex problem can be simplified to a linear time complexity solution.
