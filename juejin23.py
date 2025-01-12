def solution(stones: list) -> int:
    if len(stones) < 2:
        return 0
    
    stones = stones.copy()
    moves = 0
    
    while True:
        stones.sort()
        n = len(stones)
        
        # 检查是否已经连续
        if stones[-1] - stones[0] == n - 1 and len(set(stones)) == n:
            return moves
        
        # 找到所有空位
        empty = set(range(min(stones), max(stones))) - set(stones)
        if not empty:
            return moves
            
        # 找到最大的间隙
        max_gap = 0
        gap_start = 0
        
        for i in range(1, len(stones)):
            curr_gap = stones[i] - stones[i-1] - 1
            if curr_gap > max_gap:
                max_gap = curr_gap
                gap_start = stones[i-1]
        
        # 如果最大间隙小于等于1，说明已经连续
        if max_gap <= 1:
            return moves
        
        # 移动端点到最大间隙的一端
        if stones[-1] - stones[-2] >= stones[1] - stones[0]:
            # 移动右端点
            stones[-1] = gap_start + 1
        else:
            # 移动左端点
            stones[0] = gap_start + max_gap
        
        moves += 1

if __name__ == '__main__':
    print(solution(stones=[7, 4, 9]) == 2)
    print(solution(stones=[6, 5, 4, 3, 10]) == 3)
    print(solution(stones=[1, 2, 3, 4, 5]) == 0)
    print(solution(stones=[12, 15, 7, 2, 13]) == 8)