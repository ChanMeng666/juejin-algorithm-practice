def solution(n: int, l: int, r: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # Count the number of perfect even numbers
    count = 0

    # Iterate over each number in the array
    for num in a:
        # Check if both conditions for a perfect even number are met:
        # 1. The number is even (num % 2 == 0)
        # 2. The number is within the range [l, r] (l <= num <= r)
        if num % 2 == 0 and l <= num <= r:
            count += 1

    return count

if __name__ == '__main__':
    print(solution(5, 3, 8, [1, 2, 6, 8, 7]) == 2)
    print(solution(4, 10, 20, [12, 15, 18, 9]) == 2)
    print(solution(3, 1, 10, [2, 4, 6]) == 3)
