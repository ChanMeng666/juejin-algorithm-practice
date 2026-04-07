def solution(n: int) -> int:
    # If there is only 1 team, return 0 directly
    if n == 1:
        return 0

    total_matches = 0
    remaining_teams = n

    # Continue the tournament while more than 1 team remains
    while remaining_teams > 1:
        if remaining_teams % 2 == 0:
            # Even number of teams: play n/2 matches
            matches = remaining_teams // 2
            remaining_teams = matches
        else:
            # Odd number of teams: one team gets a bye, remaining teams play (n-1)/2 matches
            matches = (remaining_teams - 1) // 2
            remaining_teams = matches + 1

        total_matches += matches

    return total_matches

if __name__ == '__main__':
    print(solution(7) == 6)
    print(solution(14) == 13)
    print(solution(1) == 0)
