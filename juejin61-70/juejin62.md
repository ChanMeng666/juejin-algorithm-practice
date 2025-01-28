# 病毒传播问题

## 题目描述

在一个封闭的房间中，排列着 n 行 m 列的座位，每个座位间距为 1 米。房间中每个座位上都坐着一人，部分人戴了口罩（用1表示），部分人未戴口罩（用0表示）。已知房间中有一位已经感染病毒的人，病毒可以每秒向相邻座位传播 1 米。

对于戴口罩的人：
1. 病毒需要两秒才能成功感染
2. 如果同时有多个感染源（至少一个相邻感染者），则只需要1秒就能被感染

要求设计一个算法，计算病毒感染房间内所有人所需的最短时间。如果无法感染所有人，则返回0。

## 示例

### 示例1
```
输入：
row_n = 4, column_m = 4
seats = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,1,1],
    [0,0,0,1]
]
patient = [2,2]

输出：6

解释：从位置[2,2]开始传播，考虑到部分人戴口罩需要2秒感染，最终需要6秒才能感染所有人。
```

### 示例2
```
输入：
row_n = 4, column_m = 4
seats = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,1,1],
    [0,0,0,1]
]
patient = [2,5]

输出：0

解释：初始感染者的位置在数组范围外，无法开始传播，因此返回0。
```

## 解题思路

这是一个典型的图搜索问题，可以使用广度优先搜索(BFS)来解决。主要难点在于处理戴口罩情况下的传播时间计算。

### 算法步骤

1. **初始化**
   - 创建距离数组dist，用float('inf')表示未访问的位置
   - 使用双端队列存储待处理的位置
   - 将初始感染者位置加入队列，距离设为0

2. **BFS遍历**
   - 从队列中取出当前位置和时间
   - 遍历四个方向（上、下、左、右）
   - 对于每个新位置，根据是否戴口罩计算传播时间：
     - 未戴口罩：传播时间+1
     - 戴口罩：检查周围是否有其他感染源
       - 有至少一个其他感染源：传播时间+1
       - 没有其他感染源：传播时间+2

3. **更新传播时间**
   - 如果找到更短的传播时间，更新dist数组
   - 将新位置加入队列继续传播

4. **结果判断**
   - 遍历所有位置，如果存在无法到达的位置（dist值为inf），返回0
   - 否则返回最大的传播时间

### 代码实现

```python
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
```

## 复杂度分析

- 时间复杂度：O(N*M*K)，其中N和M是房间的行数和列数，K是检查周围感染源的常数时间
- 空间复杂度：O(N*M)，主要是距离数组和队列的空间开销

## 注意事项

1. 需要特别注意边界条件的处理，包括：
   - 输入数组为空
   - 初始感染者位置无效
   - 无法感染所有人的情况

2. 对于戴口罩的人，要正确处理多个感染源的情况：
   - 检查除当前传播源外是否还有其他感染源
   - 根据感染源数量决定传播时间

3. 使用float('inf')作为初始值可以方便地判断未访问的位置和更新最短时间

4. BFS保证了我们能找到最短的传播时间路径

