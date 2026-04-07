# Array Transformation

## Problem Description

Little M has an array. She can perform multiple operations, where each operation selects two elements $a_i$ and $a_j$, chooses a factor $x$ of $a_i$, then transforms $a_i$ to $a_i/x$ and $a_j$ to $a_j \times x$. Her goal is to make each element in the array contain at most one type of prime factor through a finite number of operations.

The definition of a prime factor is: if $x$ is divisible by a prime number $p$, then $p$ is a prime factor of $x$. For example, the prime factors of 12 are 2 and 3.

Your task is to determine whether it is possible to make each element in the array contain at most one type of prime factor through a finite number of operations. If possible, output "Yes"; otherwise, output "No".

## Solution Approach

This problem may seem complex at first glance, but upon careful analysis, we can discover some important properties:

1. Each operation essentially transfers factors between two elements without changing their product.
2. Therefore, the product of all elements in the array remains constant throughout the operations.
3. Our goal is to have each element contain at most one type of prime factor, meaning we need to distribute different prime factors to different elements.

Based on the above observations, we can draw an important conclusion: the solvability of the problem depends on whether the number of distinct prime factors of the product of all elements does not exceed the length of the array.

### Requirements

1. Calculate the product of all elements in the array.
2. Find all prime factors of this product.
3. Count the number of distinct prime factors.
4. If the number of distinct prime factors does not exceed the array length, the problem is solvable; otherwise, it is not.

This approach works because:
- If the number of distinct prime factors does not exceed the array length, we can always distribute each prime factor to a separate element through operations.
- If the number of distinct prime factors exceeds the array length, no matter what operations we perform, at least one element will contain more than one type of prime factor.

## Implementation

Here is the Python implementation:

```python
def solution(n: int, a: list) -> str:
    def prime_factors(num):
        factors = []
        d = 2
        while num > 1:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
            if d * d > num:
                if num > 1:
                    factors.append(num)
                break
        return factors

    # Calculate the product of all elements
    product = 1
    for num in a:
        product *= num

    # Find all prime factors of the product
    all_factors = prime_factors(product)

    # Count the number of distinct prime factors
    unique_factors = set(all_factors)

    # Check if the number of distinct prime factors does not exceed the array length
    if len(unique_factors) <= n:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4]) == "Yes")
    print(solution(2, [10, 12]) == "No")
    print(solution(3, [6, 9, 15]) == "Yes")
```

### Code Explanation

1. `prime_factors` function:
   - This helper function finds all prime factors of a number.
   - It uses trial division, starting from 2, testing each divisor. If divisible, it records the factor and continues dividing until it is no longer divisible.
   - Then it increments the divisor and continues until the square of the divisor exceeds the remaining number.
   - If the remaining number is greater than 1, it is itself a prime factor.

2. Main function `solution`:
   - First calculates the product of all elements in the array.
   - Then uses the `prime_factors` function to find all prime factors of this product.
   - Uses `set` to count the number of distinct prime factors, which removes duplicates.
   - Finally compares the number of distinct prime factors with the array length; returns "Yes" if it does not exceed, otherwise returns "No".

## Complexity Analysis

- Time Complexity: O(n + sqrt(m)), where n is the array length and m is the product of the array elements. Computing the product takes O(n) time, while finding prime factors takes approximately O(sqrt(m)) time.
- Space Complexity: O(log m), for storing prime factors. In the worst case, the number of prime factors of a number is approximately at the logarithmic level.

## Examples

1. Input: `n = 4, a = [1, 2, 3, 4]`
   Output: `'Yes'`
   Explanation: The product is 24, prime factors are 2 and 3, count is 2, which does not exceed the array length 4.

2. Input: `n = 2, a = [10, 12]`
   Output: `'No'`
   Explanation: The product is 120, prime factors are 2, 3, and 5, count is 3, which exceeds the array length 2.

3. Input: `n = 3, a = [6, 9, 15]`
   Output: `'Yes'`
   Explanation: The product is 810, prime factors are 2, 3, and 5, count is 3, which does not exceed the array length 3.

## Summary

This problem appears complex at first, but by analyzing the invariance of the product of array elements, we can transform the problem into simple prime factor counting. This transformation approach is very common and important in algorithm problems. Through this problem, we not only learn how to decompose prime factors but also understand how to convert complex operation sequence problems into static mathematical problems. This way of thinking is very helpful for solving more complex algorithm problems.
