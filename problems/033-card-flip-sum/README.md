# Card Flip Sum

## Problem Description

Xiao M has n cards, each with different numbers written on the front and back sides. The front side number is a[i] and the back side is b[i]. Xiao M wants to choose one side of each card such that the sum of all face-up numbers is divisible by 3. You need to tell Xiao M how many different arrangements can satisfy this condition.

## Examples

**Example 1:**
```
Input: n = 3, a = [1, 2, 3], b = [2, 3, 2]
Output: 3
```

**Example 2:**
```
Input: n = 4, a = [3, 1, 2, 4], b = [1, 2, 3, 1]
Output: 6
```

**Example 3:**
```
Input: n = 5, a = [1, 2, 3, 4, 5], b = [1, 2, 3, 4, 5]
Output: 32
```

## Solution Approach

This is a classic backtracking problem where we need to try all possible card flip combinations. The main approach is as follows:

1. **Use backtracking**
   - For each card, we have two choices: use the front side number or the back side number
   - Try all possible combinations through recursion

2. **State tracking**
   - Use a list to record the currently selected numbers
   - Add the number to the list after each selection

3. **Termination condition**
   - When all cards have been processed (i.e., reaching the n-th card)
   - Check whether the sum of numbers in the current combination is divisible by 3

4. **Counting valid arrangements**
   - If a combination satisfies the condition, increment the count by 1
   - Finally, return the total number of valid combinations

## Implementation

```python
def solution(n: int, a: list, b: list) -> int:
    def check_sum(nums):
        # Check if the sum of the numbers is divisible by 3
        return sum(nums) % 3 == 0
    
    def backtrack(index, current_nums):
        # If all cards have been processed, check if the current combination is valid
        if index == n:
            return 1 if check_sum(current_nums) else 0
        
        # Choose the front side number
        count = backtrack(index + 1, current_nums + [a[index]])
        
        # Choose the back side number
        count += backtrack(index + 1, current_nums + [b[index]])
        
        return count
    
    # Start trying all possible combinations from the first card
    return backtrack(0, [])
```

## Code Explanation

1. **Helper function check_sum**
   - Takes a list of numbers as a parameter
   - Computes the sum of all numbers in the list
   - Checks whether the sum is divisible by 3
   - Returns a boolean indicating whether the condition is met

2. **Backtracking function backtrack**
   - Parameters:
     - index: the index of the current card being processed
     - current_nums: the list of currently selected numbers
   - Termination condition:
     - When index == n, all cards have been processed
     - At this point, check whether the current combination is valid
   - Selection process:
     - Try selecting the front and back side of the current card respectively
     - Add the selected number to current_nums
     - Recursively process the next card
   - Return value:
     - Returns the count of valid combinations

## Complexity Analysis

- **Time complexity**: O(2^n)
  - Each card has 2 choices
  - There are n cards in total
  - Therefore, the total number of possibilities is 2^n

- **Space complexity**: O(n)
  - The depth of the recursion call stack is n
  - Each recursion needs to store the current number list

## Notes

1. Pay attention to the termination condition of the recursion during implementation
2. Correctly update the current number list after each selection
3. Do not forget to count all possible combinations
4. Handle edge cases, such as when n = 0

## Related Problems

- Similar backtracking algorithm problems
- Combination sum problems
- State selection problems
