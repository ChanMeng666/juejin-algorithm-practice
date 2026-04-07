def solution(str1):
    # Start trying from the shortest possible substring
    n = len(str1)
    for i in range(1, n + 1):
        # Take the first i characters as the candidate initial string
        candidate = str1[:i]
        current = candidate

        # Track strings already tried to avoid cycles
        seen = {current}
        queue = [(current, 0)]  # (current string, number of steps used)

        while queue:
            current, steps = queue.pop(0)
            if current == str1:
                return candidate

            if steps >= n:  # Prevent infinite loop
                break

            # Try all possible values of K
            for k in range(len(current)):
                # Append the substring starting from position k to the end
                next_str = current + current[k:]
                if len(next_str) <= len(str1) and next_str not in seen and str1.startswith(next_str):
                    seen.add(next_str)
                    queue.append((next_str, steps + 1))

    return str1


if __name__ == "__main__":
    # Add your test cases here

    print(solution("abbabbbabb") == "ab")
    print(solution("abbbabbbb") == "ab")
    print(
        solution(
            "jiabanbananananiabanbananananbananananiabanbananananbananananbananananbanananan"
        )
        == "jiaban"
    )
    print(
        solution(
            "selectecttectelectecttectcttectselectecttectelectecttectcttectectelectecttectcttectectcttectectcttectectcttect"
        )
        == "select"
    )
    print(
        solution(
            "discussssscussssiscussssscussssdiscussssscussssiscussssscussssiscussssscussss"
        )
        == "discus"
    )
