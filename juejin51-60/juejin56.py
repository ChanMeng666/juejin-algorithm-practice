def solution(n, cats_levels):
    # 初始化每只猫获得的鱼干数量为1
    candies = [1] * n
    
    # 从左向右遍历，确保等级高的猫比左边的猫获得更多鱼干
    for i in range(1, n):
        if cats_levels[i] > cats_levels[i-1]:
            candies[i] = candies[i-1] + 1
    
    # 从右向左遍历，确保等级高的猫比右边的猫获得更多鱼干
    for i in range(n-2, -1, -1):
        if cats_levels[i] > cats_levels[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    # 返回所需的总鱼干数量
    return sum(candies)

if __name__ == "__main__":
    #  You can add more test cases here
    cats_levels1 = [1, 2, 2]
    cats_levels2 = [6, 5, 4, 3, 2, 16]
    cats_levels3 = [1, 2, 2, 3, 3, 20, 1, 2, 3, 3, 2, 1, 5, 6, 6, 5, 5, 7, 7, 4]
    print(solution(3, cats_levels1) == 4)
    print(solution(6, cats_levels2) == 17)
    print(solution(20, cats_levels3) == 35)