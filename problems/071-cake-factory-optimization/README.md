# Cake Factory Optimization

## Problem Description

A cake factory has a certain number of machines and workers. Each day, the factory produces `m * w` cakes, where `m` is the number of machines and `w` is the number of workers. The factory can use accumulated cakes to purchase additional machines or workers, each costing `p` cakes. The goal is to determine the minimum number of days required to produce at least `n` cakes in total.

### Requirements

- Given `m` machines, `w` workers, cost `p` per new machine/worker, and target `n` cakes
- Each day, production equals `m * w` cakes
- Cakes can be spent to buy new machines or workers (each costs `p` cakes)
- Purchases happen at the end of a day and take effect the next day
- Find the minimum number of days to reach at least `n` total cakes

### Constraints

- To maximize production efficiency, new machines and workers should be allocated to keep `m` and `w` as close as possible (since `m * w` is maximized when they are balanced)

## Examples

```
Input: m = 3, w = 1, p = 2, n = 12
Output: 3

Input: m = 10, w = 5, p = 30, n = 500
Output: 8

Input: m = 3, w = 5, p = 30, n = 320
Output: 14
```

## Solution Approach

This is a greedy simulation problem. Each day we decide whether to spend cakes on new resources or continue accumulating:

1. **Check completion**: If current accumulated cakes plus today's production meets the target, return the current day count + 1.
2. **Insufficient funds**: If total cakes (accumulated + today's production) cannot afford any resource, just produce and continue.
3. **Purchase resources**: If affordable, buy as many resources as possible and distribute them to keep `m` and `w` balanced (assign to whichever is smaller), since the product `m * w` is maximized when the two values are as close as possible.

## Implementation

```python
def solution(m, w, p, n):
    days = 0
    total_cakes = 0
    
    while total_cakes < n:
        if total_cakes + m * w >= n:
            return days + 1
        
        current_production = m * w
        
        if total_cakes + current_production < p:
            total_cakes += current_production
            days += 1
            continue
        
        resources_to_buy = (total_cakes + current_production) // p
        total_cakes = (total_cakes + current_production) % p
        
        while resources_to_buy > 0:
            if m < w:
                m += 1
            else:
                w += 1
            resources_to_buy -= 1
        
        days += 1
    
    return days
```

## Complexity Analysis

- **Time Complexity**: O(days * resources_per_day) - depends on input values; each day we may allocate multiple resources
- **Space Complexity**: O(1) - only constant extra space is used

## Summary

This problem uses a greedy simulation approach. The key insight is that to maximize daily production `m * w`, resources should be allocated to keep the number of machines and workers as balanced as possible. Each day, the algorithm decides whether to invest in new resources or simply accumulate cakes toward the target.
