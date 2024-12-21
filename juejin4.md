# 数字组合求和问题

## 题目描述

小M面对一组从1到9的数字，这些数字被分成多个小组，需要从每个小组中选择一个数字组成一个新的数。目标是计算出有多少种不同的选择方法，使得组成的新数的各位数字之和为偶数。

### 输入格式
- numbers: 一个整数列表，每个整数代表一个数字组

### 输出格式
- 返回一个整数，表示满足条件的组合数量

### 示例
```python
输入：numbers = [123, 456, 789]
输出：14
解释：符合条件的14个数为：147, 149, 158, 167, 169, 248, 257, 259, 268, 347, 349, 358, 367, 369

输入：numbers = [123456789]
输出：4

输入：numbers = [14329, 7568]
输出：10
```

## 解题思路

1. **问题分析**
   - 我们需要从每个数字组中选择一个数字
   - 选择的数字组合起来后，各位数字之和必须是偶数
   - 需要计算所有可能的组合数量

2. **解决方案**
   - 使用回溯法（递归）来生成所有可能的组合
   - 对每个数字组，先转换为字符串并去重，避免重复计算
   - 递归时逐个选择数字，直到处理完所有组
   - 检查最终组合的数字之和是否为偶数

## 代码实现

```python
def solution(numbers):
    # 将每个数字转换为字符串并分离成单个数字集合
    digit_groups = []
    for num in numbers:
        # 将每个数字转为字符串，然后转为集合去重
        digit_groups.append(set(str(num)))
    
    def get_digit_sum(combination):
        # 计算数字组合的各位数字之和
        return sum(int(d) for d in combination)
    
    def backtrack(current_combination, group_index):
        # 当我们处理完所有组时，检查和是否为偶数
        if group_index == len(digit_groups):
            return 1 if get_digit_sum(current_combination) % 2 == 0 else 0
        
        count = 0
        # 从当前组中选择一个数字
        for digit in digit_groups[group_index]:
            count += backtrack(current_combination + digit, group_index + 1)
        return count
    
    # 从空组合开始回溯
    return backtrack("", 0)
```

## 代码详解

1. **数据预处理**
   ```python
   digit_groups = []
   for num in numbers:
       digit_groups.append(set(str(num)))
   ```
   - 将每个输入数字转换为字符串
   - 使用集合去除重复数字
   - 存储在digit_groups列表中

2. **辅助函数：计算数字之和**
   ```python
   def get_digit_sum(combination):
       return sum(int(d) for d in combination)
   ```
   - 接收一个字符串形式的数字组合
   - 将每个字符转换为整数并求和

3. **回溯函数**
   ```python
   def backtrack(current_combination, group_index):
   ```
   - current_combination: 当前已选择的数字组合
   - group_index: 当前处理的数字组索引
   - 递归终止条件：处理完所有组时，检查和是否为偶数
   - 递归过程：遍历当前组的每个数字，将其添加到组合中继续递归

## 复杂度分析

- 时间复杂度：O(9^n)，其中n是数字组的数量。每个组最多有9个不同的数字可选。
- 空间复杂度：O(n)，主要是递归调用栈的深度。

## 总结

这道题目是一个典型的回溯算法应用。通过递归生成所有可能的组合，并检查每个组合是否满足条件。关键点在于：
1. 使用集合去重，避免重复计算
2. 递归时传递当前组合和处理的组索引
3. 使用字符串拼接来构建组合，便于计算各位数字之和

对于算法初学者来说，这道题目有助于理解：
- 回溯算法的基本思想
- 如何处理组合问题
- 如何使用递归解决复杂问题

