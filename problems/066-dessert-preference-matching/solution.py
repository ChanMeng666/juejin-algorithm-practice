def solution(n, m, s, like):
    # Calculate factorial
    def factorial(x):
        if x == 0: return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    # dp[i][j][k]: number of ways considering the first i desserts, using j magic wands, with sum k
    dp = [[[0] * (s + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1  # Initial state

    # Iterate through each dessert
    for i in range(n):
        # Iterate through the number of magic wands used
        for j in range(m + 1):
            # Iterate through the current sum
            for k in range(s + 1):
                if dp[i][j][k] == 0:
                    continue

                # Do not select the current dessert
                dp[i + 1][j][k] += dp[i][j][k]

                # Select without using a magic wand
                if k + like[i] <= s:
                    dp[i + 1][j][k + like[i]] += dp[i][j][k]

                # Select and use a magic wand
                if j < m:
                    fact = factorial(like[i])
                    if k + fact <= s:
                        dp[i + 1][j + 1][k + fact] += dp[i][j][k]

    # Sum of all possible ways
    result = 0
    for j in range(m + 1):
        result += dp[n][j][s]

    return result
