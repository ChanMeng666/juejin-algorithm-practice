# Find the Number Appearing More Than Half the Time in an Array

## Problem Description
Xiao R selected some students from a class, and each student provides a number. It is known that among these numbers, a certain number appears more than half of the total count. Now you need to help Xiao R find this number.

## Examples
### Example 1
Input: `array = [1, 3, 8, 2, 3, 1, 3, 3, 3]`
Output: `3`
Explanation: The number 3 appears 5 times, which is more than half of the array length 9.

### Example 2
Input: `array = [5, 5, 5, 1, 2, 5, 5]`
Output: `5`
Explanation: The number 5 appears 5 times, which is more than half of the array length 7.

### Example 3
Input: `array = [9, 9, 9, 9, 8, 9, 8, 8]`
Output: `9`
Explanation: The number 9 appears 5 times, which is more than half of the array length 8.

## Solution Approach
This problem can be solved using the "Boyer-Moore Voting Algorithm." It is a classic algorithm for finding elements that appear more than half the time in an array.

The core idea of the algorithm is:
1. If a number appears more than half the time, when this number is paired and cancelled with all other numbers, the remaining one must be this number.
2. We maintain a candidate number and a counter:
   - When the counter reaches 0, select the current number as the new candidate
   - When encountering the same number, increment the counter
   - When encountering a different number, decrement the counter

### Algorithm Steps
1. Initialization:
   - Select the first number as the candidate
   - Set the counter to 1

2. First pass:
   - Traverse the remaining elements of the array
   - Update the counter based on whether the current number equals the candidate
   - Change the candidate when the counter reaches 0

3. Second pass:
   - Count the actual number of occurrences of the candidate in the array
   - Verify whether it exceeds half the array length

## Implementation
```python
def solution(array):
    # Use Boyer-Moore Voting Algorithm
    candidate = array[0]  # Candidate number
    count = 1  # Counter
    
    # First pass: find the potential majority element
    for num in array[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Second pass: verify that this number indeed appears more than half the time
    count = sum(1 for num in array if num == candidate)
    if count > len(array) // 2:
        return candidate
    
    return 0  # If no qualifying number exists (though per the problem description this case won't occur)
```

## Complexity Analysis
- Time complexity: O(n), the array needs to be traversed twice
- Space complexity: O(1), only a constant number of variables are used

## Code Explanation
1. `candidate = array[0]`: Select the first number as the initial candidate
2. `count = 1`: Initialize the counter to 1
3. First pass:
   - `if count == 0`: When the counter reaches 0, the previous candidate has been fully cancelled out; select the current number as the new candidate
   - `elif num == candidate`: Same number encountered, increment the counter
   - `else`: Different number encountered, decrement the counter
4. Second pass:
   - Use a generator expression to count the actual occurrences of the candidate
   - Verify whether it exceeds half the array length

## Common Pitfalls
1. Don't forget the second pass to verify the candidate's occurrence count
2. Note that half the array length should use integer division `//`
3. Initialization should start from the first element, and traversal should start from the second element

## Related Topics
- Finding the mode of an array
- Finding elements appearing more than n/3 times in an array

## Summary
The Boyer-Moore Voting Algorithm is a very clever algorithm that uses the concept of "cancellation" to find the element appearing more than half the time in O(n) time. This algorithm is not only efficient but also relatively simple to implement, making it the best choice for solving this type of problem.
