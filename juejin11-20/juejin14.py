def solution(n: int, k: int) -> int:
    # 创建一个数组存储选中的数
    result = []
    # 从k开始，找到n个k的倍数
    current = k
    while len(result) < n:
        result.append(current)
        current += k
    
    # 返回数组元素之和
    return sum(result)

if __name__ == '__main__':
    print(solution(n = 3, k = 1) == 6)  # 1 + 2 + 3 = 6
    print(solution(n = 2, k = 2) == 6)  # 2 + 4 = 6
    print(solution(n = 4, k = 3) == 30) # 3 + 6 + 9 + 12 = 30