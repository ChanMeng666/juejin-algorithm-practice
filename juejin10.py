def solution(a: int, b: int) -> int:
    # 使用向上取整的除法计算所需天数
    # 如果 a 不能被 b 整除，则需要多一天
    return (a + b - 1) // b

if __name__ == '__main__':
    print(solution(10, 1) == 10)
    print(solution(10, 2) == 5)
    print(solution(10, 3) == 4)