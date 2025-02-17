# 寻找数组中出现次数超过一半的数字

## 题目描述
小R从班级中抽取了一些同学，每位同学都会给出一个数字。已知在这些数字中，某个数字的出现次数超过了数字总数的一半。现在需要你帮助小R找到这个数字。

## 示例
### 示例 1
输入：`array = [1, 3, 8, 2, 3, 1, 3, 3, 3]`
输出：`3`
解释：数字3出现了5次，超过数组长度9的一半。

### 示例 2
输入：`array = [5, 5, 5, 1, 2, 5, 5]`
输出：`5`
解释：数字5出现了5次，超过数组长度7的一半。

### 示例 3
输入：`array = [9, 9, 9, 9, 8, 9, 8, 8]`
输出：`9`
解释：数字9出现了5次，超过数组长度8的一半。

## 解题思路
这道题可以使用"摩尔投票算法"来解决。这是一个用于找出数组中出现次数超过一半的元素的经典算法。

算法的核心思想是：
1. 如果一个数字出现次数超过一半，那么这个数字与其他所有数字两两抵消后，最后剩下的一定是这个数字。
2. 我们可以维护一个候选数字和一个计数器：
   - 当计数器为0时，选择当前数字作为新的候选数字
   - 当遇到相同的数字时，计数器加1
   - 当遇到不同的数字时，计数器减1

### 算法步骤
1. 初始化：
   - 选择第一个数字作为候选数字
   - 设置计数器为1

2. 第一次遍历：
   - 遍历数组其余元素
   - 根据当前数字是否等于候选数字来更新计数器
   - 当计数器为0时更换候选数字

3. 第二次遍历：
   - 统计候选数字在数组中的实际出现次数
   - 验证是否超过数组长度的一半

## 代码实现
```python
def solution(array):
    # 使用摩尔投票算法
    candidate = array[0]  # 候选数字
    count = 1  # 计数器
    
    # 第一遍遍历：找出可能的众数
    for num in array[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # 第二遍遍历：验证这个数字是否确实出现超过一半
    count = sum(1 for num in array if num == candidate)
    if count > len(array) // 2:
        return candidate
    
    return 0  # 如果没有符合条件的数字（虽然根据题目描述这种情况不会发生）
```

## 复杂度分析
- 时间复杂度：O(n)，需要遍历数组两次
- 空间复杂度：O(1)，只使用了常数个变量

## 代码详解
1. `candidate = array[0]`：选择第一个数字作为初始候选数字
2. `count = 1`：初始化计数器为1
3. 第一次遍历：
   - `if count == 0`：当计数器为0时，说明之前的候选数字已经被抵消完，选择当前数字作为新的候选数字
   - `elif num == candidate`：遇到相同的数字，计数器加1
   - `else`：遇到不同的数字，计数器减1
4. 第二次遍历：
   - 使用列表推导式统计候选数字的实际出现次数
   - 验证是否超过数组长度的一半

## 易错点
1. 不要忘记第二次遍历验证候选数字的出现次数
2. 注意数组长度的一半应该使用整除运算 `//`
3. 初始化时应该从第一个元素开始，遍历时从第二个元素开始

## 相关题目
- 寻找数组中的众数
- 寻找数组中出现次数超过n/3的数字

## 总结
摩尔投票算法是一个非常巧妙的算法，它利用了"抵消"的思想，可以在O(n)时间内找到出现次数超过一半的元素。这个算法不仅高效，而且实现起来相对简单，是解决此类问题的最佳选择。
