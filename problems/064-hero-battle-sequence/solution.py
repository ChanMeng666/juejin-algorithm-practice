def solution(number, heroes):
    # Sort heroes by power value in descending order
    sorted_heroes = sorted(heroes, reverse=True)
    wins = 0

    # Iterate through each round of the battle
    for i in range(number):
        # The opponent's hero power value is i+1
        opponent = i + 1
        # If our strongest hero's power value is greater than the opponent's, use the current strongest hero
        if sorted_heroes[i] > opponent:
            wins += 1

    return wins

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(7, [10,1,1,1,5,5,3]) == 4 )
    print(solution(5, [1,1,1,1,1]) == 0 )
    print(solution(10, [1,2,3,4,5,6,7,8,9,10]) == 9 )
