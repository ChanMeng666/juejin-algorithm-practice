# Red Packet Three-Way Split

## Problem Description

Given an array of red packet values, split the array into three contiguous parts such that the sum of the first part equals the sum of the third part. Among all valid splits, find the maximum possible value of this equal sum. If the array cannot be split into three parts (fewer than 3 elements), return 0.

### Constraints

- The array contains at least 1 element.
- If the array has fewer than 3 elements, return 0.
- The three parts must be contiguous segments of the original array.
- The middle part can have any sum; only the first and third parts need equal sums.

## Examples

```
Input: [1, 3, 4, 6, 7, 14]
Output: 14
Explanation: Split as [1, 3, 4, 6] | [...] | [14], where first part sums to 14 and third part sums to 14.

Input: [10000]
Output: 0
Explanation: Cannot split a single element into three parts.

Input: [52, 13, 61, 64, 42, 26, 4, 27, 25]
Output: 52
Explanation: A valid split exists where the first and third parts each sum to 52.
```

## Solution Approach

1. **Prefix Sum**: Compute a prefix sum array to allow O(1) range sum queries.
2. **Two-pointer enumeration**: Iterate over all possible positions for the first cut (index `i`) and the second cut (index `j`). For each pair:
   - The first part is `redpacks[0..i]` with sum `prefix_sum[i+1]`.
   - The third part is `redpacks[j+1..n-1]` with sum `prefix_sum[n] - prefix_sum[j+1]`.
   - If the first and third part sums are equal, update the maximum.
3. **Track maximum**: Keep the largest equal sum found across all valid splits.

## Implementation

```python
def solution(redpacks):
    n = len(redpacks)
    if n < 3:
        return 0

    max_amount = 0
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + redpacks[i]

    for i in range(n - 2):
        first_sum = prefix_sum[i + 1]

        for j in range(i + 1, n - 1):
            third_sum = prefix_sum[n] - prefix_sum[j + 1]

            if first_sum == third_sum:
                if first_sum > max_amount:
                    max_amount = first_sum

            if i > 0 and first_sum + redpacks[i + 1] == third_sum - redpacks[j + 1]:
                max_amount = max(max_amount, first_sum + redpacks[i + 1])

    return max_amount
```

## Complexity Analysis

- **Time Complexity**: O(n^2), where n is the length of the red packets array, due to the nested loop over all pairs of cut positions.
- **Space Complexity**: O(n), for the prefix sum array.

## Summary

This problem uses prefix sums combined with a two-pointer enumeration strategy to find the optimal three-way split. The key insight is that by fixing two cut positions and comparing the sums of the first and third segments, we can efficiently find the maximum equal sum.
