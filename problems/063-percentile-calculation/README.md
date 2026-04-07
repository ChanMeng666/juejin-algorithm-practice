# 80th Percentile Calculation

## Problem Description

Xigua Video is developing a new feature that displays videos with view counts at or above the 80th percentile on the homepage recommendation list. Your task is to implement a program that calculates the 80th percentile of a given dataset.

### Requirements

**What is a percentile?**
- A percentile is a statistical concept used to indicate the position within a data distribution
- For example: in a sorted array of 100 numbers, the 80th percentile is the number at the 80th position
- Calculation method: sort N data points in ascending order, then the value at position N * 80% (round to the nearest integer when encountering decimals)

### Constraints

- Input: a string containing several integers separated by commas
- Output: an integer representing the 80th percentile value

## Examples

Example 1:
```
Input: data = "10,1,9,2,8,3,7,4,6,5"
Output: 8
Explanation: After sorting: [1,2,3,4,5,6,7,8,9,10], the 80% position of 10 numbers is the 8th number (index 7), which is 8
```

Example 2:
```
Input: data = "1,0,8,7,3,9,12,6,4,15,17,2,14,5,10,11,19,13,16,18"
Output: 15
Explanation: The 80% position of 20 numbers is the 16th number
```

## Solution Approach

1. Data Preprocessing
   - Split the input string by commas into a string array
   - Convert each string to an integer

2. Sorting
   - Sort the integer array in ascending order

3. Calculate the 80th Percentile Position
   - Get the array length n
   - Calculate the 80% position: n * 0.8
   - Use the `round()` function for rounding
   - Subtract 1 since array indices start from 0

4. Return the Result
   - Return the value at the calculated position

## Implementation

```python
def solution(data):
    # Convert the input string to a list of integers
    nums = [int(x) for x in data.split(',')]

    # Sort the list
    nums.sort()

    # Calculate the index for the 80th percentile position (using rounding)
    n = len(nums)
    index = round(n * 0.8) - 1

    # Return the 80th percentile value
    return nums[index]
```

## Code Explanation

1. `data.split(',')`
   - Uses the `split()` method to split the input string by commas
   - Returns a list of strings

2. `[int(x) for x in data.split(',')]`
   - Uses list comprehension to convert each string to an integer
   - Creates a new integer list

3. `nums.sort()`
   - Sorts the integer list in place
   - Results in an ascending order list

4. `round(n * 0.8) - 1`
   - `n * 0.8` calculates the 80% position
   - `round()` performs rounding
   - Subtract 1 because list indices start from 0

## Complexity Analysis

- Time Complexity: O(n log n), primarily from the sorting operation
- Space Complexity: O(n), for storing the converted integer list

## Summary

1. Input data validity
   - Ensure the input string contains only numbers and commas
   - Ensure numbers are separated by a single comma

2. Edge case handling
   - Handling when the input list length is 1
   - Rounding when calculating the 80% position

3. Index calculation
   - Note that list indices start from 0
   - Subtract 1 when calculating the position
