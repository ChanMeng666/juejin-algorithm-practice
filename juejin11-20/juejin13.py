def solution(n: int) -> list:
    result = []
    # 从1到n遍历，构造每一组数字
    for i in range(1, n + 1):
        # 从n倒序到i，添加到结果数组中
        for j in range(n, i - 1, -1):
            result.append(j)
    return result

if __name__ == '__main__':
    print(solution(3) == [3, 2, 1, 3, 2, 3])
    print(solution(4) == [4, 3, 2, 1, 4, 3, 2, 4, 3, 4])
    print(solution(5) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5])