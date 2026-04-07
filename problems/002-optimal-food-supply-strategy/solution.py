def solution(n, k, data):
    # dp[i][j] represents the minimum cost at the start of day i with j food portions on hand
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Initial state

    # Iterate through each day
    for i in range(n):
        # Iterate through current food quantities
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue

            # Not enough food for today's consumption
            if j == 0:
                # Must buy at least 1 portion of food
                for buy in range(1, k + 1):
                    dp[i + 1][buy - 1] = min(
                        dp[i + 1][buy - 1],
                        dp[i][j] + buy * data[i]
                    )
            else:
                # Enough food available, can choose not to buy
                dp[i + 1][j - 1] = min(
                    dp[i + 1][j - 1],
                    dp[i][j]
                )
                # Can also choose to buy more
                for buy in range(1, k - j + 1):
                    dp[i + 1][j + buy - 1] = min(
                        dp[i + 1][j + buy - 1],
                        dp[i][j] + buy * data[i]
                    )

    return dp[n][0]


if __name__ == "__main__":
    # Test cases
    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)  # True
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]) == 9)  # True
    print(solution(4, 1, [3, 2, 4, 1]) == 10)  # True
