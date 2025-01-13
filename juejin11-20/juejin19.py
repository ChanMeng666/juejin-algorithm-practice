def solution(n: int, k: int, s: str) -> str:
    # 将字符串转换为列表以便修改
    s = list(s)
    remaining_moves = k
    
    # 遍历字符串的每个位置
    i = 0
    while i < n and remaining_moves > 0:
        # 在剩余可移动范围内找到最小的字符
        best_pos = i
        for j in range(i + 1, min(i + remaining_moves + 1, n)):
            if s[j] < s[best_pos]:
                best_pos = j
        
        # 如果找到更小的字符，将它移动到当前位置
        if best_pos != i:
            # 将找到的字符移动到位置i
            moves_needed = best_pos - i
            for j in range(best_pos, i, -1):
                s[j], s[j-1] = s[j-1], s[j]
            remaining_moves -= moves_needed
        i += 1
    
    return ''.join(s)

if __name__ == '__main__':
    print(solution(5, 2, "01010") == '00101')
    print(solution(7, 3, "1101001") == '0110101')
    print(solution(4, 1, "1001") == '0101')