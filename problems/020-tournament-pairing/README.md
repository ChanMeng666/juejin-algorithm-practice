# Tournament Pairing

## Problem Description

Little R is organizing a tournament with n teams participating. The tournament follows these unique rules:

1. If the current number of teams is **even**:
   - Every team is paired with another team
   - A total of n/2 matches are played
   - n/2 teams advance to the next round

2. If the current number of teams is **odd**:
   - One team randomly gets a bye and advances
   - The remaining teams are paired
   - A total of (n-1)/2 matches are played
   - (n-1)/2 + 1 teams advance to the next round

### Requirements

Calculate the total number of pairings (matches) played throughout the entire tournament until a single winning team is determined.

## Examples

### Example 1:
```
Input: n = 7
Output: 6
Explanation:
Round 1: 7 teams, 1 gets a bye, 3 matches, 4 advance
Round 2: 4 teams, 2 matches, 2 advance
Round 3: 2 teams, 1 match, 1 advances
Total matches: 3 + 2 + 1 = 6
```

### Example 2:
```
Input: n = 14
Output: 13
Explanation:
Round 1: 14 teams, 7 matches, 7 advance
Round 2: 7 teams, 1 gets a bye, 3 matches, 4 advance
Round 3: 4 teams, 2 matches, 2 advance
Round 4: 2 teams, 1 match, 1 advances
Total matches: 7 + 3 + 2 + 1 = 13
```

### Example 3:
```
Input: n = 1
Output: 0
Explanation: Only 1 team, no matches needed
```

## Solution Approach

This is a simulation problem where we need to simulate the entire tournament process until only one team remains. The key points are:

1. Understanding the number of advancing teams after each round:
   - Even number of teams: n/2 advance
   - Odd number of teams: (n-1)/2 + 1 advance (including the 1 team with a bye)

2. Use a loop to simulate the tournament process, accumulating the number of matches in each round

3. Special case handling: when there is only 1 team, no matches are needed

## Implementation

```python
def solution(n: int) -> int:
    # If there is only 1 team, return 0 directly
    if n == 1:
        return 0

    total_matches = 0
    remaining_teams = n

    # Continue the tournament while more than 1 team remains
    while remaining_teams > 1:
        if remaining_teams % 2 == 0:
            # Even number of teams: play n/2 matches
            matches = remaining_teams // 2
            remaining_teams = matches
        else:
            # Odd number of teams: one team gets a bye, remaining teams play (n-1)/2 matches
            matches = (remaining_teams - 1) // 2
            remaining_teams = matches + 1

        total_matches += matches

    return total_matches
```

## Code Explanation

1. **Special Case Handling**:
   ```python
   if n == 1:
       return 0
   ```
   If only 1 team is participating, no matches are needed.

2. **Variable Initialization**:
   ```python
   total_matches = 0      # Track the total number of matches
   remaining_teams = n    # Track the number of teams in the current round
   ```

3. **Main Loop**:
   ```python
   while remaining_teams > 1:
   ```
   Continue playing matches as long as there is more than 1 team remaining.

4. **Even Number of Teams**:
   ```python
   if remaining_teams % 2 == 0:
       matches = remaining_teams // 2
       remaining_teams = matches
   ```
   - The number of matches in the current round is half the number of teams
   - The number of advancing teams equals the number of matches

5. **Odd Number of Teams**:
   ```python
   else:
       matches = (remaining_teams - 1) // 2
       remaining_teams = matches + 1
   ```
   - One team gets a bye, the rest are paired for matches
   - The number of advancing teams equals the number of matches plus the 1 team with a bye

6. **Accumulate Match Count**:
   ```python
   total_matches += matches
   ```
   Add the number of matches from each round to the total.

## Complexity Analysis

- Time Complexity: O(log n), since the number of teams is approximately halved after each round
- Space Complexity: O(1), only constant extra space is used

## Summary

This problem mainly tests the understanding and simulation of tournament elimination formats. The key points are:
1. Correctly calculating the number of advancing teams after each round
2. Distinguishing between the handling of odd and even numbers of teams
3. Using a loop to simulate the entire tournament process

Through this problem, we learn how to translate a real-world problem into code and how to handle different conditional branches.
