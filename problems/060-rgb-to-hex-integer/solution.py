def solution(rgb):
    # Extract numbers from the rgb string
    rgb = rgb.replace('rgb(', '').replace(')', '')
    r, g, b = map(int, rgb.split(','))

    # Calculate the hexadecimal integer value
    # Using bit shifting: (r << 16) + (g << 8) + b
    return (r << 16) + (g << 8) + b

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("rgb(192, 192, 192)") == 12632256 )
    print(solution("rgb(100, 0, 252)") == 6553852)
    print(solution("rgb(33, 44, 55)") == 2174007)
