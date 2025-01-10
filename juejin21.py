def solution(n: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    
    def dist(i, j):
        # 计算两个数的贡献值：(a_i + a_j) * dist(i, j)
        # dist(i, j) 是环形数组中两个位置的最短距离
        distance = min((i - j) % n, (j - i) % n)
        return (a[i] + a[j]) * distance
    
    max_contribution = 0
    
    # 遍历所有可能的数对
    for i in range(n):
        for j in range(i + 1, n):
            contribution = dist(i, j)
            max_contribution = max(max_contribution, contribution)
    
    return max_contribution

if __name__ == '__main__':
    print(solution(n = 3, a = [1, 2, 3]) == 5)
    print(solution(n = 4, a = [4, 1, 2, 3]) == 12)
    print(solution(n = 5, a = [1, 5, 3, 7, 2]) == 24)
