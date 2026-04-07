def solution(S: str) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # Count the occurrences of each character
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1

    operations = 0
    # For each character that appears more than once
    for count in char_count.values():
        # If the character appears more than once
        # Each operation removes 2 characters, so we need (count//2) operations
        operations += count // 2

    return operations

if __name__ == '__main__':
    print(solution(S = "abab") == 2)
    print(solution(S = "aaaa") == 2)
    print(solution(S = "abcabc") == 3)
