# Quality Chapter Selection

## Problem Description

In a novel on Tomato Novel, editor S needs to select a contiguous range of chapters for a special feature display. Each chapter has a corresponding word count. The goal is to select a contiguous interval containing the maximum number of quality chapters while staying within the total word count limit.

### Requirements

- `n`: the total number of chapters
- `k`: the maximum allowed total word count
- `array_a`: an array representing the word count of each chapter

### Constraints

- Return a string in the format: `"quality_count,start_position,end_position"`
- A **quality chapter** is defined as a chapter (excluding the first and last in the selected range) whose word count is greater than both its adjacent chapters
- If multiple solutions have the same maximum quality chapter count, choose the one with the smallest total word count
- If total word counts are also equal, choose the one with the smallest starting position
- Chapter positions are 1-based

## Examples

### Example 1
Input:
- n = 8
- k = 15000
- array_a = [1000, 3000, 2000, 4000, 3000, 2000, 4000, 2000]

Output: `"2,1,5"`

Explanation:
- Select interval [1,5], i.e., chapters 1 through 5
- Chapter 2 (3000) and chapter 4 (4000) are quality chapters
- Total word count is 13000, within the limit of 15000

### Example 2
Input:
- n = 8
- k = 15000
- array_a = [2000, 5000, 2000, 1000, 4000, 2000, 4000, 3000]

Output: `"2,4,8"`

Explanation:
- Select interval [4,8]
- Chapter 5 and chapter 7 are quality chapters
- Total word count is 14000, within the limit of 15000

## Solution Approach

### 1. Basic Analysis
This is a sliding window type problem, but all possible interval combinations need to be considered:
1. Iterate over all possible intervals
2. Count quality chapters in each interval
3. Find the optimal solution within the word count limit

### 2. Implementation Steps

#### 2.1 Helper Function
Define a function to count quality chapters in a given interval:
```python
def count_quality_chapters(left, right):
    if right - left < 2:  # No quality chapters when interval length < 3
        return 0
    count = 0
    for i in range(left + 1, right):
        if array_a[i] > array_a[i-1] and array_a[i] > array_a[i+1]:
            count += 1
    return count
```

#### 2.2 Main Steps
1. Initialize variables:
   - `best_quality`: best quality chapter count
   - `best_left`: best left boundary
   - `best_right`: best right boundary
   - `min_sum`: minimum total word count

2. Use a nested loop to iterate over all possible intervals:
   - Outer loop determines the left boundary
   - Inner loop determines the right boundary
   - Accumulate the total word count in the interval
   - Break the inner loop when total word count exceeds limit k

3. For each valid interval:
   - Count quality chapters
   - Update the optimal solution based on quality count, total word count, and interval position

4. Return the formatted result string

## Implementation

```python
def solution(n, k, array_a):
    def count_quality_chapters(left, right):
        if right - left < 2:
            return 0
        count = 0
        for i in range(left + 1, right):
            if array_a[i] > array_a[i-1] and array_a[i] > array_a[i+1]:
                count += 1
        return count
    
    best_quality = 0
    best_left = 0
    best_right = 0
    min_sum = float('inf')
    
    for left in range(n):
        window_sum = 0
        for right in range(left, n):
            window_sum += array_a[right]
            if window_sum > k:
                break
            quality_count = count_quality_chapters(left, right)
            if quality_count > best_quality:
                best_quality = quality_count
                best_left = left
                best_right = right
                min_sum = window_sum
            elif quality_count == best_quality:
                if window_sum < min_sum:
                    best_left = left
                    best_right = right
                    min_sum = window_sum
                elif window_sum == min_sum and left < best_left:
                    best_left = left
                    best_right = right
    
    return f"{best_quality},{best_left + 1},{best_right + 1}"
```

## Complexity Analysis

- Time Complexity: O(n^3)
  - Outer loop: O(n)
  - Inner loop: O(n)
  - Counting quality chapters: O(n)

- Space Complexity: O(1)
  - Only constant extra space is used

## Summary

This problem tests the following key points:
1. Application of sliding window techniques
2. Interval processing skills
3. Handling multi-criteria optimization problems
4. Edge case handling (quality chapter definition, 1-based indexing, tie-breaking rules)
