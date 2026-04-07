# Lexicographically Smallest String

## Problem Description

Little U has a string consisting of 0s and 1s. She can perform at most k operations, where each operation swaps two adjacent characters. The goal is to obtain the lexicographically smallest string through these operations.

For example, Little U currently has the string 01010 and can perform at most 2 adjacent character swap operations. Through these operations, she can rearrange the string to 00101, which is the lexicographically smallest string achievable with no more than 2 operations.

### Requirements
- n: String length
- k: Maximum number of swap operations allowed
- s: Initial string

### Constraints
Return the lexicographically smallest string achievable after at most k operations.

## Examples
```python
Input: n = 5, k = 2, s = "01010"
Output: '00101'

Input: n = 7, k = 3, s = "1101001"
Output: '0110101'

Input: n = 4, k = 1, s = "1001"
Output: '0101'
```

## Solution Approach

This is a greedy algorithm problem. We need to move character '0' to the front of the string as much as possible within the limited k operations to obtain the lexicographically smallest string.

Key idea:
1. Traverse each position of the string from left to right
2. For each position, search for a '0' within k steps after the current position
3. If a '0' is found, move it to the current position through adjacent swaps
4. Update the remaining number of operations after each move

## Implementation

```python
def solution(n: int, k: int, s: str) -> str:
    # Convert the string to a list for easy modification
    s = list(s)
    remaining_moves = k

    # Iterate through each position in the string
    for i in range(n):
        if remaining_moves == 0:
            break

        # Find the nearest 0 after the current position
        min_pos = i
        for j in range(i + 1, min(i + remaining_moves + 1, n)):
            if s[j] == '0':
                min_pos = j
                break

        # If a 0 is found, move it to the current position
        if min_pos != i and s[min_pos] == '0':
            # Calculate the number of moves needed
            moves_needed = min_pos - i
            if moves_needed <= remaining_moves:
                # Move the 0 forward to position i
                for j in range(min_pos, i, -1):
                    s[j], s[j-1] = s[j-1], s[j]
                remaining_moves -= moves_needed

    return ''.join(s)
```

## Code Explanation

1. **Initialization**:
   - Convert the input string to a list for convenient character swapping
   - Use remaining_moves to track the remaining number of available operations

2. **Main Loop**:
   - Traverse each position i of the string from left to right
   - Exit the loop if no remaining operations are available

3. **Finding the Nearest '0'**:
   - Search for the nearest '0' after the current position, within the reachable range (i + remaining_moves + 1)
   - Record the position of the found '0' as min_pos

4. **Move Operation**:
   - If a '0' is found and it is not at the current position:
     - Calculate the number of moves needed (moves_needed)
     - If moves_needed does not exceed the remaining operations:
       - Move the '0' to position i through consecutive adjacent swaps
       - Update the remaining number of operations

5. **Return Result**:
   - Convert the processed list back to a string and return it

## Complexity Analysis

- Time Complexity: O(n*k), where n is the string length and k is the maximum number of operations
- Space Complexity: O(n), for converting the string to a list

## Summary
1. Make sure to check if the remaining operations are sufficient for the move
2. Always select the nearest '0' within the reachable range to move
3. Do not forget to update the remaining number of operations
4. Consider edge cases: k=0 or the string is already optimal
