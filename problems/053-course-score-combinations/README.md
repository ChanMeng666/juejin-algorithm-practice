# Course Score Combinations

## Problem Description

Calculate the number of score combinations that allow a student to pass all courses.

### Requirements

- A student takes `n` elective courses plus 3 required courses (total `n + 3` courses).
- Each course has 20 questions, each worth 5 points, so each course score ranges from 0 to 100 in increments of 5.
- A student passes if the average score across all courses is at least 60 (i.e., total score >= 60 * total_courses).
- Return the number of valid score combinations modulo `202220222022`.

### Constraints

- `n` can be large (up to at least 888).

## Examples

```
Input: n = 3
Output: "19195617"

Input: n = 6
Output: "135464411082"

Input: n = 49
Output: "174899025576"

Input: n = 201
Output: "34269227409"

Input: n = 888
Output: "194187156114"
```

## Solution Approach

1. **Score Enumeration**: Each course can have scores 0, 5, 10, ..., 100 (21 possible values).

2. **Dynamic Programming**:
   - Define `dp[i][j]` as the number of ways to achieve a total score of `j` across `i` courses.
   - Base case: `dp[0][0] = 1`.
   - Transition: For each course, enumerate all possible scores and accumulate the combinations.

3. **Result Aggregation**: Sum up `dp[total_courses][j]` for all `j >= 60 * total_courses` to get the count of passing combinations.

4. **Modular Arithmetic**: All calculations are done modulo `202220222022`.

## Implementation

```python
def solution(n):
    MOD = 202220222022

    def get_scores():
        scores = []
        for i in range(21):  # 0 to 20 correct answers
            scores.append(i * 5)
        return scores

    def get_min_total(total_courses):
        return 60 * total_courses

    def dp_solve(n):
        scores = get_scores()
        total_courses = n + 3
        min_total = get_min_total(total_courses)

        dp = [[0] * (100 * total_courses + 1) for _ in range(total_courses + 1)]
        dp[0][0] = 1

        for i in range(total_courses):
            for j in range(i * 100 + 1):
                if dp[i][j] == 0:
                    continue
                for score in scores:
                    dp[i + 1][j + score] = (dp[i + 1][j + score] + dp[i][j]) % MOD

        result = 0
        for j in range(min_total, 100 * total_courses + 1):
            result = (result + dp[total_courses][j]) % MOD

        return str(result)

    return dp_solve(n)
```

## Complexity Analysis

- **Time Complexity**: O(total_courses^2 * 100 * 21), where total_courses = n + 3. For each course, we iterate over all possible cumulative scores and all 21 per-course score options.
- **Space Complexity**: O(total_courses * 100 * total_courses) for the DP table.

## Summary

This is a classic dynamic programming problem involving counting combinations. The key insight is modeling each course's score as a bounded knapsack item and using a 2D DP table to track the number of ways to reach each total score. Modular arithmetic prevents overflow for large inputs.
