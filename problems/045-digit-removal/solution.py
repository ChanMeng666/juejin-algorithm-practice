def solution(n: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # Copy the input array to avoid modifying the original
    nums = a.copy()
    steps = 0

    # Continue while there are non-zero numbers
    while any(nums):
        # Find the current largest number
        max_num = max(nums)
        # Find the position of this number in the array
        max_idx = nums.index(max_num)

        # Remove the leading digit of the largest number
        str_num = str(max_num)
        if len(str_num) > 1:
            nums[max_idx] = int(str_num[1:])
        else:
            nums[max_idx] = 0

        steps += 1

    return steps

if __name__ == '__main__':
    print(solution(5, [10, 13, 22, 100, 30]) == 7)
    print(solution(3, [5, 50, 505]) == 4)
    print(solution(4, [1000, 1, 10, 100]) == 4)
