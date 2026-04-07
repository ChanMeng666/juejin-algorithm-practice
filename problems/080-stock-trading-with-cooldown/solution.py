def solution(stocks):
    if not stocks or len(stocks) < 2:
        return 0

    # Define three states:
    # hold: maximum profit while holding a stock
    # sold: maximum profit after selling a stock (in cooldown period)
    # rest: maximum profit while not holding a stock and not in cooldown
    hold = [-float('inf')] * len(stocks)
    sold = [0] * len(stocks)
    rest = [0] * len(stocks)

    # Initial state
    hold[0] = -stocks[0]  # Buy stock on the first day

    for i in range(1, len(stocks)):
        # Holding stock today can come from:
        # 1. Already held stock yesterday
        # 2. Was not holding and not in cooldown yesterday, bought today
        hold[i] = max(hold[i-1], rest[i-1] - stocks[i])

        # Sold stock today (entering cooldown) can only come from:
        # Held stock yesterday, sold today
        sold[i] = hold[i-1] + stocks[i]

        # Not holding stock and not in cooldown today can come from:
        # 1. Was also not holding and not in cooldown yesterday
        # 2. Was in cooldown yesterday
        rest[i] = max(rest[i-1], sold[i-1])

    # Maximum profit on the last day must be in a state of not holding stock
    return max(sold[-1], rest[-1])

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 2]) == 1 )
    print(solution([2, 1]) == 0 )
    print(solution([1, 2, 3, 0, 2]) == 3 )
    print(solution([2, 3, 4, 5, 6, 7]) == 5 )
    print(solution([1, 6, 2, 7, 13, 2, 8]) == 12 )
