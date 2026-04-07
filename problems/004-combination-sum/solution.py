def solution(numbers):
    # Convert each number to a string and separate into individual digit sets
    digit_groups = []
    for num in numbers:
        # Convert each number to a string, then to a set for deduplication
        digit_groups.append(set(str(num)))

    def get_digit_sum(combination):
        # Calculate the sum of digits in the combination
        return sum(int(d) for d in combination)

    def backtrack(current_combination, group_index):
        # When all groups have been processed, check if the sum is even
        if group_index == len(digit_groups):
            return 1 if get_digit_sum(current_combination) % 2 == 0 else 0

        count = 0
        # Select a digit from the current group
        for digit in digit_groups[group_index]:
            count += backtrack(current_combination + digit, group_index + 1)
        return count

    # Start backtracking from an empty combination
    return backtrack("", 0)

if __name__ == "__main__":
    # Test cases
    print(solution([123, 456, 789]) == 14)  # True
    print(solution([123456789]) == 4)       # True
    print(solution([14329, 7568]) == 10)    # True
