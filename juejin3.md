# 数字千分位格式化问题

## 题目描述
给定一个表示数字的字符串，要求将其转换为带有千分位逗号的格式，同时需要处理以下特殊情况：
1. 保留小数部分（如果有）
2. 去除整数部分前面的无用的0

## 示例
```python
输入：s = "1294512.12412"
输出：'1,294,512.12412'

输入：s = "0000123456789.99"
输出：'123,456,789.99'

输入：s = "987654321"
输出：'987,654,321'
```

## 解题思路
1. 首先需要将数字分成整数部分和小数部分
2. 处理整数部分：
   - 去除前导零
   - 每三位添加一个逗号
3. 如果有小数部分，需要将其保持不变并添加回结果中

## 代码实现
```python
def solution(s: str) -> str:
    # 分割整数部分和小数部分
    parts = s.split('.')
    
    # 处理整数部分：去除前导零并添加千分位逗号
    integer_part = parts[0].lstrip('0')
    if not integer_part:  # 如果整数部分为空（即原数为0开头）
        integer_part = '0'
        
    # 从右向左每三位添加逗号
    formatted_int = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and i % 3 == 0:
            formatted_int = ',' + formatted_int
        formatted_int = digit + formatted_int
    
    # 如果有小数部分，则添加回去
    if len(parts) > 1:
        return formatted_int + '.' + parts[1]
    
    return formatted_int
```

## 代码详解

### 1. 分割整数和小数
```python
parts = s.split('.')
```
使用`split('.')`方法将字符串按小数点分割成两部分：
- 如果有小数点，parts将包含两个元素：整数部分和小数部分
- 如果没有小数点，parts将只包含一个元素：整数部分

### 2. 处理前导零
```python
integer_part = parts[0].lstrip('0')
if not integer_part:  # 如果整数部分为空（即原数为0开头）
    integer_part = '0'
```
- `lstrip('0')`方法去除字符串左边的所有0
- 如果去除后为空字符串（说明原数字是0），则将整数部分设为'0'

### 3. 添加千分位逗号
```python
formatted_int = ''
for i, digit in enumerate(integer_part[::-1]):
    if i > 0 and i % 3 == 0:
        formatted_int = ',' + formatted_int
    formatted_int = digit + formatted_int
```
- `integer_part[::-1]`将字符串反转，从右向左处理
- 使用`enumerate()`获取每个数字的索引和值
- 每当索引是3的倍数（且不是第一位）时，添加逗号
- 使用字符串拼接构建最终结果

### 4. 处理小数部分
```python
if len(parts) > 1:
    return formatted_int + '.' + parts[1]
return formatted_int
```
- 检查是否有小数部分（parts长度大于1）
- 如果有，将小数点和小数部分添加到结果中
- 如果没有，直接返回处理好的整数部分

## 复杂度分析
- 时间复杂度：O(n)，其中n是输入字符串的长度
- 空间复杂度：O(n)，需要存储处理后的字符串

## 相关题目
- 数字格式化
- 字符串处理
- 千分位分隔符

## 总结
这道题目主要考察了字符串的基本操作：
1. 字符串分割
2. 字符串遍历和拼接
3. 特殊情况的处理（前导零、小数部分）

解题关键是要理清处理步骤，分别处理整数部分和小数部分，并注意细节处理。
