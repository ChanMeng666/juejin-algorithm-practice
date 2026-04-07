# Digit Removal

## Problem Description

Xiao R has an array of length n, where each element is a positive integer. In each operation, one digit can be removed from any number in the array. The goal is to turn all numbers into 0. Calculate the minimum number of operations required.

For example, for the number 103:
- Remove the 1st digit: becomes 3
- Remove the 2nd digit: becomes 13
- Remove the 3rd digit: becomes 10

### Requirements

- First line of input: an integer n representing the array length
- Second line of input: n integers representing the numbers in the array

### Constraints

- Each operation removes exactly one digit from one number.

## Examples

Input:
```
n = 5
a = [10, 13, 22, 100, 30]
```
Output: `7`

## Solution Approach

### 1. Problem Analysis
- Each operation can remove any single digit from any number.
- An optimal removal strategy must be found to minimize the total number of steps.
- Observation: larger numbers typically require more steps to remove.

### 2. Greedy Strategy
The following greedy approach is used:
1. Find the largest number in the array each time.
2. Remove the leading digit of that largest number (since the leading digit has the greatest impact on the value).
3. Repeat until all numbers become 0.

### 3. Algorithm Steps
Using the example `[10, 13, 22, 100, 30]`, the specific operations are:

1. Remove 1 from 100 -> [10, 13, 22, 00, 30]
2. Remove 3 from 30 -> [10, 13, 22, 0, 0]
3. Remove 2 from 22 -> [10, 13, 2, 0, 0]
4. Remove 1 from 13 -> [10, 3, 2, 0, 0]
5. Remove 1 from 10 -> [0, 3, 2, 0, 0]
6. Remove 3 -> [0, 0, 2, 0, 0]
7. Remove 2 -> [0, 0, 0, 0, 0]

Total: 7 steps.

## Implementation

```python
def solution(n: int, a: list) -> int:
    # Copy the input array to avoid modifying the original
    nums = a.copy()
    steps = 0

    # Continue while there are non-zero numbers
    while any(nums):
        # Find the current largest number
        max_num = max(nums)
        # Find the position of this number in the array
        max_idx = nums.index(max_num)

        # Remove the leading digit of the largest number
        str_num = str(max_num)
        if len(str_num) > 1:
            nums[max_idx] = int(str_num[1:])
        else:
            nums[max_idx] = 0

        steps += 1

    return steps
```

## Code Explanation

1. `nums = a.copy()`: Create a copy of the input array to avoid modifying the original.
2. `while any(nums)`: Continue looping while there are non-zero numbers in the array.
3. `max_num = max(nums)`: Find the largest number in the current array.
4. `max_idx = nums.index(max_num)`: Find the position of the largest number.
5. Processing the largest number:
   - If the number has more than one digit, remove the leading digit.
   - If the number has only one digit, set it directly to 0.
6. Increment the operation counter by 1 each time.

## Complexity Analysis

- **Time Complexity**: O(D * N), where D is the number of digits in the largest number and N is the array length.
- **Space Complexity**: O(N), needed to store the array copy.

## Summary

The key insight in this problem is the greedy strategy: always removing the leading digit of the largest number is the optimal choice. This works because larger numbers will eventually need to be fully removed, and removing the leading digit reduces the number's value most rapidly, ensuring the minimum number of steps to turn all numbers to 0.
