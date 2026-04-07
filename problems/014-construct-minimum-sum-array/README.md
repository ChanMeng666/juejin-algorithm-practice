# Construct Minimum Sum Array

## Problem Description
Little C wants to construct an array of n elements that satisfies the following conditions:
1. All elements in the array are pairwise distinct
2. The greatest common divisor (GCD) of all elements is k
3. The sum of the array elements should be as small as possible

Output the minimum possible sum of the array elements that satisfies the conditions.

## Examples
### Example 1
Input:
```python
n = 3, k = 1
```
Output:
```python
6
```
Explanation: The array [1,2,3] can be constructed, with a sum of 6

### Example 2
Input:
```python
n = 2, k = 2
```
Output:
```python
6
```
Explanation: The array [2,4] can be constructed, with a sum of 6

### Example 3
Input:
```python
n = 4, k = 3
```
Output:
```python
30
```
Explanation: The array [3,6,9,12] can be constructed, with a sum of 30

## Solution Approach
1. Understanding the requirements:
   - We need to find n distinct numbers
   - The GCD of these numbers must be k
   - The sum of these numbers should be as small as possible

2. Key observation:
   - For the GCD to be k, all numbers must be multiples of k
   - To minimize the sum, we should choose the smallest multiples of k
   - Simply select consecutive multiples of k starting from k

3. Algorithm steps:
   - Initialize an empty array result
   - Starting from k, add one multiple of k at a time
   - Continue until the array length reaches n
   - Return the sum of the array elements

## Implementation
```python
def solution(n: int, k: int) -> int:
    # Create an array to store the selected numbers
    result = []
    # Starting from k, find n multiples of k
    current = k
    while len(result) < n:
        result.append(current)
        current += k

    # Return the sum of array elements
    return sum(result)
```

## Code Explanation
1. `result = []`: Create an empty array to store the selected numbers

2. `current = k`: Start from k, since k is the smallest possible value

3. `while len(result) < n:`: Loop until n numbers are found
   - `result.append(current)`: Add the current number to the array
   - `current += k`: Move to the next multiple of k

4. `return sum(result)`: Return the sum of all elements in the array

## Complexity Analysis
- Time Complexity: O(n), as we need to find n numbers
- Space Complexity: O(n), as we need to store an array of n numbers

## Walkthrough Example
Taking n=4, k=3 as an example:
1. Initial current=3, result=[3]
2. current=6, result=[3,6]
3. current=9, result=[3,6,9]
4. current=12, result=[3,6,9,12]
5. Return 3+6+9+12=30

## Summary
1. Do not try to find non-multiples of k, as that cannot guarantee the GCD is k
2. Do not skip multiples of k, as that would result in a non-minimal sum
3. Do not forget the condition that array elements must be pairwise distinct

Related problems:
- GCD-related problems
- Constructive algorithm problems
- Array minimum sum problems
