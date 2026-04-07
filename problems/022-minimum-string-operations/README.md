# Minimum String Operations

## Problem Description

Given a string S containing only lowercase letters, you can perform the following operation: choose two identical characters in the string and delete them, then append any lowercase letter to the end of the string. What is the minimum number of operations needed to make all characters in the string unique?

### Constraints

- S contains only lowercase letters

## Examples

### Example 1:
- Input: S = "abab"
- Output: 2
- Explanation:
  1. First operation: delete two 'a's, append a new character, e.g. 'c', resulting in "bbc"
  2. Second operation: delete two 'b's, append a new character, e.g. 'd', resulting in "cd"
  3. All characters are now unique, operations complete

### Example 2:
- Input: S = "aaaa"
- Output: 2
- Explanation:
  1. First operation: delete two 'a's, append a new character, e.g. 'b', resulting in "aab"
  2. Second operation: delete two 'a's, append a new character, e.g. 'c', resulting in "bc"
  3. All characters are now unique, operations complete

### Example 3:
- Input: S = "abcabc"
- Output: 3
- Explanation: One operation is needed for each pair of duplicate characters ('a', 'b', 'c')

## Solution Approach

1. **Problem Analysis**
   - Each operation can delete two identical characters
   - Then any new character can be appended
   - The goal is to make all characters in the final string unique
   - Find the minimum number of operations

2. **Key Insight**
   - For each character that appears multiple times, we need to reduce its count through operations
   - Each operation handles two identical characters
   - We don't need to worry about what new character to append, since we can always choose a character not currently in the string

3. **Solution**
   - First count the occurrences of each character
   - For each character appearing more than once, operations are needed
   - Every two identical characters require one operation
   - Therefore, for a character appearing n times, n/2 (floor division) operations are needed

## Implementation

```python
def solution(S: str) -> int:
    # Count the occurrences of each character
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1
    
    operations = 0
    # For each character that appears more than once
    for count in char_count.values():
        # Each operation removes 2 characters, so we need count//2 operations
        operations += count // 2
            
    return operations
```

## Complexity Analysis

- Time complexity: O(n), where n is the length of the string
  - One pass through the string to count character frequencies
  - One pass through the frequency dictionary

- Space complexity: O(k), where k is the character set size
  - A hash map is needed to store character frequencies
  - Since only lowercase letters are used, k <= 26

## Summary

The key to this problem is understanding that:
1. There is no need to actually simulate the string modification process
2. We only need to count the number of operations needed for each duplicate character
3. The total number of operations is the sum of operations needed for all duplicate characters
4. For each character, every two occurrences require one operation

This way, we can directly calculate the minimum number of operations needed without actually performing the string modifications.
