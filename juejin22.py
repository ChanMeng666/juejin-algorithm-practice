def solution(S: str) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # 统计每个字符的出现次数
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1
    
    operations = 0
    # 对于每个出现次数大于1的字符
    for count in char_count.values():
        # 如果字符出现次数大于1
        # 每次操作删除2个字符，所以需要 (count//2) 次操作
        operations += count // 2
            
    return operations

if __name__ == '__main__':
    print(solution(S = "abab") == 2)
    print(solution(S = "aaaa") == 2)
    print(solution(S = "abcabc") == 3)
