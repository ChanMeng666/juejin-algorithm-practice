def solution(num):
    # Convert the number to a string
    s = str(num)
    n = len(s)

    # dp[i] represents the number of translation methods from position i to the end
    dp = [0] * (n + 1)
    dp[n] = 1  # An empty string has exactly one translation method

    # Traverse from right to left
    for i in range(n-1, -1, -1):
        # If the current digit is 0, it cannot be translated alone or combined with the previous digit
        if s[i] == '0':
            dp[i] = dp[i+1]
            continue

        # Translate the current digit alone
        dp[i] = dp[i+1]

        # Combine the current digit with the next digit for translation
        if i < n-1:
            num2 = int(s[i:i+2])
            if 10 <= num2 <= 25:
                dp[i] += dp[i+2]

    return dp[0]

if __name__ == "__main__":
    # Test cases
    print(solution(12258) == 5)    # True
    print(solution(1400112) == 6)  # True
    print(solution(2110101) == 10) # True
    print(solution(25) == 2)       # True
    print(solution(1023) == 4)     # True
