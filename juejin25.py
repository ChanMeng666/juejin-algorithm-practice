def solution(dna1, dna2):
    # 创建动态规划矩阵
    m, n = len(dna1), len(dna2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化第一行和第一列
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # 填充dp矩阵
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # 取三种操作中的最小值：替换、删除、插入
                dp[i][j] = min(
                    dp[i-1][j-1] + 1,  # 替换
                    dp[i-1][j] + 1,    # 删除
                    dp[i][j-1] + 1     # 插入
                )
    
    return dp[m][n]

if __name__ == "__main__":
    # 测试用例
    print(solution("AGT", "AGCT") == 1)        # True
    print(solution("AACCGGTT", "AACCTTGG") == 4)  # True
    print(solution("ACGT", "TGC") == 3)        # True
    print(solution("A", "T") == 1)             # True
    print(solution("GGGG", "TTTT") == 4)       # True
    print(solution("AGCTTAGC", "AGCTAGCT") == 2)  # True
    print(solution("AGCCGAGC", "GCTAGCT") == 4)   # True