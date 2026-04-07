def solution(m: int, n: int, p: list[list[int]]) -> int:
    """
    Calculate the minimum cost to complete the journey.

    Args:
        m (int): Total number of travel days
        n (int): Number of supply stations
        p (list[list[int]]): Supply station information, each element is [day, price]

    Returns:
        int: Minimum cost
    """
    # Create dp array, dp[i] represents the minimum cost to reach day i
    dp = [float('inf')] * (m + 1)

    # Record supply station positions and prices
    stations = {day: price for day, price in p}

    # Initialize the state for day 0
    dp[0] = 0

    # Dynamic programming process
    for i in range(m):
        # If there is a supply station on the current day
        if i in stations:
            price = stations[i]
            # Buy food from the current station to sustain for each subsequent day
            for j in range(i + 1, m + 1):
                # dp[j] can transition from dp[i], requiring (j-i) units of food
                dp[j] = min(dp[j], dp[i] + (j - i) * price)

    return dp[m]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (5, 4, [[0, 2], [1, 3], [2, 1], [3, 2]], 7),
        (6, 5, [[0, 1], [1, 5], [2, 2], [3, 4], [5, 1]], 6),
        (4, 3, [[0, 3], [2, 2], [3, 1]], 9)
    ]

    for i, (m, n, p, expected) in enumerate(test_cases, 1):
        result = solution(m, n, p)
        print(f"Test case {i}:")
        print(f"Input: m = {m}, n = {n}, p = {p}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'PASSED' if result == expected else 'FAILED'}\n")
