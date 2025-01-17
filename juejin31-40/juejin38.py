def solution(m: int, n: int, p: list[list[int]]) -> int:
    """
    计算完成旅程所需的最小花费
    
    Args:
        m (int): 总路程天数
        n (int): 补给站数量
        p (list[list[int]]): 补给站信息，每个元素为 [天数, 价格]
    
    Returns:
        int: 最小花费
    """
    # 创建dp数组，dp[i]表示到达第i天所需的最小花费
    dp = [float('inf')] * (m + 1)
    
    # 记录补给站的位置和价格
    stations = {day: price for day, price in p}
    
    # 初始化第0天的状态
    dp[0] = 0
    
    # 动态规划过程
    for i in range(m):
        # 如果当前天数有补给站
        if i in stations:
            price = stations[i]
            # 从当前补给站买食物，可以支撑到之后的每一天
            for j in range(i + 1, m + 1):
                # dp[j]可以从dp[i]转移过来，需要购买(j-i)份食物
                dp[j] = min(dp[j], dp[i] + (j - i) * price)
    
    return dp[m]


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (5, 4, [[0, 2], [1, 3], [2, 1], [3, 2]], 7),
        (6, 5, [[0, 1], [1, 5], [2, 2], [3, 4], [5, 1]], 6),
        (4, 3, [[0, 3], [2, 2], [3, 1]], 9)
    ]
    
    for i, (m, n, p, expected) in enumerate(test_cases, 1):
        result = solution(m, n, p)
        print(f"Test case {i}:")
        print(f"Input: m = {m}, n = {n}, p = {p}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'PASSED' if result == expected else 'FAILED'}\n")