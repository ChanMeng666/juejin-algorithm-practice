# Balanced ASDF String

## Problem Description

Given a string consisting only of the characters 'A', 'S', 'D', and 'F', find the minimum number of character replacements needed to make the string balanced. A string is considered balanced when each of the four characters appears exactly the same number of times (i.e., string length / 4 times each).

### Requirements

- Each replacement operation changes one character in a substring to another character among 'A', 'S', 'D', 'F'.
- Find the minimum number of replacements to achieve a balanced string.

### Constraints

- The string length must be a multiple of 4.
- The string contains only characters 'A', 'S', 'D', and 'F'.

## Examples

```
Input: "ADDF"
Output: 1
Explanation: Replace one 'D' with 'S' to get "ADFS" (each character appears once).

Input: "ASAFASAFADDD"
Output: 3

Input: "SSDDFFFFAAAS"
Output: 1

Input: "AAAASSSSDDDDFFFF"
Output: 0
Explanation: Already balanced (each character appears 4 times).

Input: "AAAADDDDAAAASSSS"
Output: 4
```

## Solution Approach

1. **Character Frequency Analysis**: Count the frequency of each character in the substring.
2. **Calculate Excess Characters**: For each character whose frequency exceeds the target (length / 4), compute how many need to be changed.
3. **Replacement Pairing**: Each replacement handles two characters (one excess is replaced to fill a deficit), so divide the total changes by 2 (rounding up for odd totals).
4. **Brute Force Substring Search**: Iterate over all substrings whose length is a multiple of 4 and find the one requiring the fewest changes.

## Implementation

```python
def get_min_changes(freq):
    length = sum(freq.values())
    target = length // 4

    total_changes = 0
    for f in freq.values():
        if f > target:
            total_changes += f - target

    return (total_changes + 1) // 2

def check_substring(s):
    freq = {'A': 0, 'S': 0, 'D': 0, 'F': 0}
    for c in s:
        freq[c] += 1
    return get_min_changes(freq)

def solution(input):
    n = len(input)
    if n % 4 != 0:
        return -1

    min_changes = n

    for i in range(len(input)):
        for j in range(i + 3, len(input)):
            if (j - i + 1) % 4 == 0:
                curr_changes = check_substring(input[i:j+1])
                if curr_changes < min_changes:
                    min_changes = curr_changes

                if min_changes == 0:
                    return 0

    return min_changes
```

## Complexity Analysis

- **Time Complexity**: O(n^3), where n is the length of the string. Iterating over all substrings is O(n^2), and counting frequencies for each is O(n).
- **Space Complexity**: O(1), only a fixed-size frequency dictionary is used.

## Summary

This problem uses a brute-force approach to examine all substrings of valid length (multiples of 4) and calculates the minimum number of replacements needed to balance each one. The key insight is that each replacement fixes two imbalanced characters simultaneously, so the total excess count is halved (with rounding up).
