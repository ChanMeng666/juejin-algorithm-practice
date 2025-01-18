def solution(str1):
    # 从最短可能的子串开始尝试
    n = len(str1)
    for i in range(1, n + 1):
        # 获取前i个字符作为候选初始字符串
        candidate = str1[:i]
        current = candidate
        
        # 记录已经尝试过的字符串，避免循环
        seen = {current}
        queue = [(current, 0)]  # (当前字符串, 已使用的步数)
        
        while queue:
            current, steps = queue.pop(0)
            if current == str1:
                return candidate
                
            if steps >= n:  # 防止无限循环
                break
                
            # 尝试所有可能的K值
            for k in range(len(current)):
                # 从第k个位置开始的子串添加到末尾
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
