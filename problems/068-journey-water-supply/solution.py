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

if __name__ == "__main__":
    #  You can add more test cases here
    testPosition = [170, 192, 196, 234, 261, 269, 291, 404, 1055, 1121, 1150, 1234, 1268, 1402, 1725, 1726, 1727, 1762, 1901, 1970]
    testSupply = [443, 185, 363, 392, 409, 358, 297, 70, 189, 106, 380, 130, 126, 411, 63, 186, 36, 347, 339, 50]

    print(solution(10, 4, [1,4,7], [6,3,5]) == 1 )
    print(solution(2000, 200, testPosition, testSupply) == 5 )
