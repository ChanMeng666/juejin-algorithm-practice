# Digit Sum Game

## Problem Description

Given an array of `n` integers and two target values `A` and `B`, partition the array elements into two groups such that the digit sum (sum modulo 10) of each group matches the target values. Count the number of valid partitions.

### Requirements

- Partition the array into two groups
- The digit sum of each group is computed as `sum(group) % 10`
- If both groups are non-empty, group1's digit sum must equal `A` and group2's digit sum must equal `B`
- If one group is empty, the non-empty group's digit sum must equal either `A` or `B`
- Count all valid partition schemes

### Constraints

- All possible partitions are enumerated using bitmask enumeration
- Each element must belong to exactly one of the two groups

## Examples

**Example 1:**
```
Input: n = 3, A = 1, B = 2, array_a = [1, 1, 1]
Output: 3
```

**Example 2:**
```
Input: n = 3, A = 3, B = 5, array_a = [1, 1, 1]
Output: 1
```

**Example 3:**
```
Input: n = 2, A = 1, B = 1, array_a = [1, 1]
Output: 2
```

## Solution Approach

This problem uses **bitmask enumeration** to try all possible ways of partitioning the array into two groups:

1. **Bitmask enumeration**: Iterate through all integers from `0` to `2^n - 1`. Each integer's binary representation determines which group each element belongs to.
2. **Group assignment**: For each bitmask, if the j-th bit is set, the j-th element goes to group1; otherwise, it goes to group2.
3. **Digit sum calculation**: Compute the digit sum of each group as `sum(group) % 10`. An empty group returns `-1`.
4. **Validation**: Check whether the digit sums match the target values `A` and `B` according to the rules.

## Implementation

```python
def solution(n, A, B, array_a):
    def get_digit_sum(nums):
        if not nums:
            return -1
        return sum(nums) % 10
    
    count = 0
    # Use bitwise operations to enumerate all possible groupings
    for i in range(1 << n):
        group1 = []
        group2 = []
        # Assign numbers to two groups based on binary bits
        for j in range(n):
            if i & (1 << j):
                group1.append(array_a[j])
            else:
                group2.append(array_a[j])
        
        sum1 = get_digit_sum(group1)
        sum2 = get_digit_sum(group2)
        
        # Case 1: Both groups are non-empty
        if group1 and group2:
            if sum1 == A and sum2 == B:
                count += 1
        # Case 2: One group is empty
        elif not group1 and group2:
            if sum2 == A or sum2 == B:
                count += 1
        elif not group2 and group1:
            if sum1 == A or sum1 == B:
                count += 1
                
    return count
```

## Complexity Analysis

- **Time complexity**: O(n * 2^n) — iterate through all 2^n partitions, and for each partition iterate through n elements
- **Space complexity**: O(n) — for storing the two groups

## Summary

This problem is a classic bitmask enumeration problem. By representing each partition as a binary number, we can systematically explore all possible groupings and check whether each one satisfies the digit sum constraints.
