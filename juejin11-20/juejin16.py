def solution(n, array):
    max_area = 0
    
    # 遍历所有可能的窗口大小k
    for k in range(1, n + 1):
        # 遍历所有可能的起始位置
        for i in range(n - k + 1):
            # 获取当前窗口中的最小值
            min_height = min(array[i:i + k])
            # 计算当前窗口的矩形面积
            area = k * min_height
            # 更新最大面积
            max_area = max(max_area, area)
    
    return max_area


if __name__ == "__main__":
    # 测试用例
    print(solution(5, [1, 2, 3, 4, 5]) == 9)  # True
    print(solution(6, [5, 4, 3, 2, 1, 6]) == 9)  # True
    print(solution(4, [4, 4, 4, 4]) == 16)  # True
