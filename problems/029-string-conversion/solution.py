def solution(s: str, k: int) -> str:
    # Define character conversion rules
    transform = {
        'a': 'bc',
        'b': 'ca',
        'c': 'ab'
    }

    # Perform k conversions
    for _ in range(k):
        # Convert each character in the current string
        new_s = ''
        for char in s:
            new_s += transform[char]
        s = new_s

    return s

if __name__ == '__main__':
    print(solution("abc", 2) == 'caababbcbcca')
    print(solution("abca", 3) == 'abbcbccabccacaabcaababbcabbcbcca')
    print(solution("cba", 1) == 'abcabc')
