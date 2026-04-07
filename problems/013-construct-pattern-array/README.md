# Construct Pattern Array

## Problem Description
Little U is given a number n and needs to construct an array following specific rules:
- For each i (from 1 to n), concatenate numbers from n down to i in reverse order
- Repeat this process until i equals n
- Output the complete concatenated array

## Examples
```python
Input: n = 3
Output: [3, 2, 1, 3, 2, 3]

Input: n = 4
Output: [4, 3, 2, 1, 4, 3, 2, 4, 3, 4]

Input: n = 5
Output: [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5]
```

## Solution Approach
1. The key is to understand the pattern of array construction:
   - When n=3, the array consists of the following groups:
     - Group 1: [3,2,1] (counting down from 3 to 1)
     - Group 2: [3,2] (counting down from 3 to 2)
     - Group 3: [3] (only 3)

2. We can observe that:
   - The outer loop controls the ending number of each group (from 1 to n)
   - The inner loop generates the number sequence for each group (counting down from n to the current endpoint)

## Implementation
```python
def solution(n: int) -> list:
    result = []
    # Iterate from 1 to n, constructing each group of numbers
    for i in range(1, n + 1):
        # From n down to i, append to the result array
        for j in range(n, i - 1, -1):
            result.append(j)
    return result
```

## Code Explanation
1. `result = []`: Create an empty list to store the final result

2. Outer loop `for i in range(1, n + 1)`:
   - i iterates from 1 to n
   - Controls the endpoint value of each group
   - For example, when n=3, there are three groups: down to 1, down to 2, down to 3

3. Inner loop `for j in range(n, i - 1, -1)`:
   - Iterates in reverse order from n down to i
   - `range(n, i - 1, -1)` represents the descending sequence from n to i
   - For example, when n=3 and i=2, the generated sequence is [3,2]

4. `result.append(j)`:
   - Appends the current number to the result array

## Complexity Analysis
- Time Complexity: O(n^2)
  - The outer loop executes n times
  - The inner loop length decreases with each execution: n, n-1, n-2, ..., 1
  - Total number of operations is n + (n-1) + (n-2) + ... + 1 ~ n^2/2

- Space Complexity: O(n^2)
  - Storage is needed for the final result array
  - The length of the result array equals the total number of operations

## Summary
This problem mainly tests:
1. Understanding of array construction patterns
2. Use of nested loops
3. Flexible use of the range() function, especially with negative step values
4. Proficiency with Python list operations

Through this problem, we learn how to identify patterns by observing examples and translate those patterns into code. This is a very common approach in algorithm problems.
