def solution(n):
    MOD = 202220222022

    # Calculate possible scores for a single course
    def get_scores():
        scores = []
        for i in range(21):  # 0 to 20 correct answers
            scores.append(i * 5)
        return scores

    # Calculate the minimum total score required across all courses
    def get_min_total(total_courses):
        return 60 * total_courses

    # Solve using dynamic programming
    def dp_solve(n):
        scores = get_scores()
        total_courses = n + 3  # 3 required courses + n elective courses
        min_total = get_min_total(total_courses)

        # dp[i][j] represents the number of combinations for i courses with total score j
        dp = [[0] * (100 * total_courses + 1) for _ in range(total_courses + 1)]
        dp[0][0] = 1

        # Dynamic programming for each course
        for i in range(total_courses):
            for j in range(i * 100 + 1):
                if dp[i][j] == 0:
                    continue
                # Enumerate all possible scores for the current course
                for score in scores:
                    dp[i + 1][j + score] = (dp[i + 1][j + score] + dp[i][j]) % MOD

        # Count all passing combinations
        result = 0
        for j in range(min_total, 100 * total_courses + 1):
            result = (result + dp[total_courses][j]) % MOD

        return str(result)

    return dp_solve(n)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3) == "19195617" )
    print(solution(6) == "135464411082" )
    print(solution(49) == "174899025576" )
    print(solution(201) == "34269227409" )
    print(solution(888) == "194187156114" )
