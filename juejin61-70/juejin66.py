def solution(n, m, s, like):
    # 计算阶乘
    def factorial(x):
        if x == 0: return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    # dp[i][j][k]: 前i个甜点使用j个魔法棒和为k的方案数
    dp = [[[0] * (s + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1  # 初始状态
    
    # 遍历每个甜点
    for i in range(n):
        # 遍历已使用的魔法棒数量
        for j in range(m + 1):
            # 遍历当前和
            for k in range(s + 1):
                if dp[i][j][k] == 0:
                    continue
                    
                # 不选当前甜点
                dp[i + 1][j][k] += dp[i][j][k]
                
                # 选且不用魔法棒
                if k + like[i] <= s:
                    dp[i + 1][j][k + like[i]] += dp[i][j][k]
                    
                # 选且用魔法棒
                if j < m:
                    fact = factorial(like[i])
                    if k + fact <= s:
                        dp[i + 1][j + 1][k + fact] += dp[i][j][k]
    
    # 所有方案数之和
    result = 0
    for j in range(m + 1):
        result += dp[n][j][s]
        
    return result