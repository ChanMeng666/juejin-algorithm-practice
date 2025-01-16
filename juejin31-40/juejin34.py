def solution(n: int, nums: list) -> int:
    # 将列表转换为集合去重，再转换为列表并排序
    unique_nums = sorted(list(set(nums)), reverse=True)
    
    # 如果不同的数字少于3个，返回最大值
    if len(unique_nums) < 3:
        return unique_nums[0]
    
    # 否则返回第三大的数
    return unique_nums[2]

if __name__ == '__main__':
    print(solution(3, [3, 2, 1]) == 1)
    print(solution(2, [1, 2]) == 2)
    print(solution(4, [2, 2, 3, 1]) == 1)