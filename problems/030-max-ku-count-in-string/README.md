# Maximum "ku" Count in String

## Problem Description

Given a string s containing only uppercase and lowercase English letters, calculate the maximum number of "ku" strings that can be formed from the characters. Each time, you can randomly pick a character from the string, and once selected, that character cannot be reused. Letter case is ignored, meaning uppercase and lowercase letters are treated as the same.

### Constraints

- The string contains only English letters (uppercase and lowercase)

## Examples

**Example 1:**
- Input: s = "AUBTMKAxfuu"
- Output: 1
- Explanation: The string contains 1 'k' (K) and 2 'u's, so at most 1 "ku" can be formed

**Example 2:**
- Input: s = "KKuuUuUuKKKKkkkkKK"
- Output: 6
- Explanation: The string contains 12 'k's (K) and 6 'u's (U), so at most 6 "ku" can be formed

**Example 3:**
- Input: s = "abcdefgh"
- Output: 0
- Explanation: The string contains no 'k' or 'u', so no "ku" can be formed

## Solution Approach

This problem can be solved with the following steps:

1. **Case Handling**
   - The problem states that letter case is ignored, so we first convert the entire string to lowercase using Python's `lower()` method

2. **Character Counting**
   - Count the number of 'k' and 'u' characters in the string
   - Use Python's `count()` method for direct counting
   - Store the counts as k_count and u_count

3. **Result Calculation**
   - To form one "ku", one 'k' and one 'u' are needed
   - The number of "ku" that can be formed is limited by whichever character has fewer occurrences
   - Use the `min()` function to return the smaller of the two counts

## Implementation

```python
def solution(s: str) -> int:
    # Convert the string to lowercase so we don't need to handle upper and lower case separately
    s = s.lower()
    
    # Count the occurrences of 'k' and 'u' respectively
    k_count = s.count('k')
    u_count = s.count('u')
    
    # The number of "ku" pairs that can be formed depends on whichever count is smaller
    return min(k_count, u_count)
```

## Complexity Analysis

- Time complexity: O(n), where n is the length of the string. One pass is needed for case conversion, then two more passes to count character occurrences.
- Space complexity: O(n), needed to store the converted lowercase string.

## Code Explanation

1. `s.lower()`: Converts the string to lowercase, unifying the handling of upper and lowercase letters.
2. `s.count('k')`: Counts the number of lowercase 'k' characters in the string.
3. `s.count('u')`: Counts the number of lowercase 'u' characters in the string.
4. `min(k_count, u_count)`: Returns the smaller of the two values, which is the maximum number of "ku" that can be formed.

## Summary

1. Don't forget to handle the case sensitivity issue; the problem explicitly states that uppercase and lowercase letters are treated as the same.
2. Don't try to use a complex method to match the "ku" string. Since the problem allows randomly picking characters, you only need to count individual character occurrences.
3. The final result depends on the character with fewer occurrences, not the sum or product of the two counts.
