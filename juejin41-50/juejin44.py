def solution(x: int, y: int) -> int:
    # 计算射击点到靶心的距离
    distance = (x * x + y * y) ** 0.5
    
    # 如果距离大于10，超出所有环，得0分
    if distance > 10:
        return 0
        
    # 向上取整得到所在环数，然后用11减去环数得到分数
    ring = int(distance) + (1 if distance > int(distance) else 0)
    return 11 - ring

if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)