# 最少字符串操作次数

## 题目描述

小U得到一个只包含小写字母的字符串 S。她可以执行如下操作：每次选择字符串中两个相同的字符删除，然后在字符串末尾添加一个任意的小写字母。小U想知道，最少需要多少次操作才能使得字符串中的所有字母都不相同？

## 示例

### 示例 1：
- 输入：S = "abab"
- 输出：2
- 解释：
  1. 第一次操作：删除两个'a'，添加一个新字符，比如'c'，得到"bbc"
  2. 第二次操作：删除两个'b'，添加一个新字符，比如'd'，得到"cd"
  3. 此时所有字符都不相同，操作结束

### 示例 2：
- 输入：S = "aaaa"
- 输出：2
- 解释：
  1. 第一次操作：删除两个'a'，添加一个新字符，比如'b'，得到"aab"
  2. 第二次操作：删除两个'a'，添加一个新字符，比如'c'，得到"bc"
  3. 此时所有字符都不相同，操作结束

### 示例 3：
- 输入：S = "abcabc"
- 输出：3
- 解释：需要对每对重复的字符('a'、'b'、'c')各进行一次操作

## 解题思路

1. **问题分析**
   - 每次操作可以删除两个相同的字符
   - 然后可以添加任意一个新的字符
   - 目标是使最终字符串中所有字符都不相同
   - 需要找出最少的操作次数

2. **关键点**
   - 对于每个重复出现的字符，我们需要通过操作减少其出现次数
   - 每次操作可以处理两个相同字符
   - 不需要关心添加什么新字符，因为我们可以选择添加一个当前不存在的字符

3. **解决方案**
   - 首先统计每个字符出现的次数
   - 对于每个字符，如果出现次数大于1，需要进行操作
   - 每两个相同字符需要一次操作
   - 因此对于出现n次的字符，需要 n/2（向下取整）次操作

## 代码实现

```python
def solution(S: str) -> int:
    # 统计每个字符的出现次数
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1
    
    operations = 0
    # 对于每个出现次数大于1的字符
    for count in char_count.values():
        # 每次操作删除2个字符，所以需要 count//2 次操作
        operations += count // 2
            
    return operations
```

## 复杂度分析

- 时间复杂度：O(n)，其中 n 是字符串的长度
  - 需要遍历一次字符串统计字符频率
  - 需要遍历一次字符频率字典

- 空间复杂度：O(k)，其中 k 是字符集大小
  - 需要一个哈希表存储字符频率
  - 因为只包含小写字母，所以 k ≤ 26

## 总结

这道题的关键是理解：
1. 不需要真正模拟字符串的变化过程
2. 只需要计算每个重复字符需要的操作次数
3. 最终的操作次数就是所有重复字符需要的操作次数之和
4. 对于每个字符，每两个出现需要一次操作

通过这种方式，我们可以直接计算出最少需要的操作次数，而不需要实际执行字符串的修改操作。
