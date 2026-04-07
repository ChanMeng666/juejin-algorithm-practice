def solution(n: int, k: int) -> int:
    # Create an array to store the selected numbers
    result = []
    # Starting from k, find n multiples of k
    current = k
    while len(result) < n:
        result.append(current)
        current += k

    # Return the sum of array elements
    return sum(result)

if __name__ == '__main__':
    print(solution(n = 3, k = 1) == 6)  # 1 + 2 + 3 = 6
    print(solution(n = 2, k = 2) == 6)  # 2 + 4 = 6
    print(solution(n = 4, k = 3) == 30) # 3 + 6 + 9 + 12 = 30
