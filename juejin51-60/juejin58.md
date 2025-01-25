# Base32 编码解码实现

## 题目描述

实现一个 Base32 的编码和解码函数。该函数需要完成:
1. 对输入字符串进行 Base32 编码
2. 对 Base32 编码的字符串进行解码

### Base32 编码原理

Base32 是一种将二进制数据编码为可打印字符的编码方式,类似于更常见的 Base64。主要特点:

- 以 5 bit 为一组进行编码(而 Base64 是 6 bit 一组)
- 使用 32 个可打印字符表示编码结果(Base64 使用 64 个字符)
- 需要在末尾添加特定数量的 + 作为填充符

### 编码步骤

1. 字符串转二进制
   - 将输入字符串中每个字符转为 8 位二进制
   - 所有字符的二进制连接在一起

2. 5 位分组
   - 将二进制串按每 5 位一组进行分组
   - 如果最后一组不足 5 位,补充 0 直到凑够 5 位

3. 查表转换
   - 将每组 5 位二进制转为十进制数(0-31)
   - 根据映射表将数字转为对应字符

4. 添加填充
   - 根据原始字符串长度(位数)确定需要添加的 + 号数量
   - 位数除以 40 的余数决定填充数量:
     - 余数为 8: 补 6 个 +
     - 余数为 16: 补 4 个 + 
     - 余数为 24: 补 3 个 +
     - 余数为 32: 补 1 个 +
     - 余数为 0: 不补 +

### 解码步骤

1. 预处理
   - 移除末尾的 + 填充符
   - 将编码字符串按 +++ 分割(处理多段编码的情况)

2. 字符转二进制
   - 查表获取每个字符对应的索引值(0-31)
   - 将索引值转为 5 位二进制

3. 二进制转字符串
   - 将二进制串按 8 位一组转回字符
   - 处理末尾可能的填充位
   - 跳过空字符(\x00)

## 代码实现

### 核心数据结构

使用字符映射表存储 Base32 编码字符集:
```python
char_map = "9876543210mnbvcxzasdfghjklpoiuyt"
```

### 主要函数

1. str_to_bits: 字符串转二进制
```python
def str_to_bits(s):
    return ''.join(format(ord(c), '08b') for c in s)
```

2. bits_to_str: 二进制转字符串
```python
def bits_to_str(bits):
    if len(bits) % 8 != 0:
        bits = bits[:-(len(bits) % 8)]
    result = ""
    for i in range(0, len(bits), 8):
        if i + 8 <= len(bits):
            char = chr(int(bits[i:i+8], 2))
            if char != '\x00':
                result += char
    return result
```

3. encode: Base32 编码实现
```python
def encode(s):
    if not s:
        return ""
    bits = str_to_bits(s)
    padding = (5 - len(bits) % 5) % 5
    bits += '0' * padding
    
    result = ""
    for i in range(0, len(bits), 5):
        chunk = bits[i:i+5]
        idx = int(chunk, 2)
        result += char_map[idx]
    
    # 添加填充符号
    orig_bits_len = len(s) * 8
    if orig_bits_len % 40 == 8:
        result += "+" * 6
    elif orig_bits_len % 40 == 16:
        result += "+" * 4
    elif orig_bits_len % 40 == 24:
        result += "+" * 3
    elif orig_bits_len % 40 == 32:
        result += "+" * 1
        
    return result
```

4. decode: Base32 解码实现
```python
def decode(s):
    if not s:
        return ""
    s = s.rstrip('+')
    
    bits = ""
    for c in s:
        idx = char_map.index(c)
        bits += format(idx, '05b')
    
    return bits_to_str(bits)
```

## 注意事项

1. 编码时需要正确处理位数不足的情况,补充适当的 0
2. 解码时要正确处理填充符号
3. 需要跳过解码结果中的空字符
4. 处理多段编码时要正确拆分和合并结果

## 测试用例

```python
# 测试用例1
print(solution("foo", "b0zj5+++") == "bljhy+++:bar")

# 测试用例2
print(solution("The encoding process", "bljhy+++b0zj5+++") == 
      "maf3m164vlahyl60vlds9i6svuahmiod:foobar")

# 测试用例3
print(solution("Base32 encoding and decoding", "bvchz+++v4j21+++cals9+++") == 
      "10zj3l0d31z3mod6vus3sod258zhil89bash3oo5v4j3c+++:c]hintts ")
```

## 常见错误

1. 忘记处理位数不足的填充情况
2. 未正确处理多段编码的情况
3. 未跳过解码结果中的空字符
4. 填充符号数量计算错误

通过理解上述实现过程和注意事项,可以更好地掌握 Base32 编码解码的原理和实现细节。

