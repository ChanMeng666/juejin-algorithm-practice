def solution(array):
    # 使用摩尔投票算法
    candidate = array[0]  # 候选数字
    count = 1  # 计数器
    
    # 第一遍遍历：找出可能的众数
    for num in array[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # 第二遍遍历：验证这个数字是否确实出现超过一半
    count = sum(1 for num in array if num == candidate)
    if count > len(array) // 2:
        return candidate
    
    return 0  # 如果没有符合条件的数字（虽然根据题目描述这种情况不会发生）


if __name__ == "__main__":
    # 测试用例
    print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]) == 3)  # True
    print(solution([5, 5, 5, 1, 2, 5, 5]) == 5)  # True
    print(solution([9, 9, 9, 9, 8, 9, 8, 8]) == 9)  # True
