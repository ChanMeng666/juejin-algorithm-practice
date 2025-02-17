# 最优加油方案问题

## 题目描述

小F计划从青海湖出发，前往一个遥远的景点X进行旅游。他需要规划一个最优的加油方案，使得总的燃油成本最小。具体条件如下：

- 车辆油箱容量为400L
- 起点时车内剩余油量为200L
- 每行驶1km消耗1L油
- 到达终点还车时需保证剩余油量至少200L
- 沿途设有多个加油站，每个加油站的油价不同

### 输入参数
- distance：总距离（km），不超过10000 km
- n：沿途加油站数量（1 <= n <= 100）
- gas_stations：加油站信息列表，每个元素为 [距起点距离, 油价]

### 输出要求
- 返回最小花费金额
- 如果无法到达终点或无法满足还车时的油量要求，返回-1

## 解题思路

### 1. 可行性检查

首先需要进行一系列可行性检查：

1. 无加油站情况检查：
   - 如果没有加油站，检查初始油量是否足够到达终点
   
2. 数据格式检查：
   - 确保每个加油站信息包含距离和油价两个参数
   
3. 距离可达性检查：
   - 检查第一个加油站是否在初始油量可达范围内（<=200km）
   - 检查相邻加油站之间距离是否在油箱容量可达范围内（<=400km）
   - 检查最后一个加油站到终点的距离是否可达（<=400km）

### 2. 动态规划解法

#### 状态定义
- dp[i][j]：表示到达第i个加油站时，剩余j升油的最小成本

#### 初始状态
- dp[0][200] = 0：表示起点有200L油，成本为0
- 其他状态初始化为无穷大

#### 状态转移
对于每个加油站i：
1. 计算从上一个加油站到达当前加油站消耗的油量
2. 对于上一个状态的每种可能油量：
   - 计算到达当前加油站后的剩余油量
   - 考虑在当前加油站加不同数量的油
   - 更新dp数组，取最小成本

#### 最终结果计算
1. 计算从最后一个加油站到终点需要的油量
2. 检查所有可能的终点剩余油量状态（>=200L）
3. 在满足条件的状态中找出最小成本

## 代码实现要点

1. 预处理：
```python
# 对加油站按距离排序
gas_stations.sort(key=lambda x: x[0])
```

2. 状态转移核心逻辑：
```python
for i in range(n):
    prev_dist = 0 if i == 0 else gas_stations[i-1][0]
    curr_dist = gas_stations[i][0]
    cost = curr_dist - prev_dist
    
    for prev_fuel in range(cost, 401):
        if dp[i][prev_fuel] == float('inf'):
            continue
        
        curr_fuel = prev_fuel - cost
        
        for add_fuel in range(401 - curr_fuel):
            if curr_fuel + add_fuel <= 400:
                dp[i+1][curr_fuel + add_fuel] = min(
                    dp[i+1][curr_fuel + add_fuel],
                    dp[i][prev_fuel] + add_fuel * gas_stations[i][1]
                )
```

## 复杂度分析

- 时间复杂度：O(n * F * F)
  - n 是加油站数量
  - F 是油箱容量（这里是400）
  - 对每个加油站，需要考虑前一状态的每种油量，以及当前可加的每种油量

- 空间复杂度：O(n * F)
  - 需要一个二维dp数组存储状态

## 注意事项

1. 边界条件处理：
   - 无加油站的情况
   - 加油站数据格式异常的情况
   - 距离不可达的情况

2. 状态转移时的限制：
   - 确保油箱容量不超过400L
   - 确保到达终点时剩余油量至少200L

3. 最优解判断：
   - 如果找不到可行解，返回-1
   - 在所有可行解中选择成本最小的方案

