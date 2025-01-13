def solution(s: str) -> int:
    # 将字符串转换为小写，这样就不用分别处理大小写了
    s = s.lower()
    
    # 分别统计'k'和'u'的数量
    k_count = s.count('k')
    u_count = s.count('u')
    
    # 能组成的"ku"数量取决于k和u中数量较少的那个
    return min(k_count, u_count)

if __name__ == '__main__':
    print(solution("AUBTMKAxfuu") == 1)
    print(solution("KKuuUuUuKKKKkkkkKK") == 6)
    print(solution("abcdefgh") == 0)