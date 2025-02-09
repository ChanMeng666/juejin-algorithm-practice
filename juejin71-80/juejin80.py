def solution(stocks):
    if not stocks or len(stocks) < 2:
        return 0
        
    # 定义三个状态：
    # hold: 持有股票时的最大收益
    # sold: 卖出股票后在冷冻期的最大收益
    # rest: 不持有股票且不在冷冻期的最大收益
    hold = [-float('inf')] * len(stocks)
    sold = [0] * len(stocks)
    rest = [0] * len(stocks)
    
    # 初始状态
    hold[0] = -stocks[0]  # 第一天买入股票
    
    for i in range(1, len(stocks)):
        # 当天持有股票的状态可能来自：
        # 1. 前一天就持有股票
        # 2. 前一天不持有股票且不在冷冻期，今天买入
        hold[i] = max(hold[i-1], rest[i-1] - stocks[i])
        
        # 当天卖出股票（进入冷冻期）的状态只能来自：
        # 前一天持有股票，今天卖出
        sold[i] = hold[i-1] + stocks[i]
        
        # 当天不持有股票且不在冷冻期的状态可能来自：
        # 1. 前一天也不持有股票且不在冷冻期
        # 2. 前一天在冷冻期
        rest[i] = max(rest[i-1], sold[i-1])
    
    # 最后一天的最大收益一定是不持有股票的状态
    return max(sold[-1], rest[-1])

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 2]) == 1 )
    print(solution([2, 1]) == 0 )
    print(solution([1, 2, 3, 0, 2]) == 3 )
    print(solution([2, 3, 4, 5, 6, 7]) == 5 )
    print(solution([1, 6, 2, 7, 13, 2, 8]) == 12 )