# Binary String Flip Optimization

## Problem Description

Given a binary string of length `n`, you can perform the following operations to maximize your total score:

1. **Replace "00" with "0"**: Removes a consecutive pair of zeros and replaces it with a single zero, earning `a` points. This is considered an "odd" operation.
2. **Replace "11" with "1"**: Removes a consecutive pair of ones and replaces it with a single one, earning `b` points. This is considered an "even" operation.
3. **Delete a "0"**: Removes a single zero from the string, costing `c` points (negative score). This is considered an "odd" operation.

The constraint is that you cannot perform two consecutive operations of the same parity (two odd operations in a row or two even operations in a row). The goal is to find the maximum score achievable.

### Constraints

- `n`: length of the binary string (1 <= n <= small number based on DP approach)
- `a`: score gained from replacing "00" with "0"
- `b`: score gained from replacing "11" with "1"
- `c`: score lost from deleting a "0"
- `s`: a binary string consisting of '0' and '1'

## Examples

**Example 1:**
```
Input: n=5, a=2, b=2, c=1, s="01101"
Output: 3
```

**Example 2:**
```
Input: n=6, a=4, b=3, c=5, s="110001"
Output: 11
```

**Example 3:**
```
Input: n=6, a=3, b=2, c=1, s="011110"
Output: 4
```

**Example 4:**
```
Input: n=4, a=1, b=3, c=2, s="1111"
Output: 3
```

**Example 5:**
```
Input: n=3, a=2, b=2, c=1, s="000"
Output: 2
```

## Solution Approach

The solution uses **dynamic programming** with a 3-dimensional state:

- `dp[i][j][k]` represents the maximum score when processing up to the `i`-th character, where `j` is the parity of the last operation performed (0 = even, 1 = odd), and `k` is the current character value (0 or 1).

At each position, the algorithm considers four possible actions:

1. **Replace "00" with "0"** (odd operation): If the current and next characters are both '0' and the last operation was not odd, gain `a` points and advance by 2 positions.
2. **Replace "11" with "1"** (even operation): If the current and next characters are both '1' and the last operation was not even, gain `b` points and advance by 2 positions.
3. **Delete "0"** (odd operation): If the current character is '0' and the last operation was not odd, lose `c` points and advance by 1 position.
4. **Skip**: Keep the current character unchanged and move to the next position without changing parity state.

The answer is the maximum value across all states at position `n`.

## Implementation

```python
def solution(n, a, b, c, s):
    dp = [[[-float('inf')] * 2 for _ in range(2)] for _ in range(n + 1)]
    
    dp[0][0][0] = dp[0][1][0] = 0
    dp[0][0][1] = dp[0][1][1] = 0
    
    for i in range(n):
        curr = int(s[i])
        for last in range(2):
            for state in range(2):
                if dp[i][last][state] == -float('inf'):
                    continue
                    
                if i < n-1 and curr == 0 and int(s[i+1]) == 0:
                    if last != 1:
                        dp[i+2][1][0] = max(dp[i+2][1][0], dp[i][last][state] + a)
                
                if i < n-1 and curr == 1 and int(s[i+1]) == 1:
                    if last != 0:
                        dp[i+2][0][1] = max(dp[i+2][0][1], dp[i][last][state] + b)
                
                if curr == 0:
                    if last != 1:
                        dp[i+1][1][int(s[i+1]) if i+1 < n else 0] = max(
                            dp[i+1][1][int(s[i+1]) if i+1 < n else 0], 
                            dp[i][last][state] - c
                        )
                
                if i+1 < n:
                    dp[i+1][last][int(s[i+1])] = max(
                        dp[i+1][last][int(s[i+1])], 
                        dp[i][last][state]
                    )
    
    result = -float('inf')
    for last in range(2):
        for state in range(2):
            result = max(result, dp[n][last][state])
    
    return result
```

## Complexity Analysis

- **Time Complexity**: O(n) -- iterates through each position once with a constant number of state transitions (2 x 2 states per position).
- **Space Complexity**: O(n) -- the DP table has dimensions (n+1) x 2 x 2.

## Summary

This problem is solved using dynamic programming with a 3D state tracking position, operation parity, and current character value. The parity constraint prevents consecutive same-type operations, making the state transition carefully alternate between odd and even operations. The algorithm efficiently explores all valid operation sequences to maximize the total score.
