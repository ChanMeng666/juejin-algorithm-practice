def solution(n, k, data):
    # dp[i][j] 表示到第i天开始时，手上有j份食物时的最小花费
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 初始状态
    
    # 遍历每一天
    for i in range(n):
        # 遍历当前的食物数量
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue
            
            # 当前食物不够今天消耗
            if j == 0:
                # 必须购买至少1份食物
                for buy in range(1, k + 1):
                    dp[i + 1][buy - 1] = min(
                        dp[i + 1][buy - 1],
                        dp[i][j] + buy * data[i]
                    )
            else:
                # 当前食物足够，可以选择不购买
                dp[i + 1][j - 1] = min(
                    dp[i + 1][j - 1],
                    dp[i][j]
                )
                # 也可以选择购买
                for buy in range(1, k - j + 1):
                    dp[i + 1][j + buy - 1] = min(
                        dp[i + 1][j + buy - 1],
                        dp[i][j] + buy * data[i]
                    )
    
    return dp[n][0]


if __name__ == "__main__":
    # 测试用例
    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)  # True
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]) == 9)  # True
    print(solution(4, 1, [3, 2, 4, 1]) == 10)  # True
