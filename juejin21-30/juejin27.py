def solution(n: int, u: list) -> int:
    # 如果只有一个英雄，无法进行历练
    if n <= 1:
        return 0
        
    # 找出所有不同的等级并排序
    levels = sorted(set(u))
    
    # 如果所有英雄等级都相同，则无法提升
    if len(levels) == 1:
        return 0
    
    # 找出最小等级
    min_level = levels[0]
    
    # 统计所有比最小等级高的英雄数量
    # 这些英雄都可以通过与最小等级的英雄历练来提升
    result = sum(1 for x in u if x > min_level)
            
    return result

if __name__ == '__main__':
    print(solution(n = 5, u = [1, 2, 3, 1, 2]) == 3)
    print(solution(n = 4, u = [100000, 100000, 100000, 100000]) == 0)
    print(solution(n = 6, u = [1, 1, 1, 2, 2, 2]) == 3)