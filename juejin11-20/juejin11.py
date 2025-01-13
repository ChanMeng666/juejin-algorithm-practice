def solution(values: list) -> int:
    max_score = float('-inf')  # 初始化最大得分为负无穷
    max_value_plus_i = values[0] + 0  # 初始化第一个位置的values[i] + i
    
    # 遍历从第二个位置开始的所有景点
    for j in range(1, len(values)):
        # 计算当前组合得分
        current_score = max_value_plus_i + (values[j] - j)
        max_score = max(max_score, current_score)
        
        # 更新max_value_plus_i，为下一轮做准备
        max_value_plus_i = max(max_value_plus_i, values[j] + j)
    
    return max_score

if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)