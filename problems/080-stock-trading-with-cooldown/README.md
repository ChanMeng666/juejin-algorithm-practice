# Stock Trading with Cooldown

## Problem Description

Player R has recently performed well and the company has decided to reward him with stocks, allowing him to trade on the market to maximize profit. Given an array where the i-th element represents the stock price on day i, design an algorithm to achieve maximum profit.

### Requirements

1. Multiple buy and sell transactions are allowed, but you must sell the stock before buying again
2. After each sale, there is a one-day cooldown period during which no stock can be purchased

### Constraints

- Input: `stocks` - a list of integers representing stock prices on consecutive days
- Output: the maximum profit achievable

## Examples

```python
Example 1:
Input: stocks = [1, 2]
Output: 1
Explanation: Buy on day 1, sell on day 2, profit = 1

Example 2:
Input: stocks = [2, 1]
Output: 0
Explanation: Stock price drops, no transaction is made

Example 3:
Input: stocks = [1, 2, 3, 0, 2]
Output: 3
Explanation:
- Buy on day 1, price = 1
- Sell on day 3, price = 3, profit = 2
- Day 4 is the cooldown period
- Buy on day 5, price = 2
- (Implied sell later), total profit = 3
```

## Solution Approach

### 1. Problem Analysis
This is a classic dynamic programming problem. On each day, the stock status can be one of three states:
1. Holding a stock
2. Not holding a stock, in cooldown (just sold)
3. Not holding a stock, not in cooldown

### 2. State Definition
Use three arrays to record the maximum profit up to day i:
- `hold[i]`: maximum profit on day i while holding a stock
- `sold[i]`: maximum profit on day i after selling a stock (entering cooldown)
- `rest[i]`: maximum profit on day i while not holding a stock and not in cooldown

### 3. State Transition Equations
For each day i:
1. `hold[i] = max(hold[i-1], rest[i-1] - prices[i])`
   - Either held stock from the previous day
   - Or was not holding and not in cooldown yesterday, bought today

2. `sold[i] = hold[i-1] + prices[i]`
   - Can only come from holding stock yesterday and selling today

3. `rest[i] = max(rest[i-1], sold[i-1])`
   - Either was also not holding and not in cooldown yesterday
   - Or was in cooldown yesterday (just sold)

### 4. Initial State
- `hold[0] = -prices[0]`: buy stock on the first day
- `sold[0] = 0`: cannot sell on the first day
- `rest[0] = 0`: not holding stock on the first day

### 5. Final Result
The maximum profit on the last day must be in a state of not holding stock:
`max(sold[n-1], rest[n-1])`

## Implementation

```python
def solution(stocks):
    if not stocks or len(stocks) < 2:
        return 0
        
    # Define three state arrays
    hold = [-float('inf')] * len(stocks)
    sold = [0] * len(stocks)
    rest = [0] * len(stocks)
    
    # Set initial state
    hold[0] = -stocks[0]
    
    # State transition
    for i in range(1, len(stocks)):
        hold[i] = max(hold[i-1], rest[i-1] - stocks[i])
        sold[i] = hold[i-1] + stocks[i]
        rest[i] = max(rest[i-1], sold[i-1])
    
    return max(sold[-1], rest[-1])
```

## Complexity Analysis
- Time Complexity: O(n), where n is the length of the stock price array
- Space Complexity: O(n), three arrays of length n are used to store states

## Summary
Since each day's state only depends on the previous day's state, the space complexity can be optimized to O(1) by using just three variables to record the previous day's state. However, the array form is retained here for clarity.
