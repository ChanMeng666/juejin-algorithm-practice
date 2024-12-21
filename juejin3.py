def solution(s: str) -> str:
    # 分割整数部分和小数部分
    parts = s.split('.')
    
    # 处理整数部分：去除前导零并添加千分位逗号
    integer_part = parts[0].lstrip('0')
    if not integer_part:  # 如果整数部分为空（即原数为0开头）
        integer_part = '0'
        
    # 从右向左每三位添加逗号
    formatted_int = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and i % 3 == 0:
            formatted_int = ',' + formatted_int
        formatted_int = digit + formatted_int
    
    # 如果有小数部分，则添加回去
    if len(parts) > 1:
        return formatted_int + '.' + parts[1]
    
    return formatted_int

if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')