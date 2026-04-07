# Smallest Non-Palindrome

## Problem Description

Given a string `s` consisting of lowercase letters, find the largest palindrome string that is strictly smaller than `s` in lexicographic order. If no such palindrome exists, return `"-1"`.

### Requirements

- The result must be a palindrome
- The result must be strictly less than the input string in lexicographic order
- Among all valid palindromes, return the largest one (closest to the original string)
- If no valid palindrome exists, return `"-1"`

### Constraints

- The input string consists of lowercase English letters
- If the input is already a palindrome, return `"-1"` (no smaller palindrome of the same structure can be formed)

## Examples

**Example 1:**
```
Input: s = "abc"
Output: "aba"
Explanation: "aba" is a palindrome and is lexicographically smaller than "abc"
```

**Example 2:**
```
Input: s = "cba"
Output: "cac"
Explanation: "cac" is a palindrome and is lexicographically smaller than "cba"
```

**Example 3:**
```
Input: s = "aaa"
Output: "-1"
Explanation: "aaa" is already a palindrome and no smaller palindrome exists
```

## Solution Approach

The algorithm works by trying to construct the largest palindrome that is smaller than the input string:

1. **Palindrome check**: If the input string is already a palindrome, return `"-1"` since we cannot form a smaller palindrome by mirroring.

2. **Scan symmetric positions**: Iterate from the outermost positions inward. When two symmetric characters differ:
   - Take the larger character and set both symmetric positions to it, making a palindrome. If this result is less than the original, return it.
   - Otherwise, set both positions to one character below the larger one and return the result.

3. **Handle the middle character**: For odd-length strings that are nearly symmetric, decrement the middle character if possible.

## Implementation

```python
def solution(s: str) -> str:
    n = len(s)
    # If the string itself is a palindrome, return '-1'
    if s == s[::-1]:
        return '-1'
        
    # Convert the string to a list for modification
    t = list(s)
    
    # Iterate through each position from left to right
    for i in range(n):
        j = n - 1 - i  # Symmetric position
        
        if i >= j:
            break
            
        if s[i] != s[j]:
            max_char = max(s[i], s[j])
            t[i] = t[j] = max_char
            temp = ''.join(t)
            if temp < s:
                return temp
            t[i] = t[j] = chr(ord(max_char) - 1)
            return ''.join(t)
    
    # If the string is mostly symmetric, modify the middle character
    mid = n // 2
    if n % 2 == 1:
        if t[mid] > 'a':
            t[mid] = chr(ord(t[mid]) - 1)
            return ''.join(t)
    
    return '-1'
```

## Complexity Analysis

- **Time complexity**: O(n), where n is the length of the string. We iterate through at most half the string to find the first mismatch.
- **Space complexity**: O(n), for storing the character list copy of the string.

## Summary

This problem requires constructing the largest palindrome smaller than the given string. The key insight is to identify the first pair of mismatched symmetric characters and adjust them to form a valid palindrome. Special handling is needed for strings that are already palindromes (return `"-1"`) and for odd-length strings where the middle character can be decremented.
