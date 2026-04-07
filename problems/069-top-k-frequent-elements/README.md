# Top K Frequent Elements

## Problem Description

Given an integer array `nums` and an integer `k`, return the k most frequent elements. The result should be sorted in ascending order and returned as a string.

The algorithm's time complexity must be better than O(n log n), where n is the size of the array.

### Requirements

- Input:
  - nums: a positive integer array
  - k: an integer
- Output:
  - A string containing k numbers sorted in ascending order, separated by commas

### Constraints

- 1 <= nums[i] <= 10^4
- 1 <= nums.length <= 10^5
- k is in the range [1, number of distinct elements in the array]
- The answer is guaranteed to be unique

## Examples

**Example 1:**
```python
Input: nums = [1,1,1,2,2,3], k = 2
Output: "1,2"
Explanation: Element 1 appears 3 times, element 2 appears 2 times, element 3 appears 1 time, so the top two frequent elements are 1 and 2.
```

**Example 2:**
```python
Input: nums = [1], k = 1
Output: "1"
```

**Example 3:**
```python
Input: nums = [4,4,4,2,2,2,3,3,1], k = 2
Output: "2,4"
```

## Solution Approach

This problem requires finding the k most frequent elements in an array, with a time complexity better than O(n log n). We can use the bucket sort approach to solve it.

### Steps

1. **Frequency Counting**
   - Use a hash map (dictionary) to count the frequency of each number
   - Time Complexity: O(n)

2. **Bucket Sort**
   - Create a bucket array where the index represents frequency
   - Place numbers with the same frequency into the corresponding bucket
   - Time Complexity: O(n)

3. **Collect Results**
   - Traverse the bucket array from back to front (from high frequency to low frequency)
   - Sort the numbers in each non-empty bucket
   - Collect the top k frequent elements
   - Time Complexity: O(n)

4. **Format Output**
   - Sort the final result
   - Convert the result to the required string format
   - Time Complexity: O(k log k), where k is small

## Implementation

```python
def solution(nums, k):
    # Use a hash map to count the frequency of each number
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Create buckets where the index represents frequency, and the value is a list of numbers with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Traverse buckets from back to front to collect the top k frequent elements
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i]:
            # Sort numbers with the same frequency
            buckets[i].sort()
            result.extend(buckets[i])
            if len(result) >= k:
                result = result[:k]
                break

    # Sort the result and convert to a string
    result.sort()
    return ','.join(map(str, result))
```

## Complexity Analysis

- **Time Complexity**: O(n)
  - Frequency counting: O(n)
  - Creating buckets and inserting elements: O(n)
  - Collecting results: O(n)
  - Final sorting: O(k log k), where k is small
  - Overall time complexity is O(n), meeting the problem's requirement

- **Space Complexity**: O(n)
  - Hash map storage: O(n)
  - Bucket array storage: O(n)

## Summary

1. When handling elements with the same frequency, sorting them ensures result uniqueness
2. A final sort before returning is needed to satisfy the ascending order output requirement
3. The returned result must be converted to the specific string format, separated by commas

The key to this problem is using bucket sort to avoid the O(n log n) time complexity of traditional sorting. By counting frequencies with a hash map and then using bucket sort, we solve the problem in O(n) time. This is a typical example of trading space for time.
