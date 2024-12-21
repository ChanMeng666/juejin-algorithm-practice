# 超市商品排列优化问题

## 题目描述

在一个超市里，有一个包含 n 个格子的货物架，每个格子中放有一种商品，商品用小写字母 a 到 z 表示。当顾客进入超市时，他们会依次从第一个格子查找到第 n 个格子，寻找自己想要购买的商品。

购物规则：
1. 如果在某个格子中找到该商品，顾客就会购买它并离开
2. 如果中途遇到一个空格子，顾客会离开
3. 如果查找完所有格子还没有找到想要的商品，顾客也会离开

作为超市管理员，你可以在顾客到来之前重新调整商品的顺序，以便尽可能多地出售商品。注意：当第一个顾客进入后，商品位置不能再调整。

### 输入参数
- n：货物架的格子数
- m：顾客想要购买的商品种类数
- s：货物架上商品的初始顺序
- c：顾客想要购买的商品种类

### 示例

**示例 1:**
```python
输入：n = 3, m = 4, s = "abc", c = "abcd"
输出：3
解释：可以按"abc"排列，这样前三个顾客都能买到商品，第四个顾客找不到'd'
```

**示例 2:**
```python
输入：n = 4, m = 2, s = "abbc", c = "bb"
输出：2
解释：可以将商品排列为"bbac"，这样两个要买'b'的顾客都能买到
```

**示例 3:**
```python
输入：n = 5, m = 4, s = "bcdea", c = "abcd"
输出：4
解释：可以将商品排列为"abcde"，这样前四个顾客都能买到商品
```

## 解题思路

1. **问题分析**
   - 这是一个优化问题，我们需要找到一个最优的商品排列顺序
   - 关键是要理解顾客的购买行为：从左到右查找，找到就买走并离开
   - 一旦商品被买走，该位置就变成空位，可能影响后续顾客

2. **解决方案**
   - 统计每个商品的需求量
   - 将商品按需求量降序排列（需求量相同时按字母顺序）
   - 模拟顾客购买过程，记录已售出的位置

3. **优化策略**
   - 需求量大的商品应该放在前面
   - 相同需求量的商品按字母顺序排列，便于查找
   - 使用集合记录已售出的位置，避免重复销售

## 代码实现

```python
def solution(n: int, m: int, s: str, c: str) -> int:
    # 将商品列表转换为列表以便操作
    items = list(s)
    
    # 统计每个顾客想要购买的商品数量
    customer_wants = {}
    for char in c:
        customer_wants[char] = customer_wants.get(char, 0) + 1
    
    # 统计货架上每种商品的数量
    shelf_items = {}
    for char in s:
        shelf_items[char] = shelf_items.get(char, 0) + 1
    
    # 根据顾客需求对商品进行排序
    # 优先放置更多顾客想要的商品
    items.sort(key=lambda x: (-customer_wants.get(x, 0), x))
    
    # 模拟顾客购买过程
    sold = 0
    used_positions = set()
    
    for customer_item in c:
        found = False
        # 遍历所有位置
        for pos in range(n):
            if pos in used_positions:
                continue
            if items[pos] == customer_item:
                sold += 1
                used_positions.add(pos)
                found = True
                break
            # 如果遇到空格子，顾客离开
            if items[pos] == ' ':
                break
        # 如果没找到想要的商品，继续下一个顾客
        if not found:
            continue
            
    return sold
```

## 代码详解

1. **数据预处理**
   ```python
   items = list(s)
   customer_wants = {}
   for char in c:
       customer_wants[char] = customer_wants.get(char, 0) + 1
   ```
   - 将输入字符串转换为列表，方便修改
   - 统计每种商品的需求量

2. **商品排序**
   ```python
   items.sort(key=lambda x: (-customer_wants.get(x, 0), x))
   ```
   - 使用自定义排序规则
   - `-customer_wants.get(x, 0)`确保需求量大的在前面
   - 第二个排序键`x`确保相同需求量时按字母顺序排列

3. **模拟购买过程**
   ```python
   sold = 0
   used_positions = set()
   
   for customer_item in c:
       found = False
       for pos in range(n):
           if pos in used_positions:
               continue
           if items[pos] == customer_item:
               sold += 1
               used_positions.add(pos)
               found = True
               break
   ```
   - 遍历每个顾客的需求
   - 检查每个位置是否有所需商品
   - 记录已售出的位置
   - 统计总销售量

## 复杂度分析

- 时间复杂度：O(n * m)，其中n是货架格子数，m是顾客数量
- 空间复杂度：O(n)，主要用于存储商品列表和已售出位置集合

## 总结

这道题目考察了贪心算法的思想，通过合理安排商品位置来最大化销售量。关键点在于：
1. 识别出需求量大的商品应该放在前面
2. 正确处理已售出商品的位置
3. 模拟顾客的购买行为

对于算法初学者来说，这道题目是一个很好的练习，它结合了实际场景，帮助理解如何将现实问题转化为算法问题。
