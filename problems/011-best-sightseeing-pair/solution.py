def solution(values: list) -> int:
    max_score = float('-inf')  # Initialize max score to negative infinity
    max_value_plus_i = values[0] + 0  # Initialize values[i] + i for the first position

    # Iterate through all sightseeing spots starting from the second position
    for j in range(1, len(values)):
        # Calculate the current combination score
        current_score = max_value_plus_i + (values[j] - j)
        max_score = max(max_score, current_score)

        # Update max_value_plus_i for the next iteration
        max_value_plus_i = max(max_value_plus_i, values[j] + j)

    return max_score

if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)
