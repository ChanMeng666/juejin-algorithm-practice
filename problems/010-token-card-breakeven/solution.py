def solution(a: int, b: int) -> int:
    # Use ceiling division to calculate the required number of days
    # If a is not divisible by b, one extra day is needed
    return (a + b - 1) // b

if __name__ == '__main__':
    print(solution(10, 1) == 10)
    print(solution(10, 2) == 5)
    print(solution(10, 3) == 4)
