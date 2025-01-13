def solution(a: int, b: int) -> int:
    # 将数字a转换为字符串
    str_a = str(a)
    str_b = str(b)
    
    # 初始化最大值
    max_num = float('-inf')
    
    # 遍历所有可能的插入位置
    for i in range(len(str_a) + 1):
        # 在位置i处插入数字b
        new_num = int(str_a[:i] + str_b + str_a[i:])
        # 更新最大值
        max_num = max(max_num, new_num)
    
    return max_num

if __name__ == '__main__':
    print(solution(76543, 4) == 765443)
    print(solution(1, 0) == 10)
    print(solution(44, 5) == 544)
    print(solution(666, 6) == 6666)