def solution(n, A, B, array_a):
    def get_digit_sum(nums):
        if not nums:
            return -1
        return sum(nums) % 10

    count = 0
    # Use bitwise operations to enumerate all possible groupings
    for i in range(1 << n):
        group1 = []
        group2 = []
        # Assign numbers to two groups based on binary bits
        for j in range(n):
            if i & (1 << j):
                group1.append(array_a[j])
            else:
                group2.append(array_a[j])

        sum1 = get_digit_sum(group1)
        sum2 = get_digit_sum(group2)

        # Case 1: Both groups are non-empty
        if group1 and group2:
            # To avoid double counting, only count when sum1 == A
            if sum1 == A and sum2 == B:
                count += 1
        # Case 2: One group is empty
        elif not group1 and group2:
            # Check if the sum of group2 equals A or B
            if sum2 == A or sum2 == B:
                count += 1
        elif not group2 and group1:
            # Check if the sum of group1 equals A or B
            if sum1 == A or sum1 == B:
                count += 1

    return count

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, [1,1,1]) == 3 )
    print(solution(3, 3, 5, [1,1,1]) == 1 )
    print(solution(2, 1, 1, [1,1]) == 2 )
