def solution(n: int, s: list, x: list) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # Create a list containing index, name, and amount
    data = list(zip(range(n), s, x))

    # Sort by amount in descending order; if amounts are equal, sort by red packet order (index) in ascending order
    sorted_data = sorted(data, key=lambda x: (-x[2], x[0]))

    # Return the sorted list of names
    result = [name for _, name, _ in sorted_data]

    return result

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])
