# Find the Unique Number Card in a Class

## Problem Description

In a class, each student receives a card with an integer on it. Interestingly, except for one number, all numbers appear exactly twice. Now you need to help the class monitor Xiao C quickly find the number on the unique card.

### Requirements
- Design an algorithm with a time complexity of O(n), where n is the number of students in the class
- Minimize the use of extra space to demonstrate your algorithm optimization skills

### Constraints
- 1 ≤ cards.length ≤ 1001
- 0 ≤ cards[i] ≤ 1000
- The number of students is odd
- Except for one number card that appears only once, every other number card appears exactly twice

## Examples
```python
Example 1:
Input: cards = [1, 1, 2, 2, 3, 3, 4, 5, 5]
Output: 4
Explanation: The student with number 4 is the only one without a pair.

Example 2:
Input: cards = [0, 1, 0, 1, 2]
Output: 2
Explanation: Number 2 appears only once, making it the unique card.

Example 3:
Input: cards = [7, 3, 3, 7, 10]
Output: 10
Explanation: 10 is the only non-duplicate number card in the class.
```

## Solution Approach

This problem can be solved using the XOR operation. XOR has the following important properties:

1. Any number XORed with itself equals 0: `a ^ a = 0`
2. Any number XORed with 0 equals itself: `a ^ 0 = a`
3. XOR is commutative and associative:
   - `a ^ b = b ^ a`
   - `(a ^ b) ^ c = a ^ (b ^ c)`

Using these properties, we can:
1. XOR all numbers sequentially
2. Identical numbers cancel each other out (become 0)
3. The remaining value is the number that appears only once

## Implementation

```python
def solution(cards):
    # Use XOR operation to find the unique number
    result = 0
    for num in cards:
        result ^= num
    return result


if __name__ == "__main__":
    # Test cases
    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)  # True
    print(solution([0, 1, 0, 1, 2]) == 2)  # True
    print(solution([7, 3, 3, 7, 10]) == 10)  # True
```

## Code Explanation

Let's walk through Example 1 in detail:
```python
cards = [1, 1, 2, 2, 3, 3, 4, 5, 5]
```

1. Initialize `result = 0`
2. Perform XOR operations sequentially:
   - `0 ^ 1 = 1`
   - `1 ^ 1 = 0` (the first 1 is cancelled out)
   - `0 ^ 2 = 2`
   - `2 ^ 2 = 0` (2 is cancelled out)
   - `0 ^ 3 = 3`
   - `3 ^ 3 = 0` (3 is cancelled out)
   - `0 ^ 4 = 4`
   - `4 ^ 5 = 4 ^ 5`
   - `(4 ^ 5) ^ 5 = 4` (5 is cancelled out)

The final result is 4, which is the number that appears only once.

## Complexity Analysis

- Time complexity: O(n), where n is the length of the array. We only need to traverse the array once.
- Space complexity: O(1), only one variable is used to store the result.

## Summary

This problem demonstrates the clever application of bitwise operations in algorithms:
1. Using XOR, we can find the number that appears only once without using extra space
2. The code is concise, elegant, and highly efficient
3. This approach is especially advantageous when handling large-scale data

This solution is superior to the traditional approach of using a hash table to count frequencies, because it requires no additional storage space, perfectly meeting the problem's space optimization requirement.

