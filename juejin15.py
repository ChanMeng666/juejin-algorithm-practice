def solution(S: str, T: str) -> int:
    # 如果S已经是T的前缀，直接返回0
    if T.startswith(S):
        return 0
    
    # 获取两个字符串的长度
    s_len = len(S)
    t_len = len(T)
    
    # 如果S比T长，需要删除多余的字符
    if s_len > t_len:
        # 先计算需要删除的字符数
        delete_count = s_len - t_len
        # 然后计算前t_len个字符中需要修改的字符数
        change_count = sum(1 for i in range(t_len) if S[i] != T[i])
        return delete_count + change_count
    
    # 如果S长度小于或等于T，只需要计算需要修改的字符数
    return sum(1 for i in range(s_len) if S[i] != T[i])

if __name__ == '__main__':
    print(solution("aba", "abb") == 1)
    print(solution("abcd", "efg") == 4)
    print(solution("xyz", "xy") == 1)
    print(solution("hello", "helloworld") == 0)
    print(solution("same", "same") == 0)