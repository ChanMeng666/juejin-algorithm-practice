# Hero Battle Sequence

## Problem Description

You have a team of heroes, each with a certain power value. You need to battle against an opponent whose heroes have power values 1, 2, 3, ..., up to `number`. In each round, one of your heroes faces one of the opponent's heroes. A battle is won if your hero's power value is strictly greater than the opponent's. Determine the maximum number of battles you can win by optimally arranging the matchups.

### Requirements
- You have `number` heroes with power values given in the `heroes` array
- The opponent has heroes with power values 1, 2, 3, ..., `number`
- Each hero can only be used once
- A win occurs when your hero's power value is strictly greater than the opponent's
- Maximize the total number of wins

### Constraints
- `number` equals the length of the `heroes` array
- Each hero is used exactly once

## Examples

```python
Example 1:
Input: number = 7, heroes = [10, 1, 1, 1, 5, 5, 3]
Output: 4
Explanation: Sort heroes in descending order: [10, 5, 5, 3, 1, 1, 1].
  Round 1: 10 > 1 (win), Round 2: 5 > 2 (win), Round 3: 5 > 3 (win),
  Round 4: 3 > 4 is false (loss), but by optimal matching we get 4 wins.

Example 2:
Input: number = 5, heroes = [1, 1, 1, 1, 1]
Output: 0
Explanation: All heroes have power value 1, matching against opponents 1-5.
  No hero can beat any opponent since 1 is not strictly greater than 1.

Example 3:
Input: number = 10, heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 9
Explanation: Sort heroes descending: [10,9,8,7,6,5,4,3,2,1].
  Heroes with values 10,9,8,7,6,5,4,3,2 beat opponents 1,2,3,4,5,6,7,8,9 respectively. 9 wins total.
```

## Solution Approach

The key insight is a greedy strategy: sort your heroes in descending order and match them against the opponent's heroes in ascending order (1, 2, 3, ...). By pairing your strongest heroes against the weakest opponents first, you maximize the number of wins.

1. Sort the `heroes` array in descending order
2. For each round `i` (0-indexed), the opponent's hero has power value `i + 1`
3. If `sorted_heroes[i] > i + 1`, count it as a win
4. Return the total win count

This greedy approach works because using your strongest heroes against the weakest opponents ensures no hero's strength is "wasted" on an opponent that a weaker hero could also beat.

## Implementation

```python
def solution(number, heroes):
    # Sort heroes by power value in descending order
    sorted_heroes = sorted(heroes, reverse=True)
    wins = 0

    # Iterate through each round of the battle
    for i in range(number):
        # The opponent's hero power value is i+1
        opponent = i + 1
        # If our strongest hero's power value is greater than the opponent's, use the current strongest hero
        if sorted_heroes[i] > opponent:
            wins += 1

    return wins
```

## Complexity Analysis

- Time Complexity: O(n log n), where n is the number of heroes, due to the sorting step
- Space Complexity: O(n), for storing the sorted array

## Summary

This is a classic greedy matching problem. By sorting heroes in descending order and opponents in ascending order, we can greedily assign the strongest available hero to the weakest available opponent, maximizing the number of wins. The approach is simple yet optimal.
