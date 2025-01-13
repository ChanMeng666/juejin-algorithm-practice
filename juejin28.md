# 竞技场逃生问题

## 题目描述

在一个 N × M 的竞技场迷宫中，你需要找出所有的"危险位置"数量。所谓"危险位置"，就是指如果站在该位置上，无论采取什么移动策略，都无法到达出口的位置。

### 地图元素说明
- `.`：普通地板，可以向上下左右四个方向移动
- `O`：出口位置
- `U`：向上传送器，踩上去会被强制传送到上方的格子
- `D`：向下传送器，踩上去会被强制传送到下方的格子
- `L`：向左传送器，踩上去会被强制传送到左方的格子
- `R`：向右传送器，踩上去会被强制传送到右方的格子

注意：如果被传送到竞技场外，则视为死亡。

### 输入格式
- `N`：竞技场地图的行数
- `M`：竞技场地图的列数
- `data`：N × M 的字符二维数组，表示竞技场地图

### 限制条件
- 1 ≤ N, M ≤ 100

## 解题思路

这是一个典型的图论问题，我们可以通过以下步骤来解决：

### 1. 反向思维
不直接寻找危险位置，而是找出所有可以到达出口的安全位置，剩下的就是危险位置。

### 2. 使用BFS（广度优先搜索）
从出口位置开始，反向寻找所有可以到达出口的位置。

### 3. 具体实现步骤

1. **找到出口位置**
   - 遍历地图找到 'O' 的位置

2. **定义辅助函数**
   - `is_valid(x, y)`：判断位置是否在地图范围内
   - `get_prev_positions(x, y)`：获取所有可以到达当前位置的前置位置

3. **处理不同类型的格子**
   - 普通地板(.)：可以从上下左右四个方向到达
   - 传送器(U/D/L/R)：只能从特定方向到达
   - 需要考虑传送器的方向和地图边界

4. **使用BFS遍历**
   - 从出口开始，使用队列存储待处理的位置
   - 使用集合记录已找到的安全位置
   - 不断寻找可以到达当前位置的前置位置

5. **计算结果**
   - 危险位置数量 = 总格子数 - 安全位置数量

## 代码实现

```python
def solution(N, M, data):
    # 找到出口位置
    exit_pos = None
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'O':
                exit_pos = (i, j)
                break
        if exit_pos:
            break
    
    # 判断位置是否有效
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M
    
    # 获取可以到达当前位置的所有前置位置
    def get_prev_positions(x, y):
        positions = []
        for px, py in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not is_valid(px, py):
                continue
            curr = data[px][py]
            # 检查传送器方向
            if curr == 'U' and x == px-1:
                positions.append((px, py))
            elif curr == 'D' and x == px+1:
                positions.append((px, py))
            elif curr == 'L' and y == py-1:
                positions.append((px, py))
            elif curr == 'R' and y == py+1:
                positions.append((px, py))
            elif curr in '.O':
                positions.append((px, py))
        return positions
    
    # BFS寻找安全位置
    safe_positions = set([exit_pos])
    queue = [exit_pos]
    
    while queue:
        curr_x, curr_y = queue.pop(0)
        for px, py in get_prev_positions(curr_x, curr_y):
            if (px, py) not in safe_positions:
                safe_positions.add((px, py))
                queue.append((px, py))
    
    return N * M - len(safe_positions)
```

## 示例及解释

### 示例1
```python
pattern = [
    [".", ".", ".", ".", "."],
    [".", "R", "R", "D", "."],
    [".", "U", ".", "D", "R"],
    [".", "U", "L", "L", "."],
    [".", ".", ".", ".", "O"]
]
输出：10
```
解释：有10个位置无法到达出口，标记为X的位置都是危险位置：
```
['.', '.', '.', '.', '.']
['.', 'X', 'X', 'X', '.']
['.', 'X', 'X', 'X', 'X']
['.', 'X', 'X', 'X', '.']
['.', '.', '.', '.', 'O']
```

### 示例2
```python
pattern = [[".", "R", ".", "O"], 
           ["U", ".", "L", "."], 
           [".", "D", ".", "."], 
           [".", ".", "R", "D"]]
输出：2
```

### 示例3
```python
pattern = [[".", "U", "O"],
           ["L", ".", "R"],
           ["D", ".", "."]]
输出：8
```

## 复杂度分析

- 时间复杂度：O(N×M)，其中N和M是地图的行数和列数
- 空间复杂度：O(N×M)，主要用于存储安全位置集合和BFS队列

## 注意事项

1. 处理传送器时要特别注意方向
2. 需要考虑传送到地图外的情况
3. BFS遍历时要避免重复访问相同位置
4. 边界条件的处理很重要
