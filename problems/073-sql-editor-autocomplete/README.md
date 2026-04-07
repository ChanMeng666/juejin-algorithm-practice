# SQL Editor Autocomplete

## Problem Description

When developing an SQL editor, an autocomplete feature needs to be implemented. Given a user's input fragment, the feature should find all candidate words from known SQL keywords and database-related names that start with the given fragment, and output them in lexicographic order.

### Requirements

- `num`: an integer representing the length of the data list
- `data`: a string array containing SQL keywords and database-related names
- `input`: a string representing the user's input prefix

### Constraints

- If matches are found, return all matching strings sorted in lexicographic order, joined by commas
- If no matches are found, return `"-1"`

## Examples

```python
Input:
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "f"
Output: "from,from_mobile"

Input:
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "wh"
Output: "where"

Input:
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "z"
Output: "-1"
```

## Solution Approach

1. **Problem Analysis**
   - This is a string prefix matching problem
   - Special cases need to be handled (no match, single match, multiple matches)
   - Results must be sorted in lexicographic order

2. **Key Points**
   - Use the `startswith()` method for prefix matching
   - Exact matches need special handling
   - Results must be sorted lexicographically
   - Multiple results are joined by commas with no spaces

3. **Implementation Steps**
   1. Create an empty list to store matching results
   2. Traverse the data list to find all strings starting with `input`
   3. Handle exact matches and prefix matches separately
   4. Sort the matching results
   5. Return the final result

## Implementation

```python
def solution(num, data, input):
    # Store all matching results
    matches = []
    
    # Traverse the data list to find all strings starting with input
    for item in data:
        if item.startswith(input) and item != input:  # Exclude exact matches
            matches.append(item)
    
    # Handle exact match separately
    if input in data:
        matches.append(input)
    
    # If no matches found, return "-1"
    if not matches:
        return "-1"
    
    # Sort matches in lexicographic order
    matches.sort()
    
    # Join results with commas into a string
    return ",".join(matches)
```

## Code Explanation

1. **Match Collection**
   - Use the `startswith()` method to check if a string begins with the input prefix
   - Use the condition `item != input` to exclude exact matches, allowing control over the position of exact matches in the result

2. **Exact Match Handling**
   - Separately check if the input string exists in the data list
   - If it exists, add it to the match list

3. **Result Processing**
   - Use the `sort()` method to sort matches in lexicographic order
   - Use the `join()` method to concatenate results with commas
   - If no matches are found, return `"-1"`

## Complexity Analysis

- Time Complexity: O(n * k), where n is the number of items and k is the average string length
- Space Complexity: O(n), for storing the matching results

## Summary

This problem is a practical application scenario in SQL editor development. Implementing this feature improves user input efficiency and experience. Solving this problem requires attention to string handling, sorting, and edge case processing.
