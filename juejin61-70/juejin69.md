# 前K个高频元素

## 题目描述

给你一个整数数组 nums 和一个整数 k，请你返回其中出现频率前 k 高的元素。返回结果需要按升序排列并以字符串形式输出。

要求算法的时间复杂度必须优于 O(n log n)，其中 n 是数组的大小。

### 输入输出格式

- 输入：
  - nums: 一个正整数数组
  - k: 一个整数
- 输出：
  - 返回一个字符串，包含k个按升序排列的数字，数字之间用逗号分隔

### 参数限制

- 1 <= nums[i] <= 10^4
- 1 <= nums.length <= 10^5
- k的取值范围是[1, 数组中不相同元素的个数]
- 题目数据保证答案唯一

### 示例

**示例 1:**
```python
输入：nums = [1,1,1,2,2,3], k = 2
输出："1,2"
解释：元素1出现3次，元素2出现2次，元素3出现1次，所以前两个高频元素是1和2。
```

**示例 2:**
```python
输入：nums = [1], k = 1
输出："1"
```

**示例 3:**
```python
输入：nums = [4,4,4,2,2,2,3,3,1], k = 2
输出："2,4"
```

## 解题思路

这道题目要求我们找出数组中出现频率最高的k个元素，并且时间复杂度要优于O(n log n)。我们可以使用桶排序的思想来解决这个问题。

### 解题步骤

1. **频率统计**
   - 使用哈希表（字典）统计每个数字出现的频率
   - 时间复杂度：O(n)

2. **桶排序**
   - 创建一个桶数组，数组的索引表示频率
   - 将具有相同频率的数字放入对应的桶中
   - 时间复杂度：O(n)

3. **收集结果**
   - 从后向前遍历桶数组（即从高频率到低频率）
   - 对每个非空桶中的数字进行排序
   - 收集前k个高频元素
   - 时间复杂度：O(n)

4. **格式化输出**
   - 对最终结果进行排序
   - 将结果转换为要求的字符串格式
   - 时间复杂度：O(k log k)，其中k较小

### 代码实现

```python
def solution(nums, k):
    # 使用哈希表统计每个数字出现的频率
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # 创建桶，桶的索引表示频率，值为具有该频率的数字列表
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # 从后向前遍历桶，收集前k个高频元素
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i]:
            # 对同一频率的数字进行排序
            buckets[i].sort()
            result.extend(buckets[i])
            if len(result) >= k:
                result = result[:k]
                break
    
    # 对结果进行排序并转换为字符串
    result.sort()
    return ','.join(map(str, result))
```

### 复杂度分析

- **时间复杂度**: O(n)
  - 频率统计：O(n)
  - 创建桶和放入元素：O(n)
  - 收集结果：O(n)
  - 最终排序：O(k log k)，其中k较小
  - 总体时间复杂度为O(n)，满足题目要求

- **空间复杂度**: O(n)
  - 哈希表存储：O(n)
  - 桶数组存储：O(n)

### 注意事项

1. 在处理相同频率的元素时，需要对它们进行排序以确保结果的唯一性
2. 最终返回结果前需要再次排序，以满足升序输出的要求
3. 返回结果需要转换为特定的字符串格式，使用逗号分隔

### 总结

这道题的关键在于使用桶排序的思想来避免传统排序算法的O(n log n)时间复杂度。通过哈希表统计频率，再使用桶排序的思想，我们可以在O(n)的时间复杂度内解决这个问题。这是一个典型的用空间换时间的例子，值得学习和掌握。

