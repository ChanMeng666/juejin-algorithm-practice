# DNA Sequence Edit Distance

## Problem Description

Given two DNA sequences, write a function to calculate the minimum number of editing steps required to transform a damaged DNA sequence (dna1) into an undamaged sequence (dna2).

The available editing operations are:
1. Insert a base
2. Delete a base
3. Replace a base

### Constraints

- DNA sequences consist of characters A, C, G, T

## Examples

```python
Input: dna1 = "AGT", dna2 = "AGCT"
Output: 1
Explanation: Only one insertion of 'C' is needed

Input: dna1 = "AACCGGTT", dna2 = "AACCTTGG"
Output: 4
Explanation: Four replacement operations are needed

Input: dna1 = "ACGT", dna2 = "TGC"
Output: 3
Explanation: One deletion and two replacements are needed
```

## Solution Approach

This is a classic edit distance (Levenshtein Distance) problem. We can solve it using dynamic programming.

### 1. DP State Definition

- Create a 2D array `dp[i][j]`
- `dp[i][j]` represents the minimum number of operations needed to transform the first i characters of dna1 into the first j characters of dna2

### 2. State Transition Equation

For each position (i, j), we need to consider:

1. If the current characters are the same (dna1[i-1] == dna2[j-1]):
   ```python
   dp[i][j] = dp[i-1][j-1]  # No operation needed
   ```

2. If the current characters differ, take the minimum of three operations:
   ```python
   dp[i][j] = min(
       dp[i-1][j-1] + 1,  # Replace operation
       dp[i-1][j] + 1,    # Delete operation
       dp[i][j-1] + 1     # Insert operation
   )
   ```

### 3. Initialization

- First row: `dp[0][j]` represents the number of operations to transform an empty string into a string of length j (i.e., j insertions)
- First column: `dp[i][0]` represents the number of operations to transform a string of length i into an empty string (i.e., i deletions)

## Implementation

```python
def solution(dna1, dna2):
    # Create the dynamic programming matrix
    m, n = len(dna1), len(dna2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill in the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1] + 1,  # Replace
                    dp[i-1][j] + 1,    # Delete
                    dp[i][j-1] + 1     # Insert
                )
    
    return dp[m][n]
```

## Code Explanation

Taking dna1 = "AGT", dna2 = "AGCT" as an example:

1. Initial state:
```
  '' A G C T
'' 0 1 2 3 4
A  1
G  2
T  3
```

2. After dynamic programming fills in the table:
```
  '' A G C T
'' 0 1 2 3 4
A  1 0 1 2 3
G  2 1 0 1 2
T  3 2 1 1 1
```

3. The final answer is dp[3][4] = 1, meaning only 1 operation is needed (inserting 'C' between "G" and "T")

## Complexity Analysis

- Time complexity: O(mn), where m and n are the lengths of the two DNA sequences respectively
- Space complexity: O(mn), a 2D array is needed to store intermediate states

## Summary

This problem is a variant of the edit distance problem that can be efficiently solved using dynamic programming. The key points are:

1. Correctly defining the state transition equation
2. Properly handling boundary cases (initialization)
3. Understanding how the three operations (insert, delete, replace) affect state transitions

Mastering this solution is very helpful for understanding dynamic programming. Similar problems include string matching, sequence alignment, and more.
