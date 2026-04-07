# Texas Hold'em Full House Problem

## Problem Description

In a Texas Hold'em poker game, a "Full House" is a special hand consisting of three cards of the same face value (a) and two cards of the same face value (b). This problem adds an additional constraint to the traditional full house: the sum of the face values of the five cards cannot exceed a given maximum value, max.

### Requirements
- 1(A) > K(13) > Q(12) > J(11) > 10 > 9 > ... > 2
- A has a face value of 1, K is 13, and so on

### Constraints
When comparing two full houses:
1. First compare the three-of-a-kind (a) value
2. If the three-of-a-kind values are equal, compare the pair (b) value

## Examples
```python
Input: n = 9, max = 34, array = [6, 6, 6, 8, 8, 8, 5, 5, 1]
Output: [8, 5]
Explanation: Possible full houses:
- [6,6,6,8,8] 
- [6,6,6,5,5]
- [8,8,8,6,6]
- [8,8,8,5,5]
Among these, [8,8,8,6,6] has a sum of 36 > 34, so it is invalid.
Among the remaining valid combinations, [8,8,8,5,5] is the largest.

Input: n = 9, max = 37, array = [9, 9, 9, 9, 6, 6, 6, 6, 13]
Output: [6, 9]
Explanation: [9,9,9,6,6] has a sum of 39 > 37, so it is invalid.
Therefore, return the next largest combination [6,6,6,9,9].
```

## Solution Approach

1. Count the occurrences of each number
   - Use a dictionary to record the frequency of each face value
   
2. Find all possible three-of-a-kind and pair combinations
   - Cards appearing 3 or more times can form a three-of-a-kind
   - Cards appearing 2 or more times can form a pair

3. Special handling for A(1) being the highest card
   - Treat 1 as 14 during sorting
   - Use the tuple (0 if x != 1 else 14, x) as the sorting key
   
4. Sort possible combinations by value in descending order
   - Sort three-of-a-kind combinations in descending order
   - Sort pair combinations in descending order

5. Iterate through all possible combinations
   - Skip cases where the three-of-a-kind and pair use the same face value
   - Check if the sum of five cards exceeds max
   - The first valid combination found is the largest

## Implementation

```python
def solution(n, max, array):
    # Count the occurrences of each number
    count_dict = {}
    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Find all possible three-of-a-kind combinations
    triples = []
    for num, count in count_dict.items():
        if count >= 3:
            triples.append(num)
    
    # Find all possible pair combinations
    pairs = []
    for num, count in count_dict.items():
        if count >= 2:
            pairs.append(num)
    
    # If there are not enough cards to form a full house, return [0, 0]
    if not triples or not pairs:
        return [0, 0]
    
    # Sort triples and pairs by card value (considering 1/Ace as the highest)
    triples.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)
    pairs.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)
    
    # Find the largest valid full house combination
    for triple in triples:
        for pair in pairs:
            # Skip if using the same number for both
            if triple == pair:
                continue
            # Calculate the total card value sum
            total = triple * 3 + pair * 2
            # Check if it exceeds the maximum value
            if total > max:
                continue
            # If a valid combination is found, return immediately (since we sorted by value)
            return [triple, pair]
    
    return [0, 0]
```

## Complexity Analysis

- Time complexity: O(n + k^2)
  - n is the length of the input array
  - k is the number of distinct face values
  - Counting frequencies takes O(n)
  - Sorting takes O(k log k)
  - Iterating through combinations takes O(k^2)

- Space complexity: O(k)
  - k is the number of distinct face values
  - Storage is needed for the frequency dictionary and possible combination lists

## Common Pitfalls

1. Not considering the special case where A(1) is the highest card
2. Forgetting to check if the sum of five cards exceeds max
3. Using the same face value for both the three-of-a-kind and the pair
4. Not comparing different full house combinations in the correct order

## Related Topics

- Texas Hold'em hand type evaluation
- Card game problems
- Combinatorial counting problems
