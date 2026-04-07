# DNA Edit Distance

## Problem Description

Paleontologist U is studying the evolutionary relationships between different species. To analyze how closely related two ancient organisms are, she needs to compare their DNA sequences. DNA is composed of four nucleotides: A, C, G, and T, and may undergo three types of mutations:
1. Add a nucleotide
2. Delete a nucleotide
3. Replace a nucleotide

She believes that the minimum number of mutations between two DNA sequences can reflect their evolutionary relationship: the fewer mutations, the closer the relationship.

### Requirements

- `dna1`: the first DNA sequence
- `dna2`: the second DNA sequence

### Constraints

- Return the minimum number of mutations needed to transform `dna1` into `dna2`

## Examples

1. `dna1 = "AGT", dna2 = "AGCT"` -> Output: 1
2. `dna1 = "AACCGGTT", dna2 = "AACCTTGG"` -> Output: 4
3. `dna1 = "ACGT", dna2 = "TGC"` -> Output: 3
4. `dna1 = "", dna2 = "ACGT"` -> Output: 4
5. `dna1 = "GGGG", dna2 = "TTTT"` -> Output: 4

## Solution Approach

This is a variant of the classic Edit Distance (Levenshtein Distance) problem. We use dynamic programming to solve it.

### 1. DP State Definition

Create a 2D array `dp`, where:
- `dp[i][j]` represents the minimum number of operations to transform the first `i` characters of `dna1` into the first `j` characters of `dna2`

### 2. State Transition Equation

For each position (i, j):

1. If the current characters match (`dna1[i-1] == dna2[j-1]`):
   ```
   dp[i][j] = dp[i-1][j-1]
   ```

2. If the current characters differ, take the minimum of three operations:
   ```
   dp[i][j] = min(
       dp[i-1][j-1] + 1,  # Replace
       dp[i-1][j] + 1,    # Delete
       dp[i][j-1] + 1     # Insert
   )
   ```

### 3. Initialization

- First row (i=0): `dp[0][j] = j` (transforming an empty string to a string of length j requires j insertions)
- First column (j=0): `dp[i][0] = i` (transforming a string of length i to an empty string requires i deletions)

## Implementation

```python
def solution(dna1, dna2):
    m, n = len(dna1), len(dna2)
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    # Fill the DP table
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

## Complexity Analysis

- Time Complexity: O(mn), where m and n are the lengths of the two DNA sequences
- Space Complexity: O(mn), a 2D array of (m+1) rows and (n+1) columns is needed to store intermediate states

## Summary

Using the input `dna1 = "AGT"`, `dna2 = "AGCT"` as an example:

1. Initial state:
```
   ''  A  G  C  T
'' 0  1  2  3  4
A  1
G  2
T  3
```

2. Final DP table:
```
   ''  A  G  C  T
'' 0  1  2  3  4
A  1  0  1  2  3
G  2  1  0  1  2
T  3  2  1  1  1
```

The answer is `dp[3][4] = 1`, meaning one operation is needed (insert "C" between "AG" and "T").

Key considerations:
1. Handle empty string cases
2. Correctly initialize the first row and column of the DP table
3. Mind the index offset in implementation (DP table size is one larger than string lengths)
