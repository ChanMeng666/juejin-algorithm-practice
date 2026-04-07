# Restore Original String

## Problem Description

Given a string F, this string was constructed from some initial string S using the following rule:

- Choose an integer K (where 0 <= K < |S|, |S| denotes the length of string S)
- Append the substring of S from position K (0-indexed) to the end of S, i.e., S = S + S[K:]

Now given the final string F, find the shortest possible initial string S.

### Requirements

- Find the shortest initial string that can produce the given final string through repeated application of the above operation.

### Constraints

- The input is a string containing only lowercase letters, with a length not exceeding 1000.
- If no valid initial string can produce the input through the described operations, return the original string F.

## Examples

### Example 1:
```
Input: str1 = "abbabbbabb"
Output: "ab"
Explanation: The initial string "ab" can produce the final string through the following steps:
K = 1: "ab" -> "abb"
K = 0: "abb" -> "abbabb"
K = 2: "abbabb" -> "abbabbbabb"
```

### Example 2:
```
Input: str1 = "abbbabbbb"
Output: "ab"
```

## Solution Approach

1. **Core Idea**:
   - Start from the shortest possible length (from 1) and find the shortest initial string that can construct the target string through the described operations.
   - For each possible initial string length, take the prefix of the original string as the candidate initial string.

2. **Implementation Details**:
   - Use Breadth-First Search (BFS) to try all possible operation sequences.
   - For each state, try all possible K values (from 0 to current string length - 1).
   - Use a set to track intermediate states already tried, avoiding redundant computation.
   - Ensure that each generated intermediate string is a prefix of the target string.

3. **Optimization Strategies**:
   - Use a `seen` set to avoid duplicate states.
   - Limit the number of operation steps to the length of the original string to prevent infinite loops.
   - Use `startswith` to ensure intermediate results are always a prefix of the target string.

## Implementation

```python
def solution(str1):
    # Start trying from the shortest possible substring
    n = len(str1)
    for i in range(1, n + 1):
        # Take the first i characters as the candidate initial string
        candidate = str1[:i]
        current = candidate

        # Track strings already tried to avoid cycles
        seen = {current}
        queue = [(current, 0)]  # (current string, number of steps used)

        while queue:
            current, steps = queue.pop(0)
            if current == str1:
                return candidate

            if steps >= n:  # Prevent infinite loop
                break

            # Try all possible values of K
            for k in range(len(current)):
                # Append the substring starting from position k to the end
                next_str = current + current[k:]
                if len(next_str) <= len(str1) and next_str not in seen and str1.startswith(next_str):
                    seen.add(next_str)
                    queue.append((next_str, steps + 1))

    return str1
```

## Complexity Analysis

- **Time Complexity**: O(n^2), where n is the length of the input string. For each possible initial string length, multiple operation steps need to be tried.
- **Space Complexity**: O(n), mainly used for storing the queue and the set of visited states.

## Summary

This problem uses BFS to explore all possible construction paths from candidate initial strings of increasing length. Key optimizations include prefix checking to prune invalid paths and state deduplication to avoid redundant computation. The algorithm guarantees finding the shortest initial string by trying candidates in order of increasing length.
