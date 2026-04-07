def solution(a: int, b: int) -> int:
    # Convert number a to a string
    str_a = str(a)
    str_b = str(b)

    # Initialize the maximum value
    max_num = float('-inf')

    # Iterate over all possible insertion positions
    for i in range(len(str_a) + 1):
        # Insert digit b at position i
        new_num = int(str_a[:i] + str_b + str_a[i:])
        # Update the maximum value
        max_num = max(max_num, new_num)

    return max_num

if __name__ == '__main__':
    print(solution(76543, 4) == 765443)
    print(solution(1, 0) == 10)
    print(solution(44, 5) == 544)
    print(solution(666, 6) == 6666)
