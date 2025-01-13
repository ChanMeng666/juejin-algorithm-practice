def solution(n: int) -> int:
    # 如果只有1支队伍，直接返回0
    if n == 1:
        return 0
    
    total_matches = 0
    remaining_teams = n
    
    # 当还有超过1支队伍时继续比赛
    while remaining_teams > 1:
        if remaining_teams % 2 == 0:
            # 偶数队伍：进行 n/2 场比赛
            matches = remaining_teams // 2
            remaining_teams = matches
        else:
            # 奇数队伍：一支轮空，其余队伍进行 (n-1)/2 场比赛
            matches = (remaining_teams - 1) // 2
            remaining_teams = matches + 1
        
        total_matches += matches
    
    return total_matches

if __name__ == '__main__':
    print(solution(7) == 6)
    print(solution(14) == 13)
    print(solution(1) == 0)