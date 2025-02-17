# 打点计数器问题

## 题目描述

小明正在设计一台打点计数器，该计数器可以接受多个递增的数字范围，并对这些范围内的每个唯一数字打点。如果多个范围之间有重叠，计数器将合并这些范围并只对每个唯一数字打一次点。现在需要计算在给定的多组数字范围内，计数器会打多少个点。

### 示例

**示例 1：**
```python
输入：[[1, 4], [7, 10], [3, 5]]
输出：9
解释：
- 区间 [1,4] 和 [3,5] 有重叠，合并为 [1,5]，包含数字：1,2,3,4,5
- 区间 [7,10] 保持不变，包含数字：7,8,9,10
- 总共包含 9 个唯一数字
```

**示例 2：**
```python
输入：[[1, 2], [6, 10], [11, 15]]
输出：12
解释：
- 三个区间没有重叠，分别包含：
  [1,2]: 2个数字
  [6,10]: 5个数字
  [11,15]: 5个数字
- 总共包含 12 个唯一数字
```

## 解题思路

这道题目可以分为以下几个步骤来解决：

1. **预处理**：
   - 首先检查输入数组是否为空，如果为空返回0
   - 将输入的区间按照起始位置排序，便于后续合并操作

2. **合并重叠区间**：
   - 从第一个区间开始，依次处理后续区间
   - 如果当前区间的起始位置小于等于前一个区间的结束位置+1，说明两个区间重叠或相邻
   - 合并重叠区间时，新区间的结束位置取两个区间结束位置的较大值
   - 如果不重叠，则将当前区间添加到结果中

3. **计算总点数**：
   - 遍历合并后的所有区间
   - 对每个区间，计算其包含的数字个数（end - start + 1）
   - 将所有区间的数字个数相加得到最终结果

## 代码实现

```python
def solution(inputArray):
    if not inputArray:
        return 0
    
    # 按照区间起始位置排序
    intervals = sorted(inputArray, key=lambda x: x[0])
    
    # 合并重叠区间
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1] + 1:  # 如果当前区间与上一个区间重叠或相邻
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    # 计算所有区间内的数字总数
    total_points = 0
    for start, end in merged:
        total_points += end - start + 1
        
    return total_points
```

## 复杂度分析

- **时间复杂度**：O(nlogn)，其中 n 是输入区间的数量。主要开销来自对区间的排序。
- **空间复杂度**：O(n)，需要存储合并后的区间。

## 注意事项

1. 区间合并时需要考虑相邻的情况（如 [1,2] 和 [3,4]）
2. 计算区间内数字个数时要包含起始和结束数字
3. 输入数组为空时需要特殊处理

## 相关题目

- 区间合并
- 区间重叠问题
- 区间调度问题

## 总结

这道题目是区间处理的经典问题，核心在于：
1. 理解如何判断区间的重叠或相邻关系
2. 掌握区间合并的技巧
3. 正确计算合并后区间内的数字个数

解决此类问题的通用方法是：先排序，再合并，最后统计。这种思路也可以应用到其他类似的区间处理问题中。

