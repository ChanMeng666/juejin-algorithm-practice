def solution(n, max, array):
    # Count the occurrences of each number
    count_dict = {}
    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find all possible three-of-a-kind combinations
    triples = []
    for num, count in count_dict.items():
        if count >= 3:
            triples.append(num)

    # Find all possible pair combinations
    pairs = []
    for num, count in count_dict.items():
        if count >= 2:
            pairs.append(num)

    # If there are not enough cards to form a full house, return [0, 0]
    if not triples or not pairs:
        return [0, 0]

    # Sort triples and pairs by card value (considering 1/Ace as the highest)
    triples.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)
    pairs.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)

    # Find the largest valid full house combination
    result = [0, 0]
    for triple in triples:
        for pair in pairs:
            # Skip if using the same number for both
            if triple == pair:
                continue
            # Calculate the total card value sum
            total = triple * 3 + pair * 2
            # Check if it exceeds the maximum value
            if total > max:
                continue
            # If a valid combination is found, return immediately (since we sorted by value)
            return [triple, pair]

    return [0, 0]


if __name__ == "__main__":
    # Add your test cases here
    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]) == [0, 0])
