def solution(num):
    # 将数字转换为字符串
    s = str(num)
    n = len(s)
    
    # dp[i]表示从第i位到最后的翻译方法数
    dp = [0] * (n + 1)
    dp[n] = 1  # 空字符串只有一种翻译方法
    
    # 从后向前遍历
    for i in range(n-1, -1, -1):
        # 如果当前数字是0，那么它不能单独翻译，也不能和前一个数字组合
        if s[i] == '0':
            dp[i] = dp[i+1]
            continue
            
        # 当前数字单独翻译
        dp[i] = dp[i+1]
        
        # 当前数字和下一个数字组合翻译
        if i < n-1:
            num2 = int(s[i:i+2])
            if 10 <= num2 <= 25:
                dp[i] += dp[i+2]
    
    return dp[0]

if __name__ == "__main__":
    # 测试用例
    print(solution(12258) == 5)    # True
    print(solution(1400112) == 6)  # True
    print(solution(2110101) == 10) # True
    print(solution(25) == 2)       # True
    print(solution(1023) == 4)     # True