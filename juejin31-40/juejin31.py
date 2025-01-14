def solution(word: str) -> int:
    # 将所有非数字字符替换为空格
    processed = ''.join(' ' if not c.isdigit() else c for c in word)
    
    # 分割字符串，去除空字符串
    numbers = [num for num in processed.split() if num]
    
    # 去除前导零并转换为集合来统计不同数字的个数
    unique_numbers = set(str(int(num)) for num in numbers)
    
    return len(unique_numbers)

if __name__ == '__main__':
    print(solution("a123bc34d8ef34") == 3)
    print(solution("t1234c23456") == 2)
    print(solution("a1b01c001d4") == 2)