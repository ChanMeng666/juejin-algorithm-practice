def solution(n):
    # 创建缓存来存储子问题的结果
    dp = {}
    
    def dfs(left, right):
        # 如果范围只有一个数，则必定猜中，获胜概率为1
        if left == right:
            return 1
        
        # 如果已经计算过这个范围，直接返回结果
        if (left, right) in dp:
            return dp[(left, right)]
        
        total = right - left + 1
        prob = 0
        
        # 遍历当前玩家可以猜的所有数字
        for guess in range(left, right + 1):
            curr_prob = 1.0 / total  # 当前数字是答案的概率
            
            # 如果猜中，当前玩家获胜
            # 如果猜小了，递归计算剩余右半部分的获胜概率
            # 如果猜大了，递归计算剩余左半部分的获胜概率
            if guess > left:
                curr_prob += (guess - left) / total * (1 - dfs(left, guess - 1))
            if guess < right:
                curr_prob += (right - guess) / total * (1 - dfs(guess + 1, right))
            
            # 取最大概率（最优策略）
            prob = max(prob, curr_prob)
        
        dp[(left, right)] = prob
        return prob
    
    # 计算从1到n的范围内的获胜概率
    result = dfs(1, n)
    # 转换为字符串并保留5位小数
    return '{:.5f}'.format(result)

if __name__ == "__main__":
    # 测试用例
    print(solution(2) == "0.50000")
    print(solution(931) == "0.50054")
    print(solution(924) == "0.50000")
    print(solution(545) == "0.50092")