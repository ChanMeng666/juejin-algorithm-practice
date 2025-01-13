# 最佳观光组合

## 题目描述

小R正在研究一组观光景点，每个景点都有一个评分，保存在数组 values 中，其中 values[i] 表示第 i 个观光景点的评分。同时，景点之间的距离由它们的下标差 j - i 表示。

一对景点 (i < j) 的观光组合得分计算公式为：values[i] + values[j] + i - j

要求找出能获得的最高观光组合得分。

### 约束条件
- 2 <= values.length
- 1 <= values[i] <= 1000

### 示例
**示例 1:**
```python
输入：values = [8, 3, 5, 5, 6]
输出：11
解释：i = 0, j = 2 时得到最高分：8 + 5 + 0 - 2 = 11
```

**示例 2:**
```python
输入：values = [10, 4, 8, 7]
输出：16
解释：i = 0, j = 2 时得到最高分：10 + 8 + 0 - 2 = 16
```

**示例 3:**
```python
输入：values = [1, 2, 3, 4, 5]
输出：8
解释：i = 2, j = 4 时得到最高分：3 + 5 + 2 - 4 = 8
```

## 解题思路

这道题乍看可能有点复杂，让我们一步步分析：

1. **公式转换**
   - 原始公式：values[i] + values[j] + i - j
   - 可以重写为：(values[i] + i) + (values[j] - j)
   - 这样的转换让我们看到了问题的本质

2. **关键发现**
   - 对于任意位置j，我们需要在它之前找到最大的(values[i] + i)
   - 这样就把问题转化为了维护前缀最大值的问题

3. **解决方案**
   - 用一个变量记录之前位置中(values[i] + i)的最大值
   - 遍历每个位置j，计算当前得分并更新最大得分
   - 同时更新(values[i] + i)的最大值

## 代码实现

```python
def solution(values: list) -> int:
    max_score = float('-inf')  # 初始化最大得分为负无穷
    max_value_plus_i = values[0] + 0  # 初始化第一个位置的values[i] + i
    
    # 遍历从第二个位置开始的所有景点
    for j in range(1, len(values)):
        # 计算当前组合得分
        current_score = max_value_plus_i + (values[j] - j)
        max_score = max(max_score, current_score)
        
        # 更新max_value_plus_i，为下一轮做准备
        max_value_plus_i = max(max_value_plus_i, values[j] + j)
    
    return max_score
```

## 代码详解

1. **初始化**
   ```python
   max_score = float('-inf')
   max_value_plus_i = values[0] + 0
   ```
   - 初始化最大得分为负无穷
   - 初始化第一个位置的values[i] + i值

2. **主循环**
   ```python
   for j in range(1, len(values)):
       current_score = max_value_plus_i + (values[j] - j)
   ```
   - 从第二个位置开始遍历
   - 利用当前位置j和之前的最大values[i] + i计算得分

3. **更新最大值**
   ```python
   max_score = max(max_score, current_score)
   max_value_plus_i = max(max_value_plus_i, values[j] + j)
   ```
   - 更新全局最大得分
   - 更新values[i] + i的最大值，为下一轮计算做准备

## 复杂度分析

- **时间复杂度**: O(n)，其中n是数组长度，只需要遍历一次数组
- **空间复杂度**: O(1)，只使用了常数个变量

## 易错点提醒

1. 不要尝试使用双重循环暴力解决，那样会导致O(n²)的时间复杂度
2. 注意公式转换后的理解，(values[i] + i) + (values[j] - j)是解决这道题的关键
3. 初始化max_score时要用负无穷，而不是0
4. 记得在每次循环中都要更新max_value_plus_i

## 相关题目推荐

- 买卖股票的最佳时机
- 最大子数组和
- 前缀和相关问题

这道题是一道很好的动态规划思维训练题，通过公式转换和维护最大值的方式，可以把看似复杂的问题简化成线性时间复杂度的解法。

