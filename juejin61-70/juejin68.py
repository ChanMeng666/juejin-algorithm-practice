def solution(d, w, position, supply):
    # 如果初始水量就足够到达终点，直接返回0
    if w >= d:
        return 0
    
    # 如果没有补给站，且初始水量不足，返回-1
    if not position:
        return -1
    
    # 将补给站按位置排序
    stations = list(zip(position, supply))
    stations.sort()
    
    # 当前水量和位置
    current_water = w
    current_pos = 0
    refill_count = 0
    
    while current_pos < d:
        max_reach = current_pos + current_water
        
        # 如果当前水量能直接到达终点
        if max_reach >= d:
            return refill_count
        
        # 在当前水量可达范围内找补给量最大的站点
        best_station_index = -1
        max_supply = -1
        
        for i, (station_pos, station_supply) in enumerate(stations):
            # 跳过已经过的站点
            if station_pos <= current_pos:
                continue
            # 如果站点超出了能到达的范围
            if station_pos > max_reach:
                break
            # 选择补给量最大的站点
            if station_supply > max_supply:
                max_supply = station_supply
                best_station_index = i
        
        # 如果找不到可到达的补给站
        if best_station_index == -1:
            return -1
        
        # 移动到选中的补给站
        station_pos, station_supply = stations[best_station_index]
        # 更新剩余水量（减去路上消耗的）
        current_water -= (station_pos - current_pos)
        # 在补给站补充水
        current_water = station_supply
        current_pos = station_pos
        refill_count += 1
        
        # 删除已经访问过的站点
        stations = stations[best_station_index + 1:]
    
    return refill_count

if __name__ == "__main__":
    #  You can add more test cases here
    testPosition = [170, 192, 196, 234, 261, 269, 291, 404, 1055, 1121, 1150, 1234, 1268, 1402, 1725, 1726, 1727, 1762, 1901, 1970]
    testSupply = [443, 185, 363, 392, 409, 358, 297, 70, 189, 106, 380, 130, 126, 411, 63, 186, 36, 347, 339, 50]

    print(solution(10, 4, [1,4,7], [6,3,5]) == 1 )
    print(solution(2000, 200, testPosition, testSupply) == 5 )