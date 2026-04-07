def solution(n):
    # Create a cache to store subproblem results
    dp = {}

    def dfs(left, right):
        # If the range contains only one number, it is guessed correctly; winning probability is 1
        if left == right:
            return 1

        # If this range has already been computed, return the cached result
        if (left, right) in dp:
            return dp[(left, right)]

        total = right - left + 1
        prob = 0

        # Iterate through all numbers the current player can guess
        for guess in range(left, right + 1):
            curr_prob = 1.0 / total  # Probability that the current number is the answer

            # If guessed correctly, the current player wins
            # If the guess is too low, recursively compute the winning probability for the remaining right half
            # If the guess is too high, recursively compute the winning probability for the remaining left half
            if guess > left:
                curr_prob += (guess - left) / total * (1 - dfs(left, guess - 1))
            if guess < right:
                curr_prob += (right - guess) / total * (1 - dfs(guess + 1, right))

            # Take the maximum probability (optimal strategy)
            prob = max(prob, curr_prob)

        dp[(left, right)] = prob
        return prob

    # Compute the winning probability for the range 1 to n
    result = dfs(1, n)
    # Convert to string and retain 5 decimal places
    return '{:.5f}'.format(result)

if __name__ == "__main__":
    # Test cases
    print(solution(2) == "0.50000")
    print(solution(931) == "0.50054")
    print(solution(924) == "0.50000")
    print(solution(545) == "0.50092")
