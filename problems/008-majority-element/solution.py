def solution(array):
    # Use Boyer-Moore Voting Algorithm
    candidate = array[0]  # Candidate number
    count = 1  # Counter

    # First pass: find the potential majority element
    for num in array[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Second pass: verify that this number indeed appears more than half the time
    count = sum(1 for num in array if num == candidate)
    if count > len(array) // 2:
        return candidate

    return 0  # If no qualifying number exists (though per the problem description this case won't occur)


if __name__ == "__main__":
    # Test cases
    print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]) == 3)  # True
    print(solution([5, 5, 5, 1, 2, 5, 5]) == 5)  # True
    print(solution([9, 9, 9, 9, 8, 9, 8, 8]) == 9)  # True
