# Combination Sum Problem

## Problem Description

Xiao M faces a group of digits from 1 to 9, divided into multiple groups. The task is to select one digit from each group to form a new number. The goal is to count how many different selections result in a new number whose digit sum is even.

### Requirements
- numbers: A list of integers, where each integer represents a digit group

### Constraints
- Return an integer representing the number of valid combinations

## Examples
```python
Input: numbers = [123, 456, 789]
Output: 14
Explanation: The 14 valid numbers are: 147, 149, 158, 167, 169, 248, 257, 259, 268, 347, 349, 358, 367, 369

Input: numbers = [123456789]
Output: 4

Input: numbers = [14329, 7568]
Output: 10
```

## Solution Approach

1. **Problem Analysis**
   - We need to select one digit from each digit group
   - The sum of the selected digits must be even
   - We need to count all possible valid combinations

2. **Solution**
   - Use backtracking (recursion) to generate all possible combinations
   - For each digit group, convert to a string and deduplicate to avoid redundant calculations
   - Recursively select digits one by one until all groups are processed
   - Check whether the final combination's digit sum is even

## Implementation

```python
def solution(numbers):
    # Convert each number to a string and separate into individual digit sets
    digit_groups = []
    for num in numbers:
        # Convert each number to a string, then to a set for deduplication
        digit_groups.append(set(str(num)))
    
    def get_digit_sum(combination):
        # Calculate the sum of digits in the combination
        return sum(int(d) for d in combination)
    
    def backtrack(current_combination, group_index):
        # When all groups have been processed, check if the sum is even
        if group_index == len(digit_groups):
            return 1 if get_digit_sum(current_combination) % 2 == 0 else 0
        
        count = 0
        # Select a digit from the current group
        for digit in digit_groups[group_index]:
            count += backtrack(current_combination + digit, group_index + 1)
        return count
    
    # Start backtracking from an empty combination
    return backtrack("", 0)
```

## Code Explanation

1. **Data Preprocessing**
   ```python
   digit_groups = []
   for num in numbers:
       digit_groups.append(set(str(num)))
   ```
   - Convert each input number to a string
   - Use a set to remove duplicate digits
   - Store in the digit_groups list

2. **Helper Function: Calculate Digit Sum**
   ```python
   def get_digit_sum(combination):
       return sum(int(d) for d in combination)
   ```
   - Takes a string-form digit combination
   - Converts each character to an integer and computes the sum

3. **Backtracking Function**
   ```python
   def backtrack(current_combination, group_index):
   ```
   - current_combination: The currently selected digit combination
   - group_index: The index of the current digit group being processed
   - Termination condition: When all groups are processed, check if the sum is even
   - Recursive process: Iterate through each digit in the current group, add it to the combination, and continue recursing

## Complexity Analysis

- Time complexity: O(9^n), where n is the number of digit groups. Each group can have up to 9 distinct digits to choose from.
- Space complexity: O(n), mainly due to the recursion call stack depth.

## Summary

This problem is a classic application of the backtracking algorithm. It generates all possible combinations through recursion and checks whether each combination meets the condition. Key points include:
1. Using sets for deduplication to avoid redundant calculations
2. Passing the current combination and group index during recursion
3. Using string concatenation to build combinations, making it easy to compute digit sums

For algorithm beginners, this problem helps in understanding:
- The fundamental concept of backtracking algorithms
- How to handle combination problems
- How to solve complex problems using recursion

