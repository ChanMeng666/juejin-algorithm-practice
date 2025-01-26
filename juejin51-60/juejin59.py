def solution(n, a, b, c, s):
    # dp[i][j][k] 表示处理到第i个字符，上一次操作的奇偶性为j，当前状态为k时的最大收益
    # j: 0表示偶数，1表示奇数
    # k: 0表示当前位置是0，1表示当前位置是1
    dp = [[[-float('inf')] * 2 for _ in range(2)] for _ in range(n + 1)]
    
    # 初始状态
    dp[0][0][0] = dp[0][1][0] = 0
    dp[0][0][1] = dp[0][1][1] = 0
    
    # 遍历每个位置
    for i in range(n):
        curr = int(s[i])
        # 遍历上一次操作的奇偶性
        for last in range(2):
            # 遍历当前位置的状态
            for state in range(2):
                if dp[i][last][state] == -float('inf'):
                    continue
                    
                # 如果当前是连续的00，可以替换为0
                if i < n-1 and curr == 0 and int(s[i+1]) == 0:
                    # 替换00为0是奇数操作
                    if last != 1:  # 上一次不能是奇数
                        dp[i+2][1][0] = max(dp[i+2][1][0], dp[i][last][state] + a)
                
                # 如果当前是连续的11，可以替换为1
                if i < n-1 and curr == 1 and int(s[i+1]) == 1:
                    # 替换11为1是偶数操作
                    if last != 0:  # 上一次不能是偶数
                        dp[i+2][0][1] = max(dp[i+2][0][1], dp[i][last][state] + b)
                
                # 删除当前的0
                if curr == 0:
                    # 删除0是奇数操作
                    if last != 1:  # 上一次不能是奇数
                        dp[i+1][1][int(s[i+1]) if i+1 < n else 0] = max(
                            dp[i+1][1][int(s[i+1]) if i+1 < n else 0], 
                            dp[i][last][state] - c
                        )
                
                # 保持当前字符不变
                if i+1 < n:
                    dp[i+1][last][int(s[i+1])] = max(
                        dp[i+1][last][int(s[i+1])], 
                        dp[i][last][state]
                    )
    
    # 返回最后一个位置的最大值
    result = -float('inf')
    for last in range(2):
        for state in range(2):
            result = max(result, dp[n][last][state])
    
    return result

if __name__ == "__main__":
    # 测试用例
    print(solution(5, 2, 2, 1, "01101") == 3)
    print(solution(6, 4, 3, 5, "110001") == 11)
    print(solution(6, 3, 2, 1, "011110") == 4)
    print(solution(4, 1, 3, 2, "1111") == 3)
    print(solution(3, 2, 2, 1, "000") == 2)