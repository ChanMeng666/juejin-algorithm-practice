def solution(x_position, y_position):
    # 如果起点等于终点，直接返回0
    if x_position == y_position:
        return 0
    
    # 计算需要移动的总距离
    distance = abs(y_position - x_position)
    
    # 如果距离为1，直接返回1
    if distance == 1:
        return 1
        
    # 计算最小步数
    # 从k=2开始尝试，k表示步数
    k = 2
    while True:
        # 计算k步能达到的最大距离
        max_dist = k * (k - 1) // 2 + 1
        if max_dist >= distance and (max_dist - distance) % 2 == 0:
            return k
        k += 1

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(12, 6) == 4)  # True
    print(solution(34, 45) == 6)  # True
    print(solution(50, 30) == 8)  # True
    print(solution(0, 0) == 0)    # True