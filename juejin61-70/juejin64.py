def solution(number, heroes):
    # 将英雄按能力值从大到小排序
    sorted_heroes = sorted(heroes, reverse=True)
    wins = 0
    
    # 遍历每一轮比赛
    for i in range(number):
        # 小正的英雄能力值为i+1
        opponent = i + 1
        # 如果我方最强的英雄能力值大于对手，则使用当前最强英雄
        if sorted_heroes[i] > opponent:
            wins += 1
            
    return wins

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(7, [10,1,1,1,5,5,3]) == 4 )
    print(solution(5, [1,1,1,1,1]) == 0 )
    print(solution(10, [1,2,3,4,5,6,7,8,9,10]) == 9 )