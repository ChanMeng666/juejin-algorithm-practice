# Optimal Refueling Strategy

## Problem Description

Xiao F plans to depart from Qinghai Lake and travel to a distant scenic spot X. He needs to plan an optimal refueling strategy to minimize the total fuel cost. The specific conditions are as follows:

- Vehicle tank capacity: 400L
- Starting fuel: 200L
- Fuel consumption: 1L per km
- The vehicle must be returned with at least 200L of fuel remaining
- Multiple gas stations are available along the route, each with a different fuel price

### Requirements

- Input parameters:
  - `distance`: total distance (km), not exceeding 10,000 km
  - `n`: number of gas stations along the route (1 <= n <= 100)
  - `gas_stations`: list of gas station information, each element is [distance from start, fuel price]
- Output: the minimum cost
- If the destination cannot be reached or the fuel requirement at return cannot be met, return -1

## Solution Approach

### 1. Feasibility Checks

A series of feasibility checks must be performed first:

1. **No gas stations**: If there are no gas stations, check whether the initial fuel is sufficient to reach the destination.
2. **Data format validation**: Ensure each gas station entry contains both distance and price.
3. **Distance reachability checks**:
   - Check if the first gas station is within the initial fuel range (<= 200 km)
   - Check if adjacent gas stations are within tank capacity range (<= 400 km)
   - Check if the distance from the last gas station to the destination is reachable (<= 400 km)

### 2. Dynamic Programming Solution

#### State Definition
- `dp[i][j]`: the minimum cost to reach gas station i with j liters of fuel remaining

#### Initial State
- `dp[0][200] = 0`: starting with 200L of fuel at cost 0
- All other states initialized to infinity

#### State Transition
For each gas station i:
1. Calculate the fuel consumed to reach the current gas station from the previous one
2. For each possible fuel level from the previous state:
   - Compute the remaining fuel upon arrival at the current station
   - Consider refueling different amounts at the current station
   - Update the dp array, keeping the minimum cost

#### Final Result
1. Calculate the fuel needed from the last gas station to the destination
2. Check all possible ending fuel states (>= 200L)
3. Find the minimum cost among feasible states

## Implementation

```python
def solution(distance, n, gas_stations):
    if n == 0 and distance > 200:
        return -1

    for station in gas_stations:
        if len(station) != 2:
            return -1

    gas_stations.sort(key=lambda x: x[0])

    if n > 0 and gas_stations[0][0] > 200:
        return -1

    for i in range(n-1):
        if gas_stations[i+1][0] - gas_stations[i][0] > 400:
            return -1

    if n > 0 and distance - gas_stations[-1][0] > 400:
        return -1
    elif n == 0 and distance > 400:
        return -1

    dp = [[float('inf')] * 401 for _ in range(n + 1)]
    dp[0][200] = 0

    for i in range(n):
        prev_dist = 0 if i == 0 else gas_stations[i-1][0]
        curr_dist = gas_stations[i][0]
        cost = curr_dist - prev_dist

        for prev_fuel in range(cost, 401):
            if dp[i][prev_fuel] == float('inf'):
                continue

            curr_fuel = prev_fuel - cost

            for add_fuel in range(401 - curr_fuel):
                if curr_fuel + add_fuel <= 400:
                    dp[i+1][curr_fuel + add_fuel] = min(
                        dp[i+1][curr_fuel + add_fuel],
                        dp[i][prev_fuel] + add_fuel * gas_stations[i][1]
                    )

    final_cost = float('inf')
    last_dist = 0 if n == 0 else gas_stations[-1][0]
    remain_dist = distance - last_dist

    for fuel in range(remain_dist + 200, 401):
        if dp[n][fuel] != float('inf'):
            final_cost = min(final_cost, dp[n][fuel])

    return final_cost if final_cost != float('inf') else -1
```

## Complexity Analysis

- **Time Complexity**: O(n * F * F)
  - n is the number of gas stations
  - F is the tank capacity (400 in this case)
  - For each station, every previous fuel level and every possible refuel amount must be considered

- **Space Complexity**: O(n * F)
  - A 2D dp array is needed to store the states

## Summary

This problem uses dynamic programming where the state tracks both the current gas station and the remaining fuel level. Feasibility checks (reachability between stations, data validation) are performed upfront. The DP transition considers all possible refueling amounts at each station, and the final answer is extracted by checking all valid end states that satisfy the minimum return fuel requirement of 200L.
