def solution(redpacks):
    n = len(redpacks)
    # If there are fewer than 3 red packets, they cannot be split into three parts
    if n < 3:
        return 0

    max_amount = 0
    # Compute prefix sums for fast range sum calculations
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + redpacks[i]

    # Enumerate all possible cut positions
    for i in range(n-2):  # Position of the first cut
        first_sum = prefix_sum[i+1]  # Sum of the first part

        for j in range(i+1, n-1):  # Position of the second cut
            third_sum = prefix_sum[n] - prefix_sum[j+1]  # Sum of the third part

            # If the first and third parts are equal, consider the combination
            if first_sum == third_sum:
                # If a larger sum is found, update max_amount
                if first_sum > max_amount:
                    max_amount = first_sum

            # Check if merging adjacent red packets can yield a larger sum
            if i > 0 and first_sum + redpacks[i+1] == third_sum - redpacks[j+1]:
                max_amount = max(max_amount, first_sum + redpacks[i+1])

    return max_amount

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 3, 4, 6, 7, 14]) == 14)
    print(solution([10000]) == 0)
    print(solution([52, 13, 61, 64, 42, 26, 4, 27, 25]) == 52)
    print(solution([2, 5, 50, 30, 60, 52, 26, 5, 74, 83, 34, 96, 6, 88, 94, 80, 64, 22, 97, 47, 46, 25, 24, 43, 76, 24, 2, 42, 51, 96, 97, 87, 47, 93, 11, 98, 41, 54, 18, 16, 11, 96, 34, 36, 87, 24, 32, 27, 62, 72, 54, 14, 67, 5, 21, 20, 44, 55, 3, 82, 19, 45, 1, 52, 14, 44, 46, 39, 83, 27, 30, 87, 61, 56, 59, 10, 83, 80, 42, 44, 75, 39, 43, 41, 23, 93, 73, 50, 94, 94, 82, 46, 87, 60, 94, 47, 52, 67, 22, 50, 49, 8, 9, 30, 62, 87, 13, 11]) == 2627)
