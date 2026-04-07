def solution(n: int, u: list) -> int:
    # If there is only one hero, training is not possible
    if n <= 1:
        return 0

    # Find all distinct levels and sort them
    levels = sorted(set(u))

    # If all heroes have the same level, no level-up is possible
    if len(levels) == 1:
        return 0

    # Find the minimum level
    min_level = levels[0]

    # Count all heroes with levels higher than the minimum
    # These heroes can level up by training with the minimum-level hero
    result = sum(1 for x in u if x > min_level)

    return result

if __name__ == '__main__':
    print(solution(n = 5, u = [1, 2, 3, 1, 2]) == 3)
    print(solution(n = 4, u = [100000, 100000, 100000, 100000]) == 0)
    print(solution(n = 6, u = [1, 1, 1, 2, 2, 2]) == 3)
