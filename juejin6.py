def solution(n: int, H: int, A: int, h: list, a: list) -> int:
    # 创建一个数组来存储以每个怪物结尾的最长可击败序列长度
    dp = [0] * n
    
    # 遍历每个怪物
    for i in range(n):
        # 如果当前怪物可以被击败
        if H > h[i] and A > a[i]:
            # 初始化为1，表示至少可以击败当前怪物
            dp[i] = 1
            # 检查之前的怪物
            for j in range(i):
                # 如果之前的怪物也被击败了，且满足序列要求
                if dp[j] > 0 and h[i] > h[j] and a[i] > a[j]:
                    # 更新最长序列长度
                    dp[i] = max(dp[i], dp[j] + 1)
    
    # 返回最长序列长度
    return max(dp) if any(dp) else 0

if __name__ == '__main__':
    print(solution(3, 4, 5, [1, 2, 3], [3, 2, 1]) == 1)
    print(solution(5, 10, 10, [6, 9, 12, 4, 7], [8, 9, 10, 2, 5]) == 2)
    print(solution(4, 20, 25, [10, 15, 18, 22], [12, 18, 20, 26]) == 3)