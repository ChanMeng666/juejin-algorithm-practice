def solution(n):
    MOD = 202220222022
    
    # 计算单门课程可能的得分情况
    def get_scores():
        scores = []
        for i in range(21):  # 0到20题正确
            scores.append(i * 5)
        return scores
        
    # 计算所有课程的总分要求
    def get_min_total(total_courses):
        return 60 * total_courses
    
    # 动态规划求解
    def dp_solve(n):
        scores = get_scores()
        total_courses = n + 3  # 必修课3门 + 选修课n门
        min_total = get_min_total(total_courses)
        
        # dp[i][j] 表示i门课程总分为j的组合数
        dp = [[0] * (100 * total_courses + 1) for _ in range(total_courses + 1)]
        dp[0][0] = 1
        
        # 对每门课程进行动态规划
        for i in range(total_courses):
            for j in range(i * 100 + 1):
                if dp[i][j] == 0:
                    continue
                # 枚举当前课程的所有可能分数
                for score in scores:
                    dp[i + 1][j + score] = (dp[i + 1][j + score] + dp[i][j]) % MOD
        
        # 统计所有及格的组合数
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