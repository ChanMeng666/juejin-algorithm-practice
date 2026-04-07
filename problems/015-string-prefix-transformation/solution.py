def solution(S: str, T: str) -> int:
    # If S is already a prefix of T, return 0 directly
    if T.startswith(S):
        return 0

    # Get the lengths of both strings
    s_len = len(S)
    t_len = len(T)

    # If S is longer than T, we need to delete the extra characters
    if s_len > t_len:
        # First calculate the number of characters to delete
        delete_count = s_len - t_len
        # Then calculate the number of characters to modify among the first t_len characters
        change_count = sum(1 for i in range(t_len) if S[i] != T[i])
        return delete_count + change_count

    # If S is shorter than or equal to T, only calculate the number of characters to modify
    return sum(1 for i in range(s_len) if S[i] != T[i])

if __name__ == '__main__':
    print(solution("aba", "abb") == 1)
    print(solution("abcd", "efg") == 4)
    print(solution("xyz", "xy") == 1)
    print(solution("hello", "helloworld") == 0)
    print(solution("same", "same") == 0)
