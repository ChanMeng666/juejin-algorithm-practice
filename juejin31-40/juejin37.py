def solution(s: str) -> str:
    n = len(s)
    # 如果字符串本身是回文串，则无法构造更小的回文串
    if s == s[::-1]:
        return '-1'
        
    # 将字符串转换为列表以便修改
    t = list(s)
    
    # 从左到右遍历每个位置
    for i in range(n):
        # 对称位置
        j = n - 1 - i
        
        # 如果已经处理到中间或之后的位置，退出循环
        if i >= j:
            break
            
        # 如果对称位置的字符不同
        if s[i] != s[j]:
            # 选择较大的字符作为基准
            max_char = max(s[i], s[j])
            # 将两个位置都设为这个字符
            t[i] = t[j] = max_char
            # 检查是否小于原字符串
            temp = ''.join(t)
            if temp < s:
                return temp
            # 如果不小于原字符串，将两个位置都设为较大字符-1
            t[i] = t[j] = chr(ord(max_char) - 1)
            return ''.join(t)
    
    # 如果字符串基本对称，需要修改中间的字符
    mid = n // 2
    if n % 2 == 1:
        if t[mid] > 'a':
            t[mid] = chr(ord(t[mid]) - 1)
            return ''.join(t)
    
    return '-1'

if __name__ == '__main__':
    print(solution("abc") == 'aba')
    print(solution("cba") == 'cac')
    print(solution("aaa") == '-1')