def solution(distance, n, gas_stations):
    # 如果没有加油站且距离大于当前油量可行驶的距离，返回-1
    if n == 0 and distance > 200:
        return -1
    
    # 验证加油站数据格式
    for station in gas_stations:
        if len(station) != 2:
            return -1
            
    # 对加油站按距离排序
    gas_stations.sort(key=lambda x: x[0])
    
    # 验证第一个加油站是否可达
    if n > 0 and gas_stations[0][0] > 200:
        return -1
        
    # 验证相邻加油站之间的距离是否可达
    for i in range(n-1):
        if gas_stations[i+1][0] - gas_stations[i][0] > 400:
            return -1
            
    # 验证最后一个加油站到终点的距离是否可达
    if n > 0 and distance - gas_stations[-1][0] > 400:
        return -1
    elif n == 0 and distance > 400:
        return -1
        
    # 初始化dp数组，dp[i][j]表示到达第i个加油站时剩余j升油的最小成本
    dp = [[float('inf')] * 401 for _ in range(n + 1)]
    
    # 初始状态：起点有200L油
    dp[0][200] = 0
    
    # 对每个加油站
    for i in range(n):
        # 计算到达当前加油站消耗的油量
        prev_dist = 0 if i == 0 else gas_stations[i-1][0]
        curr_dist = gas_stations[i][0]
        cost = curr_dist - prev_dist
        
        # 对于上一个状态的每种油量
        for prev_fuel in range(cost, 401):
            if dp[i][prev_fuel] == float('inf'):
                continue
                
            # 到达当前加油站后的剩余油量
            curr_fuel = prev_fuel - cost
            
            # 可以选择加或不加油
            for add_fuel in range(401 - curr_fuel):
                if curr_fuel + add_fuel <= 400:
                    dp[i+1][curr_fuel + add_fuel] = min(
                        dp[i+1][curr_fuel + add_fuel],
                        dp[i][prev_fuel] + add_fuel * gas_stations[i][1]
                    )
    
    # 计算从最后一个加油站到终点
    final_cost = float('inf')
    last_dist = 0 if n == 0 else gas_stations[-1][0]
    remain_dist = distance - last_dist
    
    # 检查每种可能的到达终点时的油量状态
    for fuel in range(remain_dist + 200, 401):
        if dp[n][fuel] != float('inf'):
            final_cost = min(final_cost, dp[n][fuel])
            
    return final_cost if final_cost != float('inf') else -1


if __name__ == "__main__":
    #  You can add more test cases here
    gas_stations1 = [(100, 1), (200, 30), (400, 40), (300, 20)]
    gas_stations2 = [(100, 999), (150, 888), (200, 777),
                     (300, 999), (400, 1009), (450, 1019), (500, 1399)]
    gas_stations3 = [(101,), (100, 100), (102, 1)]
    gas_stations4 = [(34, 1), (105, 9), (9, 10), (134, 66), (215, 90), (999, 1999), (49, 0), (10, 1999), (200, 2),
                     (300, 500), (12, 34), (1, 23), (46, 20), (80, 12), (1, 1999), (90, 33), (101, 23), (34, 88), (103, 0), (1, 1)]

    print(solution(500, 4, gas_stations1) == 4300)
    print(solution(500, 7, gas_stations2) == 410700)
    print(solution(500, 3, gas_stations3) == -1)
    print(solution(100, 20, gas_stations4) == 0)
    print(solution(100, 0, []) == -1)
