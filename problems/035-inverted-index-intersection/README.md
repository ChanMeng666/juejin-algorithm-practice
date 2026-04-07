# Inverted Index Intersection

## Problem Description

Xiao S is developing a search engine and needs to implement inverted index functionality. An inverted index is a commonly used search engine index structure that works as follows:
- Each keyword corresponds to a list of document IDs containing that keyword
- These IDs are sorted in ascending order
- When a user searches for multiple keywords, all documents containing those keywords need to be found

### Requirements
Given two sorted arrays `a` and `b` (representing the inverted lists of two keywords), find the elements that appear in both arrays (i.e., the intersection) and return the result in descending order.

## Examples
```python
Input: a = [1, 2, 3, 7], b = [2, 5, 7]
Output: [7, 2]
Explanation: The common elements in arrays a and b are 2 and 7, sorted in descending order returns [7, 2]

Input: a = [1, 4, 8, 10], b = [2, 4, 8, 10]
Output: [10, 8, 4]
Explanation: The common elements are 4, 8, and 10, sorted in descending order returns [10, 8, 4]
```

## Solution Approach

This problem can be solved through the following steps:

1. **Use set intersection**
   - Convert both input arrays to sets
   - Use the set intersection operator `&` to find common elements

2. **Sort the result**
   - Convert the intersection result to a list
   - Use `sorted()` to sort the result in descending order

### Why use sets?
- Set intersection is very efficient, with time complexity O(min(len(a), len(b)))
- Sets automatically remove duplicates, although in this problem the input arrays already contain no duplicates
- Set lookup operations have O(1) time complexity

## Implementation

```python
def solution(a, b):
    # Create two sets to store the numbers
    set_a = set(a)
    set_b = set(b)
    
    # Find the intersection of the two sets
    intersection = set_a & set_b
    
    # Convert the intersection to a list and sort in descending order
    result = sorted(list(intersection), reverse=True)
    
    return result
```

## Complexity Analysis

- **Time complexity**: O(n log n)
  - Set conversion and intersection: O(n)
  - Sorting: O(n log n)
  - Overall time complexity is determined by sorting: O(n log n)

- **Space complexity**: O(n)
  - Extra space is needed to store the two sets and the result list
  - n is the number of elements in the input arrays

## Test Case Analysis

```python
# Test case 1
Input: a = [1, 2, 3, 7], b = [2, 5, 7]
Output: [7, 2]
Analysis: 2 and 7 appear in both arrays, sorted in descending order

# Test case 2
Input: a = [1, 4, 8, 10], b = [2, 4, 8, 10]
Output: [10, 8, 4]
Analysis: 4, 8, and 10 are common elements, sorted in descending order

# Test case 3
Input: a = [3, 5, 9], b = [1, 4, 6]
Output: []
Analysis: No common elements, return an empty list

# Test case 4
Input: a = [1, 2, 3], b = [1, 2, 3]
Output: [3, 2, 1]
Analysis: All elements are identical, return them sorted in descending order
```

## Notes

1. The input arrays are already sorted, but we do not need to leverage this property since set operations are independent of element order
2. The result must be in descending order, so `reverse=True` must be set when using `sorted()`
3. If there is no intersection, return an empty list `[]`

## Further Considerations

If the input arrays are very large, we can consider other methods for optimization:
1. Two-pointer approach: leverage the fact that the input arrays are already sorted
2. Binary search: perform binary search in the longer array for each element in the shorter array

These methods may be more efficient than using sets in certain cases, especially when one array is much shorter than the other.
