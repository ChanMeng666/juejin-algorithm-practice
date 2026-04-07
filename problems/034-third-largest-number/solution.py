def solution(n: int, nums: list) -> int:
    # Convert the list to a set for deduplication, then back to a sorted list
    unique_nums = sorted(list(set(nums)), reverse=True)

    # If there are fewer than 3 distinct numbers, return the maximum value
    if len(unique_nums) < 3:
        return unique_nums[0]

    # Otherwise, return the third largest number
    return unique_nums[2]

if __name__ == '__main__':
    print(solution(3, [3, 2, 1]) == 1)
    print(solution(2, [1, 2]) == 2)
    print(solution(4, [2, 2, 3, 1]) == 1)
