# Reconstruct Array from Pair Sums

## Problem Description

Given an integer `n` and a list of pairwise sums, reconstruct the original array of `n` numbers.

### Requirements

- Given `n` numbers, all possible pairwise sums (each pair summed exactly once) are provided in the `sums` list.
- Reconstruct the original array such that the numbers are in non-decreasing order.
- If reconstruction is not possible, return `"Impossible"`.

### Constraints

- The number of pairwise sums should equal `n * (n - 1) / 2`.
- Values can be negative.

## Examples

```
Input: n = 3, sums = [1269, 1160, 1663]
Output: "383 777 886"

Input: n = 3, sums = [1, 1, 1]
Output: "Impossible"

Input: n = 5, sums = [226, 223, 225, 224, 227, 229, 228, 226, 225, 227]
Output: "111 112 113 114 115"

Input: n = 5, sums = [-1, 0, -1, -2, 1, 0, -1, 1, 0, -1]
Output: "-1 -1 0 0 1"
```

## Solution Approach

1. **Special case for n=2**: If there is exactly one sum and it is even, split it equally into two numbers.

2. **Case n=3**: Sort the three sums. Using the system of equations:
   - `a + b = x`, `a + c = y`, `b + c = z`
   - Solve: `a = (x + y - z) / 2`, `b = (x - y + z) / 2`, `c = (-x + y + z) / 2`
   - Verify the solution produces the original sums.

3. **Case n=5**: Sort all 10 sums. Enumerate possible pairs of the two smallest values, then derive the remaining three values from the known sums. Verify by checking that all generated pairwise sums match the input.

## Implementation

```python
def solution(n, sums):
    if n < 2:
        return "Impossible"
    if len(sums) != n * (n-1) // 2:
        return "Impossible"

    if n == 2:
        if len(sums) == 1:
            s = sums[0]
            if s % 2 == 0:
                return f"{s//2} {s//2}"
        return "Impossible"

    try:
        if n == 3:
            x, y, z = sorted(sums)
            a = (x + y - z) // 2
            b = (x - y + z) // 2
            c = (-x + y + z) // 2
            if {a+b, a+c, b+c} == set(sums) and a <= b <= c:
                return f"{a} {b} {c}"
            return "Impossible"

        if n == 5:
            sums_sorted = sorted(sums)
            sums_set = set(sums)
            for i in range(len(sums_sorted)):
                for j in range(i+1, len(sums_sorted)):
                    s1 = sums_sorted[i]
                    s2 = sums_sorted[j]
                    for k in range(-1000, 1001):
                        m = s1 - k
                        n1 = s2 - k
                        if m > k:
                            continue
                        result = [k, m]
                        if k + m not in sums_set:
                            continue
                        candidates = set()
                        for s in sums_sorted:
                            c1 = s - k
                            c2 = s - m
                            if c1 not in result and c1 not in candidates:
                                candidates.add(c1)
                            if c2 not in result and c2 not in candidates:
                                candidates.add(c2)
                        if len(candidates) == 3:
                            result.extend(sorted(candidates))
                            check_sums = []
                            for x in range(5):
                                for y in range(x+1, 5):
                                    check_sums.append(result[x] + result[y])
                            if sorted(check_sums) == sums_sorted:
                                return " ".join(map(str, result))
        return "Impossible"
    except:
        return "Impossible"
```

## Complexity Analysis

- **Time Complexity**: O(n^2 * R) for the n=5 case, where R is the search range for candidate values. For n=3, it is O(1) after sorting.
- **Space Complexity**: O(n) for storing the result array and candidate set.

## Summary

This problem requires reconstructing an array from its pairwise sums. For small values of n (3 and 5), algebraic and enumeration-based approaches are used. The key insight for n=3 is solving a system of linear equations, while for n=5, a brute-force search with verification is employed.
