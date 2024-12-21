# 比赛配对问题

## 题目描述

小R正在组织一个比赛，比赛中有 n 支队伍参赛。比赛遵循以下独特的赛制：

1. 如果当前队伍数为**偶数**：
   - 每支队伍都会与另一支队伍配对
   - 总共进行 n/2 场比赛
   - 产生 n/2 支队伍进入下一轮

2. 如果当前队伍数为**奇数**：
   - 将会随机轮空并晋级一支队伍
   - 其余的队伍配对
   - 总共进行 (n-1)/2 场比赛
   - 产生 (n-1)/2 + 1 支队伍进入下一轮

要求计算在整个比赛过程中进行的配对次数，直到决出唯一的获胜队伍为止。

## 示例

### 示例 1:
```
输入：n = 7
输出：6
解释：
第一轮：7支队伍，1支轮空，3场比赛，4支晋级
第二轮：4支队伍，2场比赛，2支晋级
第三轮：2支队伍，1场比赛，1支晋级
总共比赛场数：3 + 2 + 1 = 6场
```

### 示例 2:
```
输入：n = 14
输出：13
解释：
第一轮：14支队伍，7场比赛，7支晋级
第二轮：7支队伍，1支轮空，3场比赛，4支晋级
第三轮：4支队伍，2场比赛，2支晋级
第四轮：2支队伍，1场比赛，1支晋级
总共比赛场数：7 + 3 + 2 + 1 = 13场
```

### 示例 3:
```
输入：n = 1
输出：0
解释：只有1支队伍，不需要进行比赛
```

## 解题思路

这是一个模拟题，我们需要模拟整个比赛的过程，直到只剩下一支队伍。关键点在于：

1. 理解每一轮比赛后晋级的队伍数量：
   - 偶数队伍：n/2 支晋级
   - 奇数队伍：(n-1)/2 + 1 支晋级（包括轮空的1支）

2. 使用循环模拟比赛过程，累加每轮的比赛场数

3. 特殊情况处理：当只有1支队伍时，不需要比赛

## 代码实现

```python
def solution(n: int) -> int:
    # 如果只有1支队伍，直接返回0
    if n == 1:
        return 0
    
    total_matches = 0
    remaining_teams = n
    
    # 当还有超过1支队伍时继续比赛
    while remaining_teams > 1:
        if remaining_teams % 2 == 0:
            # 偶数队伍：进行 n/2 场比赛
            matches = remaining_teams // 2
            remaining_teams = matches
        else:
            # 奇数队伍：一支轮空，其余队伍进行 (n-1)/2 场比赛
            matches = (remaining_teams - 1) // 2
            remaining_teams = matches + 1
        
        total_matches += matches
    
    return total_matches
```

## 代码解释

1. **特殊情况处理**：
   ```python
   if n == 1:
       return 0
   ```
   如果只有1支队伍参赛，不需要进行任何比赛。

2. **变量初始化**：
   ```python
   total_matches = 0      # 记录总比赛场数
   remaining_teams = n    # 记录当前轮次的队伍数量
   ```

3. **主循环**：
   ```python
   while remaining_teams > 1:
   ```
   只要剩余队伍数量大于1，就继续进行比赛。

4. **偶数队伍情况**：
   ```python
   if remaining_teams % 2 == 0:
       matches = remaining_teams // 2
       remaining_teams = matches
   ```
   - 当前轮次的比赛场数为队伍数的一半
   - 晋级队伍数等于比赛场数

5. **奇数队伍情况**：
   ```python
   else:
       matches = (remaining_teams - 1) // 2
       remaining_teams = matches + 1
   ```
   - 一支队伍轮空，其余队伍配对比赛
   - 晋级队伍数等于比赛场数加上轮空的1支

6. **累加比赛场数**：
   ```python
   total_matches += matches
   ```
   将每轮的比赛场数加到总场数中。

## 复杂度分析

- 时间复杂度：O(log n)，因为每轮比赛后队伍数量大约减半
- 空间复杂度：O(1)，只使用了常数额外空间

## 总结

这道题目主要考察了对比赛淘汰赛制的理解和模拟能力。关键是要理清楚：
1. 每轮比赛后晋级队伍的数量计算方式
2. 区分奇数和偶数队伍的处理方式
3. 使用循环来模拟整个比赛过程

通过这道题，我们可以学习到如何将一个实际问题转化为代码实现，以及如何处理不同的情况分支。
