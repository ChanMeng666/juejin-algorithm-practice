def solution(binary1, binary2):
    # 将二进制字符串转换为十进制数
    def bin_to_dec(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal
    
    # 分别转换两个二进制数并相加
    num1 = bin_to_dec(binary1)
    num2 = bin_to_dec(binary2)
    
    # 返回和的字符串形式
    return str(num1 + num2)

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("101", "110") == "11")
    print(solution("111111", "10100") == "83")
    print(solution("111010101001001011", "100010101001") == "242420")
    print(solution("111010101001011", "10010101001") == "31220")