# Plate Stacking

## Problem Description

Player M has a special way of organizing plates. After each meal, he organizes plates according to the following rules:

1. All plates have unique integer serial numbers
2. Plates are sorted in ascending order before stacking
3. Stacking rules:
   - Each stack must contain plates with consecutive serial numbers
   - Each stack must contain at least 3 plates
   - Plates that do not form a consecutive group of 3 or more are listed individually

Write a program to output the plate stacking arrangement in a specific format:
- 3 or more consecutive serial numbers are represented as `"start-end"`
- Individual serial numbers are listed directly
- All numbers or ranges are separated by commas

### Requirements

- `plates`: `list[int]` - an integer array representing plate serial numbers
- `n`: `int` - the total number of plates

### Constraints

- Return a string representing the plate stacking arrangement

## Examples

**Example 1:**
```python
Input: plates = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], n = 10
Output: "-3--1,2,10,15,16,18-20"
Explanation:
- [-3,-2,-1] are 3 consecutive numbers, represented as "-3--1"
- [2] is a single number, represented as "2"
- [10] is a single number, represented as "10"
- [15,16] are 2 consecutive numbers, fewer than 3, so listed as "15,16"
- [18,19,20] are 3 consecutive numbers, represented as "18-20"
```

**Example 2:**
```python
Input: plates = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], n = 20
Output: "-6,-3-1,3-5,7-11,14,15,17-20"
```

**Example 3:**
```python
Input: plates = [1, 2, 7, 8, 9, 10, 11, 19], n = 8
Output: "1,2,7-11,19"
```

## Solution Approach

### 1. Core Idea
Use a two-pointer technique to track consecutive sequences, along with a counter to record the length of each consecutive sequence.

### 2. Detailed Steps

1. **Initialization**
   - Create an empty result list `result` to store the final string fragments
   - Set `start` and `end` pointers to the first number
   - Set the `count` counter to 1

2. **Traverse the Array**
   - Start from the second number
   - Check if the current number is consecutive with the previous one (difference of 1)

3. **Process Consecutive Sequences**
   - If consecutive:
     - Update the `end` pointer
     - Increment the `count` counter
   - If not consecutive:
     - Process the previous sequence
     - Reset the pointers and counter

4. **Sequence Processing Rules**
   - If sequence length >= 3:
     - Use the `"start-end"` format
   - If sequence length < 3:
     - Add each number individually

5. **Final Processing**
   - Process the last sequence
   - Join all results with commas

## Implementation

```python
def solution(plates: list[int], n: int) -> str:
    if not plates:
        return ""
    
    result = []
    start = end = plates[0]
    count = 1
    
    for i in range(1, len(plates)):
        if plates[i] == plates[i-1] + 1:
            end = plates[i]
            count += 1
        else:
            if count >= 3:
                result.append(f"{start}-{end}")
            else:
                for j in range(start, end + 1):
                    result.append(str(j))
            start = end = plates[i]
            count = 1
    
    if count >= 3:
        result.append(f"{start}-{end}")
    else:
        for j in range(start, end + 1):
            result.append(str(j))
            
    return ",".join(result)
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the number of plates. A single pass through the array is required.
- **Space Complexity**: O(n). In the worst case (no consecutive sequences), all numbers must be stored.

## Summary

This problem primarily tests:
1. Array traversal and processing
2. Application of the two-pointer technique
3. String formatting and concatenation
4. Handling of edge cases (empty input, negative number sequences like `"-3--1"`)
