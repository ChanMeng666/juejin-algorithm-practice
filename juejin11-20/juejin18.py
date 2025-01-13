def solution(m: int, n: int, a: list) -> int:
    # 定义方向：上下左右
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    max_steps = [0]  # 使用列表存储最大步数，方便在递归中修改
    
    def dfs(x: int, y: int, going_up: bool, steps: int):
        max_steps[0] = max(max_steps[0], steps)
        
        # 遍历四个方向
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # 检查新位置是否有效
            if (new_x < 0 or new_x >= m or 
                new_y < 0 or new_y >= n or 
                (new_x, new_y) in visited):
                continue
            
            # 检查高度差是否符合上坡/下坡要求
            if going_up and a[new_x][new_y] <= a[x][y]:
                continue
            if not going_up and a[new_x][new_y] >= a[x][y]:
                continue
            
            # 继续搜索
            visited.add((new_x, new_y))
            dfs(new_x, new_y, not going_up, steps + 1)
            visited.remove((new_x, new_y))
    
    # 从每个位置开始尝试
    for i in range(m):
        for j in range(n):
            visited.add((i, j))
            # 分别尝试从上坡和下坡开始
            dfs(i, j, True, 0)
            dfs(i, j, False, 0)
            visited.remove((i, j))
    
    return max_steps[0]

if __name__ == '__main__':
    print(solution(2, 2, [[1, 2], [4, 3]]) == 3)
    print(solution(3, 3, [[10, 1, 6], [5, 9, 3], [7, 2, 4]]) == 8)
    print(solution(4, 4, [[8, 3, 2, 1], [4, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]) == 11)