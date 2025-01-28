from collections import deque

def solution(row_n, column_m, seats, patient):
    if not seats or not seats[0]:
        return 0
    
    # 检查病人位置是否有效
    if patient[0] < 0 or patient[0] >= row_n or patient[1] < 0 or patient[1] >= column_m:
        return 0
    
    # 初始化距离数组
    dist = [[float('inf')] * column_m for _ in range(row_n)]
    
    # 方向数组：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 使用双端队列进行BFS
    queue = deque()
    queue.append((patient[0], patient[1]))
    dist[patient[0]][patient[1]] = 0
    
    while queue:
        curr_row, curr_col = queue.popleft()
        curr_time = dist[curr_row][curr_col]
        
        for dx, dy in directions:
            new_row, new_col = curr_row + dx, curr_col + dy
            
            if 0 <= new_row < row_n and 0 <= new_col < column_m:
                # 计算到达新位置的时间
                if seats[new_row][new_col] == 1:  # 戴口罩
                    # 检查是否有多个感染源
                    infected_count = 0
                    for dx2, dy2 in directions:
                        r2, c2 = new_row + dx2, new_col + dy2
                        if (0 <= r2 < row_n and 0 <= c2 < column_m and 
                            dist[r2][c2] <= curr_time and (r2, c2) != (curr_row, curr_col)):
                            infected_count += 1
                    
                    new_time = curr_time + (1 if infected_count >= 1 else 2)
                else:  # 未戴口罩
                    new_time = curr_time + 1
                
                if new_time < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_time
                    queue.append((new_row, new_col))
    
    # 找出最大感染时间，同时检查是否所有人都被感染
    max_time = 0
    for i in range(row_n):
        for j in range(column_m):
            if dist[i][j] == float('inf'):
                return 0  # 有人未被感染
            max_time = max(max_time, dist[i][j])
    
    return max_time

if __name__ == "__main__":
    #  You can add more test cases here
    testSeats1 = [[0,1,1,1],[1,0,1,0],[1,1,1,1],[0,0,0,1]]
    testSeats2 = [[0,1,1,1],[1,0,1,0],[1,1,1,1],[0,0,0,1]]
    testSeats3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    testSeats4 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    testSeats5 = [[1]]

    print(solution(4, 4, testSeats1, [2, 2]) == 6 )
    print(solution(4, 4, testSeats2, [2, 5]) == 0 )
    print(solution(4, 4, testSeats3, [2, 2]) == 4 )
    print(solution(4, 4, testSeats4, [2, 2]) == 6 )
    print(solution(1, 1, testSeats5, [0, 0]) == 0 )