# Perfect Even Count

## Problem Description

Xiao C has defined a "perfect even number." A positive integer x is considered a perfect even number if it satisfies both of the following conditions:

1. x is even
2. x falls within the range [l, r]

Given an array a of length n, determine how many perfect even numbers are in the array.

### Requirements

- Input: an integer n (array length), integers l and r (range endpoints), and array a
- Where 1 <= n <= 100000, 1 <= l <= r <= 1000000
- Each element in array a satisfies: 1 <= a[i] <= 1000000

### Constraints

- A number must satisfy both conditions simultaneously to be counted.

## Examples

### Example 1:
Input:
```
n = 5, l = 3, r = 8, a = [1, 2, 6, 8, 7]
```
Output:
```
2
```
Explanation: The numbers 6 and 8 in the array are perfect even numbers because they are both even and within the range [3, 8].

### Example 2:
Input:
```
n = 4, l = 10, r = 20, a = [12, 15, 18, 9]
```
Output:
```
2
```
Explanation: The numbers 12 and 18 in the array are perfect even numbers because they are both even and within the range [10, 20].

### Example 3:
Input:
```
n = 3, l = 1, r = 10, a = [2, 4, 6]
```
Output:
```
3
```
Explanation: All numbers 2, 4, and 6 in the array are perfect even numbers because they are all even and within the range [1, 10].

## Solution Approach

1. **Problem Analysis**
   - Count the numbers in the array that satisfy two conditions:
   - Condition 1: The number is even
   - Condition 2: The number falls within the given range [l, r]

2. **Solution**
   - Use a counter (`count`) to track numbers that meet the conditions
   - Iterate through each number in the array and check both conditions:
     - Use the modulo operation (`num % 2 == 0`) to check if it is even
     - Use range checking (`l <= num <= r`) to confirm it is within the range
   - If both conditions are satisfied simultaneously, increment the counter
   - Return the counter value at the end

## Implementation

```python
def solution(n: int, l: int, r: int, a: list) -> int:
    count = 0

    for num in a:
        if num % 2 == 0 and l <= num <= r:
            count += 1

    return count
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the array. Only one pass through the array is needed.
- **Space Complexity**: O(1), only a single counter variable is used.

## Summary

This is a straightforward filtering problem. The solution iterates through the array once, checking each element against two conditions (even parity and range membership). The modulo operation determines evenness, and a double inequality checks the range. Python's chained comparison (`l <= num <= r`) provides a clean and readable implementation.
