# Journey Water Supply

## Problem Description

You are embarking on a journey of distance `d` with an initial water supply of `w`. Along the route, there are supply stations at various positions, each offering a certain amount of water. When you stop at a supply station, your water is replaced with that station's supply amount. Determine the minimum number of stops needed to reach the destination, or return -1 if it is impossible.

### Requirements
- `d`: total distance of the journey
- `w`: initial water supply (each unit of water allows traveling 1 unit of distance)
- `position`: array of supply station positions along the route
- `supply`: array of water amounts available at each supply station
- When stopping at a station, your current water is replaced by that station's supply amount
- Find the minimum number of refill stops to reach the destination
- Return -1 if the destination cannot be reached

### Constraints
- Supply stations are located between the starting point and the destination
- Each station can be used at most once
- You must have enough water to reach a station before stopping there
- Stations are not necessarily given in sorted order

## Examples

```python
Example 1:
Input: d = 10, w = 4, position = [1, 4, 7], supply = [6, 3, 5]
Output: 1
Explanation: With initial water of 4, we can reach any station up to position 4.
  Stop at position 1 (supply = 6), then we can travel 6 more units,
  reaching the destination at position 10. Only 1 stop needed.

Example 2:
Input: d = 2000, w = 200, position = [170, 192, ...], supply = [443, 185, ...]
Output: 5
Explanation: With 20 supply stations along a 2000-unit journey, the optimal strategy
  requires 5 stops to reach the destination.
```

## Solution Approach

This problem uses a greedy strategy. At each step, among all reachable supply stations, choose the one with the maximum supply to maximize the distance that can be traveled after each stop.

### Algorithm Steps

1. **Edge Cases**:
   - If initial water `w >= d`, no stops are needed; return 0
   - If there are no supply stations and water is insufficient, return -1

2. **Sort Stations**: Sort all supply stations by their position

3. **Greedy Selection**:
   - Calculate the maximum reachable position from the current location
   - If the destination is reachable, return the current refill count
   - Among all stations within the reachable range (that have not been passed), select the one with the maximum supply
   - Move to the selected station, update water supply, and increment the refill count
   - If no reachable station exists, return -1

4. **Repeat** until the destination is reached or determined to be unreachable

## Implementation

```python
def solution(d, w, position, supply):
    # If the initial water is enough to reach the destination, return 0 directly
    if w >= d:
        return 0

    # If there are no supply stations and the initial water is insufficient, return -1
    if not position:
        return -1

    # Sort supply stations by position
    stations = list(zip(position, supply))
    stations.sort()

    # Current water and position
    current_water = w
    current_pos = 0
    refill_count = 0

    while current_pos < d:
        max_reach = current_pos + current_water

        # If the current water can reach the destination directly
        if max_reach >= d:
            return refill_count

        # Find the station with the maximum supply within the reachable range
        best_station_index = -1
        max_supply = -1

        for i, (station_pos, station_supply) in enumerate(stations):
            # Skip stations already passed
            if station_pos <= current_pos:
                continue
            # If the station is beyond the reachable range
            if station_pos > max_reach:
                break
            # Select the station with the maximum supply
            if station_supply > max_supply:
                max_supply = station_supply
                best_station_index = i

        # If no reachable supply station is found
        if best_station_index == -1:
            return -1

        # Move to the selected supply station
        station_pos, station_supply = stations[best_station_index]
        # Update remaining water (subtract the amount consumed en route)
        current_water -= (station_pos - current_pos)
        # Refill water at the supply station
        current_water = station_supply
        current_pos = station_pos
        refill_count += 1

        # Remove visited stations
        stations = stations[best_station_index + 1:]

    return refill_count
```

## Complexity Analysis

- Time Complexity: O(n log n + n^2), where n is the number of supply stations. O(n log n) for sorting, and in the worst case O(n^2) for scanning remaining stations at each stop.
- Space Complexity: O(n), for storing the sorted station list.

## Summary

This is a greedy algorithm problem similar to the classic gas station refueling problem. The key insight is that at each step, selecting the reachable station with the maximum supply minimizes the total number of stops. The greedy choice of maximum supply within reach ensures that each stop maximizes the potential distance for subsequent travel.
