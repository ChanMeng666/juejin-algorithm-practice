def solution(n: int, k: int, s: str) -> str:
    # Convert the string to a list for easy modification
    s = list(s)
    remaining_moves = k

    # Iterate through each position in the string
    i = 0
    while i < n and remaining_moves > 0:
        # Find the smallest character within the remaining movable range
        best_pos = i
        for j in range(i + 1, min(i + remaining_moves + 1, n)):
            if s[j] < s[best_pos]:
                best_pos = j

        # If a smaller character is found, move it to the current position
        if best_pos != i:
            # Move the found character to position i
            moves_needed = best_pos - i
            for j in range(best_pos, i, -1):
                s[j], s[j-1] = s[j-1], s[j]
            remaining_moves -= moves_needed
        i += 1

    return ''.join(s)

if __name__ == '__main__':
    print(solution(5, 2, "01010") == '00101')
    print(solution(7, 3, "1101001") == '0110101')
    print(solution(4, 1, "1001") == '0101')
