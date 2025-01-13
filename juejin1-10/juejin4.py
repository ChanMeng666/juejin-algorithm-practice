def solution(numbers):
    # 将每个数字转换为字符串并分离成单个数字集合
    digit_groups = []
    for num in numbers:
        # 将每个数字转为字符串，然后转为集合去重
        digit_groups.append(set(str(num)))
    
    def get_digit_sum(combination):
        # 计算数字组合的各位数字之和
        return sum(int(d) for d in combination)
    
    def backtrack(current_combination, group_index):
        # 当我们处理完所有组时，检查和是否为偶数
        if group_index == len(digit_groups):
            return 1 if get_digit_sum(current_combination) % 2 == 0 else 0
        
        count = 0
        # 从当前组中选择一个数字
        for digit in digit_groups[group_index]:
            count += backtrack(current_combination + digit, group_index + 1)
        return count
    
    # 从空组合开始回溯
    return backtrack("", 0)

if __name__ == "__main__":
    # 测试用例
    print(solution([123, 456, 789]) == 14)  # True
    print(solution([123456789]) == 4)       # True
    print(solution([14329, 7568]) == 10)    # True