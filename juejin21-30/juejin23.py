def solution(stones: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # 将石子位置转换为集合，方便查找和删除
    stone_positions = set(stones)
    moves = 0
    
    while True:
        # 找到当前的最小和最大位置
        min_pos = min(stone_positions)
        max_pos = max(stone_positions)
        
        # 尝试移动一个端点
        moved = False
        
        # 检查最小端点是否可以移动
        for pos in range(min_pos + 1, max_pos):
            if pos not in stone_positions:
                stone_positions.remove(min_pos)
                stone_positions.add(pos)
                moves += 1
                moved = True
                break
                
        if not moved:
            # 如果最小端点不能移动，检查最大端点
            for pos in range(max_pos - 1, min_pos, -1):
                if pos not in stone_positions:
                    stone_positions.remove(max_pos)
                    stone_positions.add(pos)
                    moves += 1
                    moved = True
                    break
        
        if not moved:
            break
    
    return moves

if __name__ == '__main__':
    print(solution(stones=[7, 4, 9]) == 2)
    print(solution(stones=[6, 5, 4, 3, 10]) == 3)
    print(solution(stones=[1, 2, 3, 4, 5]) == 0)