def solution(inputArray):
    if not inputArray:
        return 0

    # Sort by interval start position
    intervals = sorted(inputArray, key=lambda x: x[0])

    # Merge overlapping intervals
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1] + 1:  # If the current interval overlaps with or is adjacent to the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    # Calculate the total count of numbers across all intervals
    total_points = 0
    for start, end in merged:
        total_points += end - start + 1

    return total_points

if __name__ == "__main__":
    #  You can add more test cases here
    testArray1 = [[1,4], [7, 10], [3, 5]]
    testArray2 = [[1,2], [6, 10], [11, 15]]
    testArray3 = [[1,3], [2, 6], [8, 10]]

    print(solution(testArray1) == 9)  # True
    print(solution(testArray2) == 12)  # True
    print(solution(testArray3) == 9)  # True
