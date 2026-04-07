# String Replacement

## Problem Description

Given a string `s`, write a function that replaces all occurrences of the lowercase letter `a` with `"%100"` and returns the resulting string.

## Examples

### Example 1:
- Input: `s = "abcdwa"`
- Output: `"%100bcdw%100"`
- Explanation: The string has two 'a' characters, both replaced with "%100".

### Example 2:
- Input: `s = "banana"`
- Output: `"b%100n%100n%100"`
- Explanation: The string has three 'a' characters, all replaced with "%100".

### Example 3:
- Input: `s = "apple"`
- Output: `"%100pple"`
- Explanation: The string has only one 'a', replaced with "%100".

## Solution Approach

This is a simple string replacement problem that can be solved as follows:

1. Use Python's built-in string method `replace()`.
2. The `replace()` method accepts two parameters:
   - The character to be replaced (here, 'a')
   - The replacement string (here, '%100')
3. The method automatically handles all matching characters in the string.

## Implementation

```python
def solution(s: str) -> str:
    return s.replace('a', '%100')
```

## Code Explanation

1. The function takes a string parameter `s`.
2. It uses the `replace()` method to replace all occurrences of 'a' with '%100'.
3. The result is returned directly.

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the string.
- **Space Complexity**: O(n), a new string is created to store the result.

## Summary

This problem leverages Python's built-in `replace()` method for a clean one-line solution. The replacement is global (all occurrences are replaced), case-sensitive (only lowercase 'a' is affected), and produces a new string since Python strings are immutable.
