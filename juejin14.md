# 构造最小和数组问题

## 题目描述
小C希望构造一个包含n个元素的数组，需要满足以下条件：
1. 数组中的所有元素两两不同
2. 数组所有元素的最大公约数为k
3. 数组元素之和要尽可能小

要求输出满足条件的数组元素之和的最小值。

## 示例
### 示例1
输入：
```python
n = 3, k = 1
```
输出：
```python
6
```
解释：可以构造数组[1,2,3]，元素之和为6

### 示例2
输入：
```python
n = 2, k = 2
```
输出：
```python
6
```
解释：可以构造数组[2,4]，元素之和为6

### 示例3
输入：
```python
n = 4, k = 3
```
输出：
```python
30
```
解释：可以构造数组[3,6,9,12]，元素之和为30

## 解题思路
1. 理解题目要求：
   - 需要找到n个不同的数
   - 这些数的最大公约数必须是k
   - 这些数的和要尽可能小

2. 关键观察：
   - 要使最大公约数为k，所有数必须是k的倍数
   - 为了使和最小，应该选择最小的k的倍数
   - 从k开始，依次选择k的倍数即可

3. 算法步骤：
   - 初始化一个空数组result
   - 从k开始，每次加入一个k的倍数
   - 直到数组长度达到n
   - 返回数组元素之和

## 代码实现
```python
def solution(n: int, k: int) -> int:
    # 创建一个数组存储选中的数
    result = []
    # 从k开始，找到n个k的倍数
    current = k
    while len(result) < n:
        result.append(current)
        current += k
    
    # 返回数组元素之和
    return sum(result)
```

## 代码解释
1. `result = []`：创建一个空数组来存储选择的数

2. `current = k`：从k开始，因为k是最小的可能值

3. `while len(result) < n:`：循环直到找到n个数
   - `result.append(current)`：将当前数加入数组
   - `current += k`：移动到下一个k的倍数

4. `return sum(result)`：返回数组所有元素的和

## 复杂度分析
- 时间复杂度：O(n)，需要找到n个数
- 空间复杂度：O(n)，需要存储n个数的数组

## 举例说明
以n=4，k=3为例：
1. 初始current=3，result=[3]
2. current=6，result=[3,6]
3. current=9，result=[3,6,9]
4. current=12，result=[3,6,9,12]
5. 返回3+6+9+12=30

## 易错点
1. 不要试图寻找非k的倍数，因为这样无法保证最大公约数为k
2. 不要跳过k的倍数，因为这样会导致和不是最小的
3. 不要忘记数组元素必须互不相同的条件

## 相关题目
- 最大公约数相关问题
- 构造性算法问题
- 数组最小和问题
