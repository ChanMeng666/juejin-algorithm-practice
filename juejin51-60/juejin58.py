def solution(rawStr, encodedStr):
    # Base32字符映射表
    char_map = "9876543210mnbvcxzasdfghjklpoiuyt"
    
    def str_to_bits(s):
        # 将字符串转换为二进制位串
        return ''.join(format(ord(c), '08b') for c in s)
    
    def bits_to_str(bits):
        # 将二进制位串转换回字符串
        # 确保位数是8的倍数
        if len(bits) % 8 != 0:
            bits = bits[:-(len(bits) % 8)]
        result = ""
        for i in range(0, len(bits), 8):
            if i + 8 <= len(bits):
                char = chr(int(bits[i:i+8], 2))
                if char != '\x00':  # 跳过空字符
                    result += char
        return result
    
    def encode(s):
        if not s:
            return ""
        # 获取二进制位串
        bits = str_to_bits(s)
        # 计算需要补充的0
        padding = (5 - len(bits) % 5) % 5
        bits += '0' * padding
        
        # 每5位转换为一个字符
        result = ""
        for i in range(0, len(bits), 5):
            chunk = bits[i:i+5]
            idx = int(chunk, 2)
            result += char_map[idx]
            
        # 根据原始位数确定需要补充的+号数量
        orig_bits_len = len(s) * 8
        if orig_bits_len % 40 == 8:
            result += "+" * 6
        elif orig_bits_len % 40 == 16:
            result += "+" * 4
        elif orig_bits_len % 40 == 24:
            result += "+" * 3
        elif orig_bits_len % 40 == 32:
            result += "+" * 1
            
        return result
    
    def decode(s):
        if not s:
            return ""
        # 移除填充符号
        s = s.rstrip('+')
        
        # 将Base32字符转换回二进制位串
        bits = ""
        for c in s:
            idx = char_map.index(c)
            bits += format(idx, '05b')
        
        return bits_to_str(bits)
    
    # 编码rawStr并解码encodedStr
    encoded = encode(rawStr)
    # 处理多段编码的情况
    decoded = ""
    for part in encodedStr.split('+' * 3):
        if part:
            decoded += decode(part + '+++')
            
    return f"{encoded}:{decoded}"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("foo", "b0zj5+++") == "bljhy+++:bar" )
    print(solution("The encoding process", "bljhy+++b0zj5+++") == "maf3m164vlahyl60vlds9i6svuahmiod:foobar" )
    print(solution("Base32 encoding and decoding", "bvchz+++v4j21+++cals9+++") == "10zj3l0d31z3mod6vus3sod258zhil89bash3oo5v4j3c+++:c]hintts " )
