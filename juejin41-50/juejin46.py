def add_large_numbers(num1, num2):
    # 确保num1长度大于等于num2
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    # 补齐较短的数字
    num2 = '0' * (len(num1) - len(num2)) + num2
    
    carry = 0
    result = ''
    
    # 从右向左逐位相加
    for i in range(len(num1)-1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result = str(digit_sum % 10) + result
    
    # 处理最后的进位
    if carry:
        result = '1' + result
    
    return result

def solution(string1, string2):
    # 计算两个大数之和
    sum_result = add_large_numbers(string1, string2)
    
    # 如果结果中所有数字都相同，返回0
    if len(set(sum_result)) == 1:
        return 0
    
    # 遍历相邻数字，检查是否有不同的数字
    for i in range(len(sum_result)-1):
        if sum_result[i] != sum_result[i+1]:
            return 1
    
    return 0

if __name__ == "__main__":
    # 测试用例
    print(solution("111", "222") == 0)  # True
    print(solution("111", "34") == 1)   # True
    print(solution("999", "1") == 0)    # True
    print(solution("5976762424003073", "6301027308640389") == 6)  # True