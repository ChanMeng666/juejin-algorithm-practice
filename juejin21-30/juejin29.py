def solution(s: str, k: int) -> str:
    # 定义字符转换规则
    transform = {
        'a': 'bc',
        'b': 'ca',
        'c': 'ab'
    }
    
    # 执行k次转换
    for _ in range(k):
        # 对当前字符串中的每个字符进行转换
        new_s = ''
        for char in s:
            new_s += transform[char]
        s = new_s
    
    return s

if __name__ == '__main__':
    print(solution("abc", 2) == 'caababbcbcca')
    print(solution("abca", 3) == 'abbcbccabccacaabcaababbcabbcbcca')
    print(solution("cba", 1) == 'abcabc')