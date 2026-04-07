# Number Guessing Probability

## Problem Description

In a number game, one number from 1 to n is the lucky number, chosen uniformly at random. Two players, Xiao I and Xiao W, take turns guessing the lucky number, with Xiao I always going first.

### Requirements
- After each round, the host announces whether the guess was too high, too low, or correct
- If a player guesses correctly, that player wins the game
- Both players use optimal strategies

Calculate the probability that Xiao I (the first player) wins, and output the result rounded to five decimal places.

### Constraints
- 1 <= n
- The lucky number is chosen uniformly at random from 1 to n
- Both players play optimally

## Examples

```python
Input: n = 2
Output: '0.50000'

Input: n = 3
Output: '0.66667'

Input: n = 4
Output: '0.50000'

Input: n = 5
Output: '0.60000'
```

## Solution Approach

This is a classic game theory problem that can be solved using dynamic programming (memoized search).

### 1. Core Idea

1. For any interval [left, right], we need to compute the optimal winning probability for the first player in that interval
2. Each player will choose the strategy that maximizes their own winning probability on their turn
3. When a player guesses a number, there are three possibilities:
   - Correct guess: immediate win
   - Guess too high: continue the game in the left subinterval
   - Guess too low: continue the game in the right subinterval

### 2. State Definition

- Use `dp[(left, right)]` to represent the optimal winning probability for the first player in interval [left, right]
- Use memoized search to avoid recomputing identical states

### 3. State Transition

For the current interval [left, right]:
1. If left == right, only one number remains, so it is guessed correctly with probability 1
2. Otherwise, iterate through each possible guess and compute the winning probability for that choice:
   - Probability of a correct guess: 1 / total
   - Probability the guess is too low: (right - guess) / total * (1 - opponent's winning probability in the right subinterval)
   - Probability the guess is too high: (guess - left) / total * (1 - opponent's winning probability in the left subinterval)
3. Take the maximum probability among all choices as the optimal strategy

## Implementation

```python
def solution(n):
    dp = {}  # Memoization storage

    def dfs(left, right):
        if left == right:  # Base case
            return 1

        if (left, right) in dp:  # Avoid recomputation
            return dp[(left, right)]

        total = right - left + 1
        prob = 0

        # Iterate through all possible guesses
        for guess in range(left, right + 1):
            curr_prob = 1.0 / total  # Probability of a correct guess

            # Handle the case when the guess is too high
            if guess > left:
                curr_prob += (guess - left) / total * (1 - dfs(left, guess - 1))
            # Handle the case when the guess is too low
            if guess < right:
                curr_prob += (right - guess) / total * (1 - dfs(guess + 1, right))

            prob = max(prob, curr_prob)  # Take the optimal strategy

        dp[(left, right)] = prob
        return prob

    return '{:.5f}'.format(dfs(1, n))  # Format the output
```

## Complexity Analysis

- Time Complexity: O(n^3), where n is the number range. For each interval [left, right], all possible guesses need to be iterated.
- Space Complexity: O(n^2), mainly for storing the dynamic programming states.

## Summary

This problem is an excellent example of combining game theory with dynamic programming. The keys to solving it are:
1. Correctly defining the dynamic programming state
2. Accurately computing the probability for each choice
3. Using memoized search to optimize performance
4. Understanding the implication of both players using optimal strategies

Through this problem, we learn how to handle probability-related dynamic programming problems and how to consider both players' optimal strategies in a game setting.
