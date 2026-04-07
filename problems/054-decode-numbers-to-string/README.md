# Decode Numbers to String

## Problem Description

Given a number, translate it into a string according to the following rules:
- 0 translates to "a"
- 1 translates to "b"
- 2 translates to "c"
- ...
- 25 translates to "z"

A number may have multiple translation methods. Write a function to calculate how many different translation methods a number has.

### Constraints

- The input is a non-negative integer.
- Digits can be translated individually or in pairs (if the pair forms a number between 10 and 25).

## Examples

```
Input: 12258
Output: 5
Explanation: 12258 has 5 different translations: "bccfi", "bwfi", "bczi", "mcfi", and "mzi"
```

## Solution Approach

### 1. Problem Analysis

This is a classic dynamic programming problem. For each digit, there are two translation choices:
1. Translate the digit individually
2. Combine it with the next digit for translation (if the combined number is between 0-25)

### 2. Dynamic Programming Design

1. **State Definition**:
   - Let dp[i] represent the number of translation methods from position i to the last digit
   - dp[n] = 1, meaning an empty string has exactly one translation method

2. **State Transition**:
   - If the current digit is 0: dp[i] = dp[i+1] (0 cannot be translated alone)
   - If the current digit is not 0:
     - dp[i] = dp[i+1] (translate the current digit alone)
     - If the current digit combined with the next digit falls in range 10-25: dp[i] += dp[i+2]

3. **Special Case Handling**:
   - When encountering 0, it cannot be translated alone; it can only be combined with the previous digit
   - Two-digit combinations must be in the range 10-25 to be valid

### 3. Detailed Example

Using 12258 as an example, here is the dynamic programming process:

1. Traverse from right to left:
   - 8: can be translated alone as "i"
   - 5: can be translated alone as "f"
   - 2: can be translated alone as "c", or combined with 5 as "z"
   - 2: can be translated alone as "c", or combined with 2 as "w"
   - 1: can be translated alone as "b", or combined with 2 as "m"

2. The final 5 translation methods are:
   - b + c + c + f + i = "bccfi"
   - b + w + f + i = "bwfi"
   - b + c + z + i = "bczi"
   - m + c + f + i = "mcfi"
   - m + z + i = "mzi"

## Implementation

```python
def solution(num):
    s = str(num)
    n = len(s)

    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n-1, -1, -1):
        if s[i] == '0':
            dp[i] = dp[i+1]
            continue

        dp[i] = dp[i+1]

        if i < n-1:
            num2 = int(s[i:i+2])
            if 10 <= num2 <= 25:
                dp[i] += dp[i+2]

    return dp[0]
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the number of digits
- **Space Complexity**: O(n), a dp array is needed to store intermediate states

## Summary

Q: Why traverse from right to left?
A: Traversing from right to left makes state transitions more convenient, since the number of translation methods at each position depends on the results of subsequent positions.

Q: How to handle the digit 0?
A: The digit 0 cannot be translated alone; it simply inherits the translation count from the next position. This is because 0 does not correspond to any letter on its own.

Q: Why use dp[n] = 1 as the initial value?
A: dp[n] represents the number of translation methods for an empty string. An empty string has exactly one translation method (no translation), so it is set to 1. This serves as the boundary condition for the dynamic programming.
