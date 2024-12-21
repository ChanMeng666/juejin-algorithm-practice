def solution(m:int, s:str)->int:
    ls = s.split("UCC")
    ans = len(ls) - 1
    c1 = c2 = 0
    for s in ls:
        i = 0
        k = len(s)
        while i < k:
            if i + 1 < k and s[i + 1] == 'C':
                i += 2
                c1 += 1
            else:
                i += 1
                c2 += 1
    k1 = min(m, c1)
    m -= k1
    ans += k1
    k2 = min(m >> 1, c2)
    ans += k2
    m -= k2 * 2
    ans += m // 3
    return ans

if __name__ == '__main__':
    print(solution(m = 3,s = "UCUUCCCCC") == 3)
    print(solution(m = 6,s = "U") == 2)
    print(solution(m = 2,s = "UCCUUU") == 2)
    print(solution(m = 10, s = "CUUUCC") == 5)