# 最优食物补给策略问题

## 题目描述

小R正在计划一次从地点A到地点B的徒步旅行，总路程需要 N 天。为了在旅途中保持充足的能量，小R每天必须消耗1份食物。幸运的是，小R在路途中每天都会经过一个补给站，可以先购买完食物后再消耗今天的1份食物。然而，每个补给站的食物每份的价格可能不同，并且小R在购买完食物后最多只能同时携带 K 份食物。

现在，小R希望在保证每天食物消耗的前提下，以最小的花费完成这次徒步旅行。你能帮助小R计算出最低的花费是多少吗？

### 输入格式
- n：总路程需要的天数
- k：小R最多能同时携带食物的份数
- data[i]：第i天补给站每份食物的价格

### 输出格式
返回完成这次徒步旅行的最小花费

### 约束条件
- 1 < n,k < 1000
- 1 < data[i] < 10000

### 示例
**示例1：**
```python
输入：n = 5, k = 2, data = [1, 2, 3, 3, 2]
输出：9
```

**示例2：**
```python
输入：n = 6, k = 3, data = [4, 1, 5, 2, 1, 3]
输出：9
```

**示例3：**
```python
输入：n = 4, k = 1, data = [3, 2, 4, 1]
输出：10
```

## 解题思路

这是一个典型的动态规划问题。我们需要在每一天做出最优决策：是否购买食物，购买多少份食物。

### 关键点分析

1. **状态定义**
   - 使用二维数组dp[i][j]表示到第i天开始时，手上有j份食物时的最小花费
   - i的范围是[0, n]，j的范围是[0, k]

2. **状态转移**
   - 对于每一天，我们需要考虑两种情况：
     1. 当前没有食物(j=0)：必须购买至少1份食物
     2. 当前有食物(j>0)：可以选择不购买，或者购买一些补充

3. **边界条件**
   - 初始状态：dp[0][0] = 0
   - 其他初始状态：dp[0][j] = 无穷大 (j > 0)

### 代码实现

```python
def solution(n, k, data):
    # dp[i][j] 表示到第i天开始时，手上有j份食物时的最小花费
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 初始状态
    
    # 遍历每一天
    for i in range(n):
        # 遍历当前的食物数量
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue
            
            # 当前食物不够今天消耗
            if j == 0:
                # 必须购买至少1份食物
                for buy in range(1, k + 1):
                    dp[i + 1][buy - 1] = min(
                        dp[i + 1][buy - 1],
                        dp[i][j] + buy * data[i]
                    )
            else:
                # 当前食物足够，可以选择不购买
                dp[i + 1][j - 1] = min(
                    dp[i + 1][j - 1],
                    dp[i][j]
                )
                # 也可以选择购买
                for buy in range(1, k - j + 1):
                    dp[i + 1][j + buy - 1] = min(
                        dp[i + 1][j + buy - 1],
                        dp[i][j] + buy * data[i]
                    )
    
    return dp[n][0]
```

### 代码详解

1. **初始化**
   ```python
   dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
   dp[0][0] = 0  # 初始状态
   ```
   - 创建(n+1)×(k+1)的二维数组
   - 初始状态设置为无穷大，除了dp[0][0]=0

2. **主循环**
   ```python
   for i in range(n):
       for j in range(k + 1):
   ```
   - 遍历每一天和可能的食物数量

3. **处理没有食物的情况**
   ```python
   if j == 0:
       for buy in range(1, k + 1):
           dp[i + 1][buy - 1] = min(
               dp[i + 1][buy - 1],
               dp[i][j] + buy * data[i]
           )
   ```
   - 当没有食物时，必须购买至少1份
   - 可以购买的数量范围是[1, k]

4. **处理有食物的情况**
   ```python
   else:
       # 不购买的情况
       dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
       # 购买的情况
       for buy in range(1, k - j + 1):
           dp[i + 1][j + buy - 1] = min(
               dp[i + 1][j + buy - 1],
               dp[i][j] + buy * data[i]
           )
   ```
   - 当有食物时，可以选择不购买
   - 也可以选择购买一些，但要考虑容量限制

### 示例1详细解析
对于输入：n = 5, k = 2, data = [1, 2, 3, 3, 2]

最优策略是：
1. 第1天：买2份，花费2（消耗1份，剩1份）
2. 第2天：买2份，花费4（消耗1份，剩2份）
3. 第3天：不买，消耗1份（剩1份）
4. 第4天：不买，消耗1份（剩0份）
5. 第5天：买1份，花费3（消耗1份，剩0份）

总花费：2 + 4 + 0 + 0 + 3 = 9

## 总结

这道题目是一个典型的动态规划问题，关键在于：
1. 正确定义状态（dp数组的含义）
2. 找出状态转移方程
3. 处理好边界条件
4. 考虑清楚每天的决策选择

解题时需要特别注意：
- 每天必须消耗1份食物
- 购买数量的限制
- 当前没有食物时必须购买
- 最终状态必须是没有剩余食物