def solution(n, A, B, array_a):
    def get_digit_sum(nums):
        if not nums:
            return -1
        return sum(nums) % 10
    
    count = 0
    # 使用位运算遍历所有可能的分组情况
    for i in range(1 << n):
        group1 = []
        group2 = []
        # 根据二进制位分配数字到两个组
        for j in range(n):
            if i & (1 << j):
                group1.append(array_a[j])
            else:
                group2.append(array_a[j])
        
        sum1 = get_digit_sum(group1)
        sum2 = get_digit_sum(group2)
        
        # 情况1：两个组都非空
        if group1 and group2:
            # 为避免重复计数，只在sum1 == A时计数
            if sum1 == A and sum2 == B:
                count += 1
        # 情况2：一组为空的情况
        elif not group1 and group2:
            # 检查group2的和是否等于A或B
            if sum2 == A or sum2 == B:
                count += 1
        elif not group2 and group1:
            # 检查group1的和是否等于A或B
            if sum1 == A or sum1 == B:
                count += 1
                
    return count

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, [1,1,1]) == 3 )
    print(solution(3, 3, 5, [1,1,1]) == 1 )
    print(solution(2, 1, 1, [1,1]) == 2 )