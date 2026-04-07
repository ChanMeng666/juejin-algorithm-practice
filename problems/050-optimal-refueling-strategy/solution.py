def solution(distance, n, gas_stations):
    # If there are no gas stations and the distance exceeds the drivable range with current fuel, return -1
    if n == 0 and distance > 200:
        return -1

    # Validate gas station data format
    for station in gas_stations:
        if len(station) != 2:
            return -1

    # Sort gas stations by distance
    gas_stations.sort(key=lambda x: x[0])

    # Verify the first gas station is reachable
    if n > 0 and gas_stations[0][0] > 200:
        return -1

    # Verify adjacent gas stations are within reachable distance of each other
    for i in range(n-1):
        if gas_stations[i+1][0] - gas_stations[i][0] > 400:
            return -1

    # Verify the distance from the last gas station to the destination is reachable
    if n > 0 and distance - gas_stations[-1][0] > 400:
        return -1
    elif n == 0 and distance > 400:
        return -1

    # Initialize dp array: dp[i][j] represents the minimum cost to reach gas station i with j liters of fuel remaining
    dp = [[float('inf')] * 401 for _ in range(n + 1)]

    # Initial state: starting point has 200L of fuel
    dp[0][200] = 0

    # For each gas station
    for i in range(n):
        # Calculate the fuel consumed to reach the current gas station
        prev_dist = 0 if i == 0 else gas_stations[i-1][0]
        curr_dist = gas_stations[i][0]
        cost = curr_dist - prev_dist

        # For each possible fuel level from the previous state
        for prev_fuel in range(cost, 401):
            if dp[i][prev_fuel] == float('inf'):
                continue

            # Remaining fuel after reaching the current gas station
            curr_fuel = prev_fuel - cost

            # Choose to refuel or not
            for add_fuel in range(401 - curr_fuel):
                if curr_fuel + add_fuel <= 400:
                    dp[i+1][curr_fuel + add_fuel] = min(
                        dp[i+1][curr_fuel + add_fuel],
                        dp[i][prev_fuel] + add_fuel * gas_stations[i][1]
                    )

    # Calculate from the last gas station to the destination
    final_cost = float('inf')
    last_dist = 0 if n == 0 else gas_stations[-1][0]
    remain_dist = distance - last_dist

    # Check each possible fuel state upon reaching the destination
    for fuel in range(remain_dist + 200, 401):
        if dp[n][fuel] != float('inf'):
            final_cost = min(final_cost, dp[n][fuel])

    return final_cost if final_cost != float('inf') else -1


if __name__ == "__main__":
    #  You can add more test cases here
    gas_stations1 = [(100, 1), (200, 30), (400, 40), (300, 20)]
    gas_stations2 = [(100, 999), (150, 888), (200, 777),
                     (300, 999), (400, 1009), (450, 1019), (500, 1399)]
    gas_stations3 = [(101,), (100, 100), (102, 1)]
    gas_stations4 = [(34, 1), (105, 9), (9, 10), (134, 66), (215, 90), (999, 1999), (49, 0), (10, 1999), (200, 2),
                     (300, 500), (12, 34), (1, 23), (46, 20), (80, 12), (1, 1999), (90, 33), (101, 23), (34, 88), (103, 0), (1, 1)]

    print(solution(500, 4, gas_stations1) == 4300)
    print(solution(500, 7, gas_stations2) == 410700)
    print(solution(500, 3, gas_stations3) == -1)
    print(solution(100, 20, gas_stations4) == 0)
    print(solution(100, 0, []) == -1)
