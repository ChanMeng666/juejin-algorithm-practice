# String Prefix Transformation

## Problem Description

Little U and Little R have two strings S and T. Little U needs to perform a series of operations on S to make it a prefix of T.
The allowed operations are:
1. Modify a character in S
2. Delete the last character of S

Calculate the minimum number of operations needed to make S a prefix of T.

## Examples

### Example 1:
```
Input: S = "aba", T = "abb"
Output: 1
Explanation: Only need to change the last 'a' to 'b'
```

### Example 2:
```
Input: S = "abcd", T = "efg"
Output: 4
Explanation: Need to modify 3 characters ('a'->'e', 'b'->'f', 'c'->'g') and delete 'd', totaling 4 operations
```

### Example 3:
```
Input: S = "xyz", T = "xy"
Output: 1
Explanation: Only need to delete the last character 'z'
```

### Example 4:
```
Input: S = "hello", T = "helloworld"
Output: 0
Explanation: S is already a prefix of T, no operations needed
```

### Example 5:
```
Input: S = "same", T = "same"
Output: 0
Explanation: The two strings are identical, no operations needed
```

## Solution Approach

1. First, handle the special case: if S is already a prefix of T, no operations are needed; return 0 directly.

2. Then, handle two cases based on the length relationship between S and T:

   - When S is longer than T:
     * Need to delete the extra characters (delete count = length of S - length of T)
     * Also need to modify mismatched characters (among the first T.length characters)

   - When S is shorter than or equal to T:
     * Only need to count the number of characters that need to be modified
     * Count by comparing whether characters at corresponding positions are the same

3. Return the total number of operations needed.

## Implementation

```python
def solution(S: str, T: str) -> int:
    # If S is already a prefix of T, return 0 directly
    if T.startswith(S):
        return 0

    # Get the lengths of both strings
    s_len = len(S)
    t_len = len(T)

    # If S is longer than T, we need to delete the extra characters
    if s_len > t_len:
        # First calculate the number of characters to delete
        delete_count = s_len - t_len
        # Then calculate the number of characters to modify among the first t_len characters
        change_count = sum(1 for i in range(t_len) if S[i] != T[i])
        return delete_count + change_count

    # If S is shorter than or equal to T, only calculate the number of characters to modify
    return sum(1 for i in range(s_len) if S[i] != T[i])
```

## Code Explanation

1. `T.startswith(S)`: Check if S is already a prefix of T
   - If so, return 0 directly since no operations are needed

2. Handling when S is longer than T:
   ```python
   if s_len > t_len:
       delete_count = s_len - t_len
       change_count = sum(1 for i in range(t_len) if S[i] != T[i])
       return delete_count + change_count
   ```
   - `delete_count` calculates the number of characters to delete
   - `change_count` uses a generator expression to count the number of characters to modify
   - Returns the sum of both types of operations

3. Handling when S is shorter than or equal to T:
   ```python
   return sum(1 for i in range(s_len) if S[i] != T[i])
   ```
   - Only need to count the number of mismatched characters
   - Uses a generator expression to count the number of characters that need modification

## Complexity Analysis

- Time Complexity: O(min(len(S), len(T)))
  - Only needs to traverse the length of the shorter string
  - The startswith() function also has O(min(len(S), len(T))) complexity

- Space Complexity: O(1)
  - Only uses a few variables to store lengths and counts
  - No additional data structures are used

## Summary

This problem mainly tests string operations and basic programming logic. The keys to solving it are:
1. Correctly understanding the concept of "prefix"
2. Case-by-case analysis (when S is longer than T vs. when S is not longer than T)
3. Identifying the types of operations needed (modify and delete)
4. Using concise Python syntax for counting

Through this problem, we can learn:
- Methods for string prefix checking
- Use of generator expressions in Python
- How to decompose complex problems into simpler sub-problems
