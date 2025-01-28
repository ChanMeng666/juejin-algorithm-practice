def solution(airports):
    from collections import deque
    n = len(airports)
    
    # 使用BFS查找最短路径
    queue = deque([(0, 0)])  # (位置, 起飞次数)
    visited = {0}  # 记录已访问的位置
    
    while queue:
        pos, flights = queue.popleft()
        
        # 如果到达终点，返回所需的起飞次数
        if pos == n - 1:
            return flights
            
        # 尝试所有可能的下一步移动
        next_positions = set()
        
        # 添加相邻机场
        if pos + 1 < n:
            next_positions.add(pos + 1)
        if pos - 1 >= 0:
            next_positions.add(pos - 1)
            
        # 添加同一航空公司的其他机场
        for i in range(n):
            if airports[i] == airports[pos] and i != pos:
                next_positions.add(i)
                
        # 遍历所有可能的下一步位置
        for next_pos in next_positions:
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, flights + 1))
    
    return -1  # 如果无法到达终点

if __name__ == "__main__":
    # Test cases
    print(solution([10,12,13,12,14]) == 3)  # True
    print(solution([10,11,12,13,14]) == 4)  # True
    print(solution([7,7,7,8,9,7]) == 1)     # True
