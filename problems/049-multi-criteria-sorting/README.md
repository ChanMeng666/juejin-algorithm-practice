# Multi-Criteria Sorting

## Problem Description

Given a list of people and the amounts of red packets they received, sort the people by the amount in descending order. If two people received the same amount, sort them by their original order (index) in ascending order. Return the sorted list of names.

### Constraints

- `n` is the number of people.
- `s` is a list of `n` strings representing names.
- `x` is a list of `n` integers representing the red packet amounts each person received.
- Names and amounts correspond by index.

## Examples

```
Input: n = 4, s = ["a", "b", "c", "d"], x = [1, 2, 2, 1]
Output: ["b", "c", "a", "d"]
Explanation: "b" and "c" both have amount 2 (highest), but "b" comes first by original order.
             "a" and "d" both have amount 1, but "a" comes first by original order.

Input: n = 3, s = ["x", "y", "z"], x = [100, 200, 200]
Output: ["y", "z", "x"]
Explanation: "y" and "z" both have amount 200, "y" has a smaller index so it comes first.

Input: n = 5, s = ["m", "n", "o", "p", "q"], x = [50, 50, 30, 30, 20]
Output: ["m", "n", "o", "p", "q"]
Explanation: Already sorted by amount descending, ties broken by original order.
```

## Solution Approach

1. **Combine data**: Zip together the index, name, and amount for each person into a list of tuples.
2. **Sort with composite key**: Sort the list using a lambda that sorts by amount in descending order (negated value) as the primary key, and by the original index in ascending order as the secondary key.
3. **Extract names**: Return only the names from the sorted list.

Python's built-in `sorted()` function with a tuple key naturally handles multi-criteria sorting -- it compares by the first element first, then the second on ties.

## Implementation

```python
def solution(n: int, s: list, x: list) -> list:
    # Create a list containing index, name, and amount
    data = list(zip(range(n), s, x))

    # Sort by amount in descending order; if amounts are equal, sort by index in ascending order
    sorted_data = sorted(data, key=lambda x: (-x[2], x[0]))

    # Return the sorted list of names
    result = [name for _, name, _ in sorted_data]

    return result
```

## Complexity Analysis

- **Time Complexity**: O(n log n), where n is the number of people, due to the sorting step.
- **Space Complexity**: O(n), for storing the zipped data and the result list.
