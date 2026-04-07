def solution(dna1, dna2):
    # Use dynamic programming to solve the edit distance
    m, n = len(dna1), len(dna2)
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take the minimum of three operations: replace, delete, insert
                dp[i][j] = min(
                    dp[i-1][j-1] + 1,  # Replace
                    dp[i-1][j] + 1,    # Delete
                    dp[i][j-1] + 1     # Insert
                )

    return dp[m][n]

if __name__ == "__main__":
    # Test cases
    print(solution("AGT", "AGCT") == 1)  # True
    print(solution("", "ACGT") == 4)  # True
    print(solution("GCTAGCAT", "ACGT") == 5)  # True
    print(solution("AACCGGTT", "AACCTTGG") == 4)  # True
    print(solution("ACGT", "TGC") == 3)  # True
    print(solution("A", "T") == 1)  # True
    print(solution("GGGG", "TTTT") == 4)  # True
