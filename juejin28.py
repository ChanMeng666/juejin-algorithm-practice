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
    
    # 判断一个位置是否在地图内
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M
    
    # 获取一个位置可以到达的下一个位置
    def get_next_positions(x, y):
        positions = []
        curr = data[x][y]
        
        # 如果是传送器，只能到达传送的位置
        if curr == 'U' and is_valid(x-1, y):
            positions.append((x-1, y))
        elif curr == 'D' and is_valid(x+1, y):
            positions.append((x+1, y))
        elif curr == 'L' and is_valid(x, y-1):
            positions.append((x, y-1))
        elif curr == 'R' and is_valid(x, y+1):
            positions.append((x, y+1))
        # 如果是普通地板或出口，可以走到四个方向
        elif curr in '.O':
            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if is_valid(nx, ny):
                    positions.append((nx, ny))
        
        return positions
    
    # 从一个位置可以反向到达的位置
    def get_prev_positions(x, y):
        positions = []
        # 检查四个方向
        for px, py in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not is_valid(px, py):
                continue
            # 检查该位置是否可以到达当前位置
            curr = data[px][py]
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
    
    # 使用BFS找出所有可以到达出口的位置
    safe_positions = set()
    queue = [exit_pos]
    safe_positions.add(exit_pos)
    
    while queue:
        curr_x, curr_y = queue.pop(0)
        # 获取所有可以到达当前位置的前置位置
        prev_positions = get_prev_positions(curr_x, curr_y)
        for px, py in prev_positions:
            if (px, py) not in safe_positions:
                safe_positions.add((px, py))
                queue.append((px, py))
    
    # 计算危险位置的数量
    danger_count = N * M - len(safe_positions)
    return danger_count

if __name__ == "__main__":
    # 测试用例
    pattern = [
        [".",  ".", ".", ".", "."],
        [".",  "R", "R", "D", "."],
        [".", "U", ".", "D", "R"],
        [".", "U", "L", "L", "."],
        [".", ".", ".", ".", "O"]
    ]
    print(solution(5, 5, pattern) == 10)
    
    pattern2 = [[".", "R", ".", "O"], 
                ["U", ".", "L", "."], 
                [".", "D", ".", "."], 
                [".", ".", "R", "D"]]
    print(solution(4, 4, pattern2) == 2)
    
    pattern3 = [[".", "U", "O"],
                ["L", ".", "R"],
                ["D", ".", "."]]
    print(solution(3, 3, pattern3) == 8)