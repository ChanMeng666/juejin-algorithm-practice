def solution(s: str) -> int:
    # Convert the string to lowercase so we don't need to handle upper and lower case separately
    s = s.lower()

    # Count the occurrences of 'k' and 'u' respectively
    k_count = s.count('k')
    u_count = s.count('u')

    # The number of "ku" pairs that can be formed depends on whichever count is smaller
    return min(k_count, u_count)

if __name__ == '__main__':
    print(solution("AUBTMKAxfuu") == 1)
    print(solution("KKuuUuUuKKKKkkkkKK") == 6)
    print(solution("abcdefgh") == 0)
