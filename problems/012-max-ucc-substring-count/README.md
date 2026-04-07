# Maximum UCC Substring Count

## Problem Description

Given a string `s` consisting only of characters 'U' and 'C', and an integer `m`. Your task is to find the maximum number of "UCC" substrings that can be formed through at most `m` edit operations.

An edit operation can be one of the following:
1. Insert a character ('U' or 'C') at any position in the string
2. Delete a character from the string
3. Replace a character in the string with another character ('U' or 'C')

## Solution Approach

The solution to this problem uses a greedy algorithm. Here is the Python code to efficiently solve this problem:

```python
def solution(m: int, s: str) -> int:
    ls = s.split("UCC")
    ans = len(ls) - 1
    c1 = c2 = 0
    for s in ls:
        i = 0
        k = len(s)
        while i < k:
            if i + 1 < k and s[i + 1] == 'C':
                i += 2
                c1 += 1
            else:
                i += 1
                c2 += 1
    k1 = min(m, c1)
    m -= k1
    ans += k1
    k2 = min(m >> 1, c2)
    ans += k2
    m -= k2 * 2
    ans += m // 3
    return ans
```

## Code Explanation

Let's break down the solution step by step:

1. First, we split the string `s` by "UCC". The number of existing "UCC" substrings in `s` is `len(ls) - 1`.

2. Then, we iterate through each substring in `ls`, counting two types of patterns:
   - `c1`: Number of 'UC' patterns (requires 1 edit to become "UCC")
   - `c2`: Number of single characters (requires 2 edits to become "UCC")

3. We use the remaining edits `m` in the following order:
   - Convert 'UC' to "UCC" (costs 1 edit each)
   - Convert single characters to "UCC" (costs 2 edits each)
   - Create new "UCC" from scratch (costs 3 edits each)

4. We calculate:
   - `k1 = min(m, c1)`: How many 'UC' patterns we can convert to "UCC"
   - `k2 = min(m >> 1, c2)`: How many single characters we can convert to "UCC" (m >> 1 is equivalent to m // 2)
   - Remaining edits `m // 3`: How many new "UCC" substrings we can create from scratch

5. The final answer is the sum of:
   - Initial "UCC" count
   - "UCC" substrings converted from 'UC' patterns
   - "UCC" substrings converted from single characters
   - Newly created "UCC" substrings from scratch

This greedy approach ensures that we maximize the number of "UCC" substrings with the given number of edits.

## Complexity Analysis

- Time Complexity: O(n), where n is the length of string `s`
- Space Complexity: O(n), due to the split operation

## Examples

Let's take the example: `s = "UCUUCCCCC"` and `m = 3`

1. Split by "UCC": `ls = ["UC", "CCCCC"]`, `ans = 1` (initial count)
2. Count patterns:
   - In "UC": `c1 = 1`, `c2 = 0`
   - In "CCCCC": `c1 = 2`, `c2 = 1`
   - Total: `c1 = 3`, `c2 = 1`
3. Use edits:
   - Convert 3 'UC' to "UCC": `k1 = min(3, 3) = 3`, `m = 0`
   - No remaining edits for other operations
4. Final count: `1 + 3 = 4`

Therefore, the maximum number of "UCC" substrings that can be formed is 4.

This solution efficiently handles various cases and optimally uses the given edit operations to maximize the "UCC" substring count.
