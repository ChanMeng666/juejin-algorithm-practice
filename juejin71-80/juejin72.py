def solution(num, data):
    # 将字符串转换为列表以便修改
    dominoes = list(data)
    n = len(dominoes)
    
    # 记录每个位置的受力情况
    forces = [0] * n
    
    # 从左向右处理R的影响
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n
        elif dominoes[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] += force
    
    # 从右向左处理L的影响
    force = 0
    for i in range(n-1, -1, -1):
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] -= force
    
    # 找出保持竖直的骨牌位置
    standing = []
    for i in range(n):
        if forces[i] == 0 and dominoes[i] == '.':
            standing.append(i + 1)  # 转换为1-based索引
    
    # 格式化输出
    if not standing:
        return '0'
    return f'{len(standing)}:{",".join(map(str, standing))}'

if __name__ == "__main__":
    # 测试用例
    print(solution(14, ".L.R...LR..L..") == "4:3,6,13,14")
    print(solution(5, "R....") == "0")
    print(solution(1, ".") == "1:1")