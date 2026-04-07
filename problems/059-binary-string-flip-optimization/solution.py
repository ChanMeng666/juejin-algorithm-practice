def solution(n, a, b, c, s):
    # dp[i][j][k] represents the maximum profit when processing up to the i-th character,
    # where j is the parity of the last operation, and k is the current state
    # j: 0 means even, 1 means odd
    # k: 0 means the current position is 0, 1 means the current position is 1
    dp = [[[-float('inf')] * 2 for _ in range(2)] for _ in range(n + 1)]

    # Initial state
    dp[0][0][0] = dp[0][1][0] = 0
    dp[0][0][1] = dp[0][1][1] = 0

    # Iterate over each position
    for i in range(n):
        curr = int(s[i])
        # Iterate over the parity of the last operation
        for last in range(2):
            # Iterate over the state of the current position
            for state in range(2):
                if dp[i][last][state] == -float('inf'):
                    continue

                # If the current has consecutive 00, it can be replaced with 0
                if i < n-1 and curr == 0 and int(s[i+1]) == 0:
                    # Replacing 00 with 0 is an odd operation
                    if last != 1:  # The previous operation cannot be odd
                        dp[i+2][1][0] = max(dp[i+2][1][0], dp[i][last][state] + a)

                # If the current has consecutive 11, it can be replaced with 1
                if i < n-1 and curr == 1 and int(s[i+1]) == 1:
                    # Replacing 11 with 1 is an even operation
                    if last != 0:  # The previous operation cannot be even
                        dp[i+2][0][1] = max(dp[i+2][0][1], dp[i][last][state] + b)

                # Delete the current 0
                if curr == 0:
                    # Deleting 0 is an odd operation
                    if last != 1:  # The previous operation cannot be odd
                        dp[i+1][1][int(s[i+1]) if i+1 < n else 0] = max(
                            dp[i+1][1][int(s[i+1]) if i+1 < n else 0],
                            dp[i][last][state] - c
                        )

                # Keep the current character unchanged
                if i+1 < n:
                    dp[i+1][last][int(s[i+1])] = max(
                        dp[i+1][last][int(s[i+1])],
                        dp[i][last][state]
                    )

    # Return the maximum value at the last position
    result = -float('inf')
    for last in range(2):
        for state in range(2):
            result = max(result, dp[n][last][state])

    return result

if __name__ == "__main__":
    # Test cases
    print(solution(5, 2, 2, 1, "01101") == 3)
    print(solution(6, 4, 3, 5, "110001") == 11)
    print(solution(6, 3, 2, 1, "011110") == 4)
    print(solution(4, 1, 3, 2, "1111") == 3)
    print(solution(3, 2, 2, 1, "000") == 2)
