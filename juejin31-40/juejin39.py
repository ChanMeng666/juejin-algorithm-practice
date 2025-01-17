def solution(x_position, y_position):
    # 如果起点等于终点，不需要移动
    if x_position == y_position:
        return 0
        
    # 计算需要移动的总距离
    distance = abs(y_position - x_position)
    
    # 如果距离为1，则只需要1步
    if distance == 1:
        return 1
        
    # 如果距离为2，则需要2步
    if distance == 2:
        return 2
    
    # 对于更长的距离，我们需要考虑加速和减速
    # 初始步长为1
    steps = 3  # 最少需要3步
    current_max = 2  # 除去首尾步长1，中间最大步长从2开始
    total = 4  # 已经可以移动的距离（1 + 2 + 1 = 4）
    
    # 如果已经可以达到目标，返回当前步数
    if total >= distance:
        return steps
        
    # 继续增加步数直到可以达到目标
    while total < distance:
        steps += 1
        # 每增加两步，最大步长可以增加1
        if steps % 2 == 1:
            current_max += 1
        total += current_max
            
    return steps

if __name__ == "__main__":
    # Test cases
    print(solution(12, 6) == 4)  # True
    print(solution(34, 45) == 6)  # True
    print(solution(50, 30) == 8)  # True
    print(solution(0, 0) == 0)  # True