def solution(n, k, array_a):
    def count_quality_chapters(left, right):
        # Count the number of quality chapters in the given interval
        if right - left < 2:  # No quality chapters when interval length is less than 3
            return 0
        count = 0
        for i in range(left + 1, right):
            if array_a[i] > array_a[i-1] and array_a[i] > array_a[i+1]:
                count += 1
        return count

    best_quality = 0  # Best quality chapter count
    best_left = 0     # Best left boundary
    best_right = 0    # Best right boundary
    min_sum = float('inf')  # Minimum total word count

    # Iterate over all possible intervals
    for left in range(n):
        window_sum = 0
        for right in range(left, n):
            window_sum += array_a[right]
            if window_sum > k:  # If total word count exceeds the limit, break inner loop
                break

            quality_count = count_quality_chapters(left, right)

            # Update the optimal solution
            if quality_count > best_quality:
                best_quality = quality_count
                best_left = left
                best_right = right
                min_sum = window_sum
            elif quality_count == best_quality:
                if window_sum < min_sum:
                    best_left = left
                    best_right = right
                    min_sum = window_sum
                elif window_sum == min_sum and left < best_left:
                    best_left = left
                    best_right = right

    # Return the result string
    return f"{best_quality},{best_left + 1},{best_right + 1}"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(8, 15000, [1000, 3000, 2000, 4000, 3000, 2000, 4000, 2000]) == "2,1,5" )
    print(solution(8, 15000, [2000, 5000, 2000, 1000, 4000, 2000, 4000, 3000]) == "2,4,8" )
