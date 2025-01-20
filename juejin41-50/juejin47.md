# 完美偶数统计问题

## 题目描述

小C定义了一个"完美偶数"。一个正整数 x 被认为是完美偶数需要满足以下两个条件：

1. x 是偶数
2. x 的值在区间 [l, r] 之间

现在，小C有一个长度为 n 的数组 a，她想知道在这个数组中有多少个完美偶数。

## 输入格式

- 第一行包含四个整数：n（数组长度）、l（区间左端点）、r（区间右端点）、数组a
- 其中 1 ≤ n ≤ 100000，1 ≤ l ≤ r ≤ 1000000
- 数组a中的每个元素满足：1 ≤ a[i] ≤ 1000000

## 输出格式

输出一个整数，表示数组a中完美偶数的个数。

## 示例

### 示例1：
输入：
```
n = 5, l = 3, r = 8, a = [1, 2, 6, 8, 7]
```
输出：
```
2
```
解释：数组中的数字6和8是完美偶数，因为它们都是偶数且在区间[3,8]内。

### 示例2：
输入：
```
n = 4, l = 10, r = 20, a = [12, 15, 18, 9]
```
输出：
```
2
```
解释：数组中的数字12和18是完美偶数，因为它们都是偶数且在区间[10,20]内。

### 示例3：
输入：
```
n = 3, l = 1, r = 10, a = [2, 4, 6]
```
输出：
```
3
```
解释：数组中的所有数字2、4、6都是完美偶数，因为它们都是偶数且在区间[1,10]内。

## 解题思路

1. **问题分析**
   - 我们需要统计数组中满足两个条件的数字个数
   - 条件1：是偶数
   - 条件2：在给定区间[l,r]内

2. **解决方案**
   - 使用一个计数器（count）记录满足条件的数字个数
   - 遍历数组中的每个数字，对每个数字进行两个条件的判断：
     - 使用取模运算（num % 2 == 0）判断是否为偶数
     - 使用范围判断（l <= num <= r）确认是否在区间内
   - 如果同时满足这两个条件，计数器加1
   - 最后返回计数器的值

3. **代码实现**
```python
def solution(n: int, l: int, r: int, a: list) -> int:
    count = 0
    
    for num in a:
        if num % 2 == 0 and l <= num <= r:
            count += 1
            
    return count
```

## 复杂度分析

- 时间复杂度：O(n)，其中n是数组的长度。我们只需要遍历一次数组。
- 空间复杂度：O(1)，只使用了一个计数器变量。

## 注意事项

1. 判断偶数时，使用取模运算（num % 2 == 0）是最简单直接的方法
2. 区间判断要使用双向的边界检查（l <= num <= r）
3. 不需要考虑数组长度n是否等于实际输入数组的长度，因为实际操作时是遍历输入数组

## 相关知识点

1. 偶数的判断方法
2. 区间范围的判断
3. Python中的列表遍历
4. 计数器的使用方法
