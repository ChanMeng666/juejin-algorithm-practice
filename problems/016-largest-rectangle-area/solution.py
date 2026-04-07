def solution(n, array):
    max_area = 0

    # Iterate through all possible window sizes k
    for k in range(1, n + 1):
        # Iterate through all possible starting positions
        for i in range(n - k + 1):
            # Get the minimum value in the current window
            min_height = min(array[i:i + k])
            # Calculate the rectangle area for the current window
            area = k * min_height
            # Update the maximum area
            max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    # Test cases
    print(solution(5, [1, 2, 3, 4, 5]) == 9)  # True
    print(solution(6, [5, 4, 3, 2, 1, 6]) == 9)  # True
    print(solution(4, [4, 4, 4, 4]) == 16)  # True
