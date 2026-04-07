# Board Game Piece Grouping

## Problem Description

Players M and F are playing a board game. After the game ends, they need to sort the game pieces on the table into groups. There are N pieces, each with a number on it. Player M's goal is to divide these pieces into groups with the following requirements:
1. Each group must contain exactly 5 pieces
2. All pieces within a group must have the same number

Determine whether the pieces can be grouped according to the above rules.

## Examples

### Example 1
Input: `nums = [1, 2, 3, 4, 5]`
Output: `"False"`
Explanation: Although there are 5 pieces, they all have different numbers, so no valid grouping is possible.

### Example 2
Input: `nums = [1, 1, 1, 1, 2, 1, 2, 2, 2, 2]`
Output: `"True"`
Explanation: Can be divided into two groups -- the first group has five 1s and the second group has five 2s.

### Example 3
Input: `nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]`
Output: `"True"`
Explanation: Can be divided into two groups, each containing five 5s.

## Solution Approach

This problem can be solved with the following steps:

1. **Basic Check**
   - First check if the total number of pieces is divisible by 5
   - If not, it is impossible to divide all pieces into groups of 5, so return `"False"` immediately

2. **Frequency Counting**
   - Use a dictionary to count the occurrences of each number
   - Traverse the input array and record the frequency of each number

3. **Grouping Validation**
   - Check if each number's occurrence count is a multiple of 5
   - If any number's count is not a multiple of 5, return `"False"`
   - If all numbers' counts are multiples of 5, return `"True"`

## Implementation

```python
def solution(nums: list[int]) -> str:
    # If the total count is not divisible by 5, return False directly
    if len(nums) % 5 != 0:
        return "False"
    
    # Count the occurrences of each number
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Check if each number's occurrence count is a multiple of 5
    for count in count_dict.values():
        if count % 5 != 0:
            return "False"
    
    return "True"
```

## Code Explanation

1. `if len(nums) % 5 != 0:`
   - First check if the input array length is divisible by 5
   - This is a necessary prerequisite since each group must have exactly 5 pieces

2. `count_dict = {}`
   - Create an empty dictionary to count occurrences of each number
   - A dictionary allows fast lookup and update of counts

3. `count_dict[num] = count_dict.get(num, 0) + 1`
   - Use `dict.get()` to safely retrieve and update the count
   - If the number does not exist, the default value is 0, then add 1
   - If the number already exists, get the current count and add 1

4. The final check loop
   - Iterate over all count values in the dictionary
   - Check if each count is divisible by 5
   - If any count is not divisible by 5, return `"False"`
   - Return `"True"` only if all checks pass

## Complexity Analysis

- Time Complexity: O(n), where n is the length of the input array
  - One pass through the array to count frequencies
  - One pass through the dictionary to check count values
- Space Complexity: O(k), where k is the number of distinct numbers
  - A dictionary is needed to store the occurrence count of each number

## Summary

1. The return value is a string `"True"` or `"False"`, not a boolean
2. The input array may be very large, but the solution has linear time complexity and handles it efficiently
3. Actual grouping is not needed -- only determining whether grouping is possible
