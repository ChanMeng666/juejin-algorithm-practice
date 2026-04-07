def solution(a, b):
    # Create two sets to store the numbers
    set_a = set(a)
    set_b = set(b)

    # Find the intersection of the two sets
    intersection = set_a & set_b

    # Convert the intersection to a list and sort in descending order
    result = sorted(list(intersection), reverse=True)

    return result

if __name__ == '__main__':
    print(solution([1, 2, 3, 7], [2, 5, 7]) == [7, 2])
    print(solution([1, 4, 8, 10], [2, 4, 8, 10]) == [10, 8, 4])
    print(solution([3, 5, 9], [1, 4, 6]) == [])
    print(solution([1, 2, 3], [1, 2, 3]) == [3, 2, 1])
