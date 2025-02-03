def solution(m, w, p, n):
    # m: 机器数量
    # w: 工人数量
    # p: 购买机器或工人的成本(蛋糕数)
    # n: 目标蛋糕数量
    
    days = 0
    total_cakes = 0
    
    while total_cakes < n:
        # 如果已经生产的加上当天能生产的大于等于目标，返回天数
        if total_cakes + m * w >= n:
            return days + 1
        
        # 计算当天生产的蛋糕
        current_production = m * w
        
        # 如果当前积累的蛋糕不够买任何资源，继续生产
        if total_cakes + current_production < p:
            total_cakes += current_production
            days += 1
            continue
        
        # 计算可以购买多少个资源
        resources_to_buy = (total_cakes + current_production) // p
        
        # 计算购买后剩余的蛋糕
        total_cakes = (total_cakes + current_production) % p
        
        # 决定如何分配资源
        # 为了最大化生产效率，应该让m和w尽量接近
        while resources_to_buy > 0:
            if m < w:
                m += 1
            else:
                w += 1
            resources_to_buy -= 1
        
        days += 1
    
    return days

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, 12) == 3 )
    print(solution(10, 5, 30, 500) == 8 )
    print(solution(3, 5, 30, 320) == 14 )