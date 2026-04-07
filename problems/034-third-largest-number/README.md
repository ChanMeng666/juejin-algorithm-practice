# Third Largest Number

## Problem Description

Xiao M wants to determine a target score by looking at previous game competition rankings. He wants to find the third-place score from previous competitions as his target. The specific rules are:

- If there are three or more distinct scores, return the third largest score.
- If there are only two or fewer distinct scores, Xiao M will choose the largest score as his target.

Help Xiao M calculate the target score based on the given score array.

### Requirements
- The first parameter `n` is an integer representing the array length
- The second parameter `nums` is an integer array representing all the scores

### Constraints
- Return an integer representing the target score

## Examples
```python
Example 1:
Input: n = 3, nums = [3, 2, 1]
Output: 1
Explanation: There are 3 distinct numbers, the third largest is 1

Example 2:
Input: n = 2, nums = [1, 2]
Output: 2
Explanation: There are only 2 distinct numbers, return the maximum value 2

Example 3:
Input: n = 4, nums = [2, 2, 3, 1]
Output: 1
Explanation: After deduplication, there are 3 distinct numbers [3, 2, 1], the third largest is 1
```

## Solution Approach

1. First, handle the duplicate number issue:
   - Use `set()` to convert the list to a set, which automatically removes duplicate elements
   - This gives us all the distinct scores

2. To find the third largest number:
   - Convert the deduplicated set back to a list
   - Use `sorted()` to sort the list in descending order (`reverse=True`)
   - The largest number is at index 0, the second largest at index 1, and the third largest at index 2

3. Determine the count of distinct numbers:
   - If there are fewer than 3 distinct numbers (`len(unique_nums) < 3`), return the maximum value (`unique_nums[0]`)
   - If there are 3 or more distinct numbers, return the third largest (`unique_nums[2]`)

## Implementation
```python
def solution(n: int, nums: list) -> int:
    # Convert the list to a set for deduplication, then back to a sorted list
    unique_nums = sorted(list(set(nums)), reverse=True)
    
    # If there are fewer than 3 distinct numbers, return the maximum value
    if len(unique_nums) < 3:
        return unique_nums[0]
    
    # Otherwise, return the third largest number
    return unique_nums[2]
```

## Complexity Analysis

- Time complexity: O(n log n), primarily from the sorting operation
- Space complexity: O(n), needed for storing the deduplicated array

## Notes

1. The problem asks for the third largest number, not the third element
2. Deduplication must be done before sorting, as duplicate numbers should not be counted multiple times
3. When there are fewer than 3 distinct numbers, return the maximum value instead of the third element
