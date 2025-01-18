def get_min_changes(freq):
    length = sum(freq.values())
    target = length // 4
    
    # 计算需要改变的字符总数
    total_changes = 0
    for f in freq.values():
        if f > target:
            total_changes += f - target
    
    # 每次替换会处理两个字符，所以需要除以2
    # 当total_changes为奇数时，向上取整
    return (total_changes + 1) // 2

def check_substring(s):
    # 统计子串中的字符频率
    freq = {'A': 0, 'S': 0, 'D': 0, 'F': 0}
    for c in s:
        freq[c] += 1
    return get_min_changes(freq)

def solution(input):
    n = len(input)
    if n % 4 != 0:
        return -1
    
    min_changes = n  # 初始化为最大可能值
    
    # 遍历所有可能的子串
    for i in range(len(input)):
        for j in range(i + 3, len(input)):
            # 只检查长度为4的倍数的子串
            if (j - i + 1) % 4 == 0:
                curr_changes = check_substring(input[i:j+1])
                if curr_changes < min_changes:
                    min_changes = curr_changes
                
                # 如果找到完美平衡的子串
                if min_changes == 0:
                    return 0
    
    return min_changes

if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("ADDF", 1),
        ("ASAFASAFADDD", 3),
        ("SSDDFFFFAAAS", 1),
        ("AAAASSSSDDDDFFFF", 0),
        ("AAAADDDDAAAASSSS", 4)
    ]
    
    for test_input, expected in test_cases:
        result = solution(test_input)
        print(f"Input: {test_input}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 30)