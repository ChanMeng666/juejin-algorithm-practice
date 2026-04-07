def solution(s: str) -> str:
    # Split the integer part and decimal part
    parts = s.split('.')

    # Process the integer part: remove leading zeros and add thousands separators
    integer_part = parts[0].lstrip('0')
    if not integer_part:  # If the integer part is empty (i.e., original number starts with 0)
        integer_part = '0'

    # Add commas from right to left every three digits
    formatted_int = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and i % 3 == 0:
            formatted_int = ',' + formatted_int
        formatted_int = digit + formatted_int

    # If there is a decimal part, append it
    if len(parts) > 1:
        return formatted_int + '.' + parts[1]

    return formatted_int

if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')
