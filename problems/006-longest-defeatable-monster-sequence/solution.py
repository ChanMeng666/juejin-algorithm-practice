def solution(n: int, H: int, A: int, h: list, a: list) -> int:
    # Create an array to store the length of the longest defeatable sequence ending at each monster
    dp = [0] * n

    # Iterate through each monster
    for i in range(n):
        # If the current monster can be defeated
        if H > h[i] and A > a[i]:
            # Initialize to 1, meaning at least the current monster can be defeated
            dp[i] = 1
            # Check previous monsters
            for j in range(i):
                # If the previous monster was also defeated and satisfies the sequence requirement
                if dp[j] > 0 and h[i] > h[j] and a[i] > a[j]:
                    # Update the longest sequence length
                    dp[i] = max(dp[i], dp[j] + 1)

    # Return the longest sequence length
    return max(dp) if any(dp) else 0

if __name__ == '__main__':
    print(solution(3, 4, 5, [1, 2, 3], [3, 2, 1]) == 1)
    print(solution(5, 10, 10, [6, 9, 12, 4, 7], [8, 9, 10, 2, 5]) == 2)
    print(solution(4, 20, 25, [10, 15, 18, 22], [12, 18, 20, 26]) == 3)
