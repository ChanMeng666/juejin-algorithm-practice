def solution(n, cats_levels):
    # Initialize the amount of fish treats each cat receives to 1
    candies = [1] * n

    # Traverse left to right, ensuring higher-level cats get more treats than the cat on the left
    for i in range(1, n):
        if cats_levels[i] > cats_levels[i-1]:
            candies[i] = candies[i-1] + 1

    # Traverse right to left, ensuring higher-level cats get more treats than the cat on the right
    for i in range(n-2, -1, -1):
        if cats_levels[i] > cats_levels[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    # Return the total number of fish treats needed
    return sum(candies)

if __name__ == "__main__":
    #  You can add more test cases here
    cats_levels1 = [1, 2, 2]
    cats_levels2 = [6, 5, 4, 3, 2, 16]
    cats_levels3 = [1, 2, 2, 3, 3, 20, 1, 2, 3, 3, 2, 1, 5, 6, 6, 5, 5, 7, 7, 4]
    print(solution(3, cats_levels1) == 4)
    print(solution(6, cats_levels2) == 17)
    print(solution(20, cats_levels3) == 35)
