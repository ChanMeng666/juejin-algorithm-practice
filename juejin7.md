# 广告标题通配符匹配问题

## 问题描述

在广告平台中，为了提高广告主创建标题的效率和灵活性，系统允许使用通配符方式提交创意。通配符用成对的花括号 `{}` 括起来，可以包含0个或多个字符。系统需要判断给定的标题是否能通过替换模板中的通配符而生成。

### 输入格式
- `n`：表示需要判断的标题数量
- `template`：包含通配符的模板字符串
- `titles`：需要判断的标题列表

### 输出格式
返回一个字符串，包含n个由逗号分隔的True或False，表示每个标题是否可以由模板生成。

### 示例

**示例1：**
```python
输入：
n = 4
template = "ad{xyz}cdc{y}f{x}e"
titles = ["adcdcefdfeffe", "adcdcefdfeff", "dcdcefdfeffe", "adcdcfe"]
输出："True,False,False,True"
```

**示例2：**
```python
输入：
n = 3
template = "a{bdc}efg"
titles = ["abcdefg", "abefg", "efg"]
输出："True,True,False"
```

## 解题思路

这是一个字符串匹配问题，可以使用动态规划来解决。主要步骤如下：

1. **模板解析**：
   - 将模板字符串解析为固定部分和通配符部分
   - 通配符可以匹配任意长度的字符串（包括空字符串）

2. **动态规划**：
   - 创建dp数组：`dp[i][j]` 表示模板的前i个部分是否能匹配标题的前j个字符
   - 对于固定字符串部分，需要精确匹配
   - 对于通配符部分，可以匹配任意长度的字符串

3. **结果处理**：
   - 对每个标题进行匹配判断
   - 将结果组合成要求的格式

## 代码实现

```python
def solution(n, template_, titles):
    def can_match(template, title):
        # 将模板按照 {} 分割
        parts = []
        i = 0
        fixed_parts = []
        while i < len(template):
            if template[i] == '{':
                start = i
                while i < len(template) and template[i] != '}':
                    i += 1
                if i < len(template):
                    parts.append(('wildcard', start))
                i += 1
            else:
                start = i
                while i < len(template) and template[i] != '{':
                    i += 1
                fixed_parts.append(template[start:i])
                parts.append(('fixed', len(fixed_parts) - 1))
        
        # 动态规划数组
        dp = [[False] * (len(title) + 1) for _ in range(len(parts) + 1)]
        dp[0][0] = True
        
        # 填充dp数组
        for i in range(1, len(parts) + 1):
            part_type, part_index = parts[i-1]
            
            if part_type == 'wildcard':
                # 通配符可以匹配任意字符
                for j in range(len(title) + 1):
                    if dp[i-1][j]:
                        for k in range(j, len(title) + 1):
                            dp[i][k] = True
            else:
                # 固定字符串必须精确匹配
                fixed_str = fixed_parts[part_index]
                for j in range(len(title)):
                    if dp[i-1][j]:
                        if j + len(fixed_str) <= len(title):
                            if title[j:j+len(fixed_str)] == fixed_str:
                                dp[i][j+len(fixed_str)] = True
        
        return dp[len(parts)][len(title)]

    # 处理每个标题
    results = []
    for title in titles:
        results.append(str(can_match(template_, title)))
    
    return ','.join(results)
```

## 代码详解

1. **模板解析部分**：
   ```python
   while i < len(template):
       if template[i] == '{':
           # 处理通配符部分
           parts.append(('wildcard', start))
       else:
           # 处理固定字符串部分
           fixed_parts.append(template[start:i])
           parts.append(('fixed', len(fixed_parts) - 1))
   ```
   - 将模板分解为固定字符串和通配符两种类型的部分
   - 使用元组 `(type, index)` 记录每个部分的类型和位置

2. **动态规划部分**：
   ```python
   dp = [[False] * (len(title) + 1) for _ in range(len(parts) + 1)]
   dp[0][0] = True
   ```
   - 创建dp数组，初始状态设置为True
   - dp[i][j]表示模板的前i个部分能否匹配标题的前j个字符

3. **匹配处理**：
   - 对于通配符：可以匹配任意长度的字符串
   - 对于固定字符串：必须精确匹配

## 复杂度分析

- 时间复杂度：O(n * m * k)
  - n: 模板长度
  - m: 标题长度
  - k: 通配符数量
- 空间复杂度：O(m * p)
  - m: 标题长度
  - p: 模板部分的数量

## 总结

这道题目是一个典型的字符串匹配问题，通过动态规划的方式来解决。关键点在于：
1. 正确解析模板字符串
2. 使用动态规划处理不同类型的匹配情况
3. 灵活处理通配符的匹配规则

对于算法初学者来说，这道题目可以帮助理解：
- 字符串处理技巧
- 动态规划的应用
- 如何将复杂问题分解为可管理的子问题
