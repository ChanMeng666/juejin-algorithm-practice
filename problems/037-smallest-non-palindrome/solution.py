def solution(s: str) -> str:
    n = len(s)
    # If the string itself is a palindrome, it is impossible to construct a smaller palindrome
    if s == s[::-1]:
        return '-1'

    # Convert the string to a list for modification
    t = list(s)

    # Iterate through each position from left to right
    for i in range(n):
        # Symmetric position
        j = n - 1 - i

        # If we have reached the middle or beyond, exit the loop
        if i >= j:
            break

        # If the characters at symmetric positions differ
        if s[i] != s[j]:
            # Choose the larger character as the reference
            max_char = max(s[i], s[j])
            # Set both positions to this character
            t[i] = t[j] = max_char
            # Check if the result is less than the original string
            temp = ''.join(t)
            if temp < s:
                return temp
            # If not less than the original, set both positions to (larger character - 1)
            t[i] = t[j] = chr(ord(max_char) - 1)
            return ''.join(t)

    # If the string is mostly symmetric, modify the middle character
    mid = n // 2
    if n % 2 == 1:
        if t[mid] > 'a':
            t[mid] = chr(ord(t[mid]) - 1)
            return ''.join(t)

    return '-1'

if __name__ == '__main__':
    print(solution("abc") == 'aba')
    print(solution("cba") == 'cac')
    print(solution("aaa") == '-1')
