# 字符串前缀转换问题

## 题目描述

小U和小R有两个字符串S和T。小U需要通过对S进行若干次操作，使其变成T的一个前缀。
允许的操作有两种：
1. 修改S的某一个字符
2. 删除S末尾的字符

要求计算出最少需要多少次操作才能让S变成T的前缀。

## 示例

### 示例 1:
```
输入：S = "aba", T = "abb"
输出：1
解释：只需要将最后一个'a'修改为'b'即可
```

### 示例 2:
```
输入：S = "abcd", T = "efg"
输出：4
解释：需要修改3个字符('a'->'e', 'b'->'f', 'c'->'g')，并删除'd'，共4次操作
```

### 示例 3:
```
输入：S = "xyz", T = "xy"
输出：1
解释：只需要删除最后一个字符'z'即可
```

### 示例 4:
```
输入：S = "hello", T = "helloworld"
输出：0
解释：S已经是T的前缀，无需操作
```

### 示例 5:
```
输入：S = "same", T = "same"
输出：0
解释：两个字符串相同，无需操作
```

## 解题思路

1. 首先需要判断特殊情况：如果S已经是T的前缀，则不需要任何操作，直接返回0。

2. 然后根据S和T的长度关系，分两种情况处理：

   - 当S比T长时：
     * 需要删除多余的字符（删除操作数 = S长度 - T长度）
     * 还需要修改不匹配的字符（在前T.length个字符中）
   
   - 当S长度小于或等于T时：
     * 只需要计算需要修改的字符数量
     * 通过比较对应位置的字符是否相同来统计

3. 最终返回所需的总操作次数。

## 代码实现

```python
def solution(S: str, T: str) -> int:
    # 如果S已经是T的前缀，直接返回0
    if T.startswith(S):
        return 0
    
    # 获取两个字符串的长度
    s_len = len(S)
    t_len = len(T)
    
    # 如果S比T长，需要删除多余的字符
    if s_len > t_len:
        # 先计算需要删除的字符数
        delete_count = s_len - t_len
        # 然后计算前t_len个字符中需要修改的字符数
        change_count = sum(1 for i in range(t_len) if S[i] != T[i])
        return delete_count + change_count
    
    # 如果S长度小于或等于T，只需要计算需要修改的字符数
    return sum(1 for i in range(s_len) if S[i] != T[i])
```

## 代码解释

1. `T.startswith(S)`：检查S是否已经是T的前缀
   - 如果是，直接返回0，因为不需要任何操作

2. 当S比T长时的处理：
   ```python
   if s_len > t_len:
       delete_count = s_len - t_len
       change_count = sum(1 for i in range(t_len) if S[i] != T[i])
       return delete_count + change_count
   ```
   - `delete_count`计算需要删除的字符数
   - `change_count`使用列表推导式计算需要修改的字符数
   - 返回两种操作的总和

3. 当S长度小于或等于T时的处理：
   ```python
   return sum(1 for i in range(s_len) if S[i] != T[i])
   ```
   - 只需要计算不匹配字符的数量
   - 使用列表推导式统计需要修改的字符数

## 复杂度分析

- 时间复杂度：O(min(len(S), len(T)))
  - 只需要遍历较短字符串的长度
  - startswith()函数的复杂度也是O(min(len(S), len(T)))

- 空间复杂度：O(1)
  - 只使用了几个变量来存储长度和计数
  - 没有使用额外的数据结构

## 总结

这道题目主要考察字符串操作和基本的编程逻辑。解题的关键是：
1. 正确理解"前缀"的概念
2. 分情况讨论（S长于T和S不长于T的情况）
3. 理清楚需要的操作类型（修改和删除）
4. 使用简洁的Python语法来实现计数

通过这道题，我们可以学习到：
- 字符串前缀判断的方法
- Python中的列表推导式使用
- 如何将复杂问题分解为简单的子问题

