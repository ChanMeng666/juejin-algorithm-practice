# 多米诺骨牌问题

## 题目描述

小S玩起了多米诺骨牌，他排列了一行骨牌，并可能将某些骨牌向左或向右推倒。随着骨牌连锁反应的进行，一些骨牌可能因为左右两侧受力平衡而保持竖立。现在小S想要知道在所有动作完成后，哪些骨牌保持竖立。

### 输入格式
- 第一个参数 num：表示骨牌的总数量
- 第二个参数 data：一个字符串，表示骨牌的初始状态
  - 'L'：表示该位置的骨牌将向左倒
  - 'R'：表示该位置的骨牌将向右倒
  - '.'：表示该位置的骨牌初始时保持竖立

### 输出格式
- 如果没有骨牌保持竖立，返回字符串"0"
- 如果有骨牌保持竖立，返回格式为"数量:位置1,位置2,..."的字符串，位置从1开始计数

### 示例
```python
输入：num = 14, data = ".L.R...LR..L.."
输出："4:3,6,13,14"

输入：num = 5, data = "R...."
输出："0"

输入：num = 1, data = "."
输出："1:1"
```

## 解题思路

### 1. 问题分析
这是一个模拟物理过程的问题，关键在于理解骨牌的受力情况：
1. 一个骨牌会受到左右两侧的力的影响
2. 如果左右力相等，骨牌会保持竖立
3. 力的传递会随着距离减弱

### 2. 解决方案
我们可以使用"力的传递"的方式来解决这个问题：

1. 使用一个forces数组记录每个位置的受力情况
2. 分两次扫描处理受力：
   - 从左向右扫描：处理向右的力（R的影响）
   - 从右向左扫描：处理向左的力（L的影响）
3. 最后检查forces数组，找出受力平衡的位置

### 3. 具体实现步骤

1. **初始化**
   ```python
   dominoes = list(data)  # 将输入字符串转换为列表
   forces = [0] * len(dominoes)  # 初始化力的数组
   ```

2. **从左向右处理R的影响**
   - 遇到'R'时，设置最大力
   - 遇到'L'时，力归零
   - 对于'.'，力逐渐减小
   ```python
   force = 0
   for i in range(n):
       if dominoes[i] == 'R': force = n
       elif dominoes[i] == 'L': force = 0
       else: force = max(force - 1, 0)
       forces[i] += force
   ```

3. **从右向左处理L的影响**
   - 遇到'L'时，设置最大力
   - 遇到'R'时，力归零
   - 对于'.'，力逐渐减小
   ```python
   force = 0
   for i in range(n-1, -1, -1):
       if dominoes[i] == 'L': force = n
       elif dominoes[i] == 'R': force = 0
       else: force = max(force - 1, 0)
       forces[i] -= force
   ```

4. **找出保持竖直的骨牌**
   - 遍历forces数组
   - 如果某位置force为0且原始状态为'.'，则该骨牌保持竖直
   ```python
   standing = []
   for i in range(n):
       if forces[i] == 0 and dominoes[i] == '.':
           standing.append(i + 1)  # 转换为1-based索引
   ```

### 4. 复杂度分析
- 时间复杂度：O(n)，需要对数组进行两次遍历
- 空间复杂度：O(n)，需要存储forces数组

## 注意事项
1. 位置索引需要从1开始计数
2. 输出格式需要严格按照要求
3. 特殊情况的处理（如没有竖立的骨牌时返回"0"）

## 总结
这道题目是一个很好的物理模拟题，关键在于：
1. 理解力的传递规律
2. 分别处理左右两个方向的力
3. 通过受力平衡来判断骨牌的最终状态

通过这种方式，我们可以准确模拟出骨牌倒下的过程，找出最终保持竖直的骨牌位置。

