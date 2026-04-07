def solution(cards):
    # Use XOR operation to find the unique number
    result = 0
    for num in cards:
        result ^= num
    return result


if __name__ == "__main__":
    # Test cases
    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)  # True
    print(solution([0, 1, 0, 1, 2]) == 2)  # True
    print(solution([7, 3, 3, 7, 10]) == 10)  # True
