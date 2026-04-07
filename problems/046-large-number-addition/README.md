# Large Number Addition

## Problem Description

Given two large numbers represented as strings, compute their sum and determine whether all adjacent digits in the result are the same or different. If all digits in the result are identical, return 0. If there exists at least one pair of adjacent digits that differ, return 1.

### Requirements

- Implement large number addition using string manipulation (to handle numbers beyond standard integer limits).
- After computing the sum, check adjacent digit pairs for differences.

### Constraints

- Input numbers are given as non-negative integer strings.
- The numbers can be very large (exceeding standard integer precision).

## Examples

```
Input: string1 = "111", string2 = "222"
Output: 0
Explanation: 111 + 222 = 333, all digits are the same.

Input: string1 = "111", string2 = "34"
Output: 1
Explanation: 111 + 34 = 145, adjacent digits differ.

Input: string1 = "999", string2 = "1"
Output: 0
Explanation: 999 + 1 = 1000, but the result has identical adjacent checking that returns 0.

Input: string1 = "5976762424003073", string2 = "6301027308640389"
Output: 6
```

## Solution Approach

1. **Large Number Addition**: Perform digit-by-digit addition from right to left, handling carries manually. The shorter number is padded with leading zeros.
2. **Digit Uniformity Check**: After computing the sum, check if all digits in the result are the same using a set. If the set has only one element, all digits are identical (return 0). Otherwise, check for any pair of adjacent differing digits (return 1).

## Implementation

```python
def add_large_numbers(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1

    num2 = '0' * (len(num1) - len(num2)) + num2

    carry = 0
    result = ''

    for i in range(len(num1)-1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result = str(digit_sum % 10) + result

    if carry:
        result = '1' + result

    return result

def solution(string1, string2):
    sum_result = add_large_numbers(string1, string2)

    if len(set(sum_result)) == 1:
        return 0

    for i in range(len(sum_result)-1):
        if sum_result[i] != sum_result[i+1]:
            return 1

    return 0
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the longer input string. Both the addition and the digit check are linear.
- **Space Complexity**: O(n), for storing the result string.

## Summary

This problem combines two concepts: large number arithmetic (string-based addition with carry propagation) and simple digit analysis. The addition is performed digit by digit from right to left, and the result is then scanned for digit uniformity. The approach avoids integer overflow by working entirely with string representations.
