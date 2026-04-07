# Digit Insertion

## Problem Description

Given two numbers a and b, where a is a positive integer and b is a non-negative integer, insert b into some position in a to form the largest possible number.

### Requirements

- Insert b into any position within a (including before the first digit and after the last digit)
- Return the largest number that can be formed

### Constraints

- a is a positive integer
- b is a non-negative integer

## Examples

1. Input: a = 76543, b = 4
   Output: 765443
   Explanation: Inserting 4 into 76543 between the digits 4 and 3 yields the maximum value 765443

2. Input: a = 1, b = 0
   Output: 10
   Explanation: Inserting 0 after 1 yields the maximum value 10

3. Input: a = 44, b = 5
   Output: 544
   Explanation: Inserting 5 before 44 yields the maximum value 544

4. Input: a = 666, b = 6
   Output: 6666
   Explanation: Inserting 6 at any position in 666 yields 6666

## Solution Approach

### Method: Iterate Over All Possible Positions

This problem can be solved with the following steps:

1. First convert the input integers to strings
   - Convert integer a to string str_a
   - Convert integer b to string str_b
   - This makes string concatenation operations convenient

2. Initialize a variable to track the maximum value
   - Use float('-inf') to initialize, ensuring the first comparison always updates the value

3. Iterate over all possible insertion positions
   - From 0 to len(str_a), covering all possible insertion positions
   - Position 0 means inserting at the very front
   - Position len(str_a) means inserting at the very end

4. Try inserting digit b at each position
   - Use string slicing: str_a[:i] + str_b + str_a[i:]
   - Convert the concatenated string back to an integer
   - Compare with the current maximum and update

5. Return the maximum value found

## Implementation

```python
def solution(a: int, b: int) -> int:
    # Convert number a to a string
    str_a = str(a)
    str_b = str(b)
    
    # Initialize the maximum value
    max_num = float('-inf')
    
    # Iterate over all possible insertion positions
    for i in range(len(str_a) + 1):
        # Insert digit b at position i
        new_num = int(str_a[:i] + str_b + str_a[i:])
        # Update the maximum value
        max_num = max(max_num, new_num)
    
    return max_num
```

## Complexity Analysis

- Time complexity: O(n), where n is the number of digits in a. We need to iterate over every possible insertion position.
- Space complexity: O(n), needed to store the string representation of the number.

## Summary

The key to this problem is:
1. Converting numbers to strings for easier insertion operations
2. Iterating over all possible insertion positions to find the one that yields the largest number
3. Using string slicing to perform the insertion
4. Handling type conversions properly to ensure the final return value is an integer

Although this approach is not optimal (it could be optimized by comparing adjacent digits), the logic is clear and easy to understand and implement. For beginners, this is an excellent introductory solution.
