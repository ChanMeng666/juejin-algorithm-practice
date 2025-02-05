# SQL编辑器自动补全功能实现

## 题目描述

在开发SQL编辑器时，需要实现一个自动补全功能，根据用户输入的字符片段，从已知的SQL关键字和数据库相关名称中找到所有以该片段开头的候选词，并按字典序输出。

### 输入格式
- num: 整数，表示数据列表的长度
- data: 字符串数组，包含SQL关键字和数据库相关名称
- input: 字符串，用户输入的前缀

### 输出要求
- 如果找到匹配项，将所有匹配的字符串按字典序排序并用逗号连接返回
- 如果没有找到匹配项，返回"-1"

### 示例
```python
输入：
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "f"
输出："from,from_mobile"

输入：
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "wh"
输出："where"

输入：
num = 8
data = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]
input = "z"
输出："-1"
```

## 解题思路

1. **问题分析**
   - 这是一个字符串前缀匹配问题
   - 需要考虑特殊情况的处理（无匹配、单个匹配、多个匹配）
   - 需要按字典序排序输出结果

2. **关键点**
   - 使用`startswith()`方法进行前缀匹配
   - 需要特别处理完全匹配的情况
   - 结果需要按字典序排序
   - 多个结果用逗号连接，不能有空格

3. **实现步骤**
   1. 创建空列表存储匹配结果
   2. 遍历数据列表，查找所有以input开头的字符串
   3. 分开处理完全匹配和前缀匹配的情况
   4. 对匹配结果进行排序
   5. 返回最终结果

## 代码实现

```python
def solution(num, data, input):
    # 存储所有匹配的结果
    matches = []
    
    # 遍历数据列表，查找所有以input开头的字符串
    for item in data:
        if item.startswith(input) and item != input:  # 排除完全相等的情况
            matches.append(item)
    
    # 单独处理完全匹配的情况
    if input in data:
        matches.append(input)
    
    # 如果没有找到匹配项，返回"-1"
    if not matches:
        return "-1"
    
    # 对匹配结果按字典序排序
    matches.sort()
    
    # 将结果用逗号连接成字符串
    return ",".join(matches)
```

## 代码详解

1. **匹配收集**
   - 使用`startswith()`方法检查字符串是否以输入前缀开头
   - 使用条件`item != input`排除完全相等的情况，这样可以控制完全匹配项在结果中的位置

2. **完全匹配处理**
   - 单独检查输入字符串是否在数据列表中
   - 如果存在，将其添加到匹配列表中

3. **结果处理**
   - 使用`sort()`方法对匹配结果进行字典序排序
   - 使用`join()`方法将结果用逗号连接
   - 如果没有匹配项，返回"-1"

## 注意事项

1. 需要特别注意完全匹配的情况处理
2. 返回结果中不能包含多余的空格
3. 字典序排序是必须的
4. 当没有匹配项时必须返回"-1"而不是空字符串

## 测试用例

```python
testData1 = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]

# 测试多个匹配的情况
print(solution(8, testData1, "f") == "from,from_mobile")

# 测试单个匹配的情况
print(solution(8, testData1, "wh") == "where")

# 测试无匹配的情况
print(solution(8, testData1, "z") == "-1")
```

这个问题是SQL编辑器开发中的一个实际应用场景，通过实现这个功能，可以提高用户的输入效率和使用体验。解决这个问题需要注意字符串处理、排序和特殊情况的处理，是一个很好的编程练习题。

