def solution(n, template_, titles):
    def can_match(template, title):
        # 将模板按照 {} 分割
        parts = []
        i = 0
        fixed_parts = []
        while i < len(template):
            if template[i] == '{':
                start = i
                while i < len(template) and template[i] != '}':
                    i += 1
                if i < len(template):
                    parts.append(('wildcard', start))
                i += 1
            else:
                start = i
                while i < len(template) and template[i] != '{':
                    i += 1
                fixed_parts.append(template[start:i])
                parts.append(('fixed', len(fixed_parts) - 1))
        
        # 动态规划数组
        dp = [[False] * (len(title) + 1) for _ in range(len(parts) + 1)]
        dp[0][0] = True
        
        # 填充dp数组
        for i in range(1, len(parts) + 1):
            part_type, part_index = parts[i-1]
            
            if part_type == 'wildcard':
                # 通配符可以匹配任意字符
                for j in range(len(title) + 1):
                    if dp[i-1][j]:
                        for k in range(j, len(title) + 1):
                            dp[i][k] = True
            else:
                # 固定字符串必须精确匹配
                fixed_str = fixed_parts[part_index]
                for j in range(len(title)):
                    if dp[i-1][j]:
                        if j + len(fixed_str) <= len(title):
                            if title[j:j+len(fixed_str)] == fixed_str:
                                dp[i][j+len(fixed_str)] = True
        
        return dp[len(parts)][len(title)]

    # 处理每个标题
    results = []
    for title in titles:
        results.append(str(can_match(template_, title)))
    
    return ','.join(results)

if __name__ == "__main__":
    #  You can add more test cases here
    testTitles1 = ["adcdcefdfeffe", "adcdcefdfeff", "dcdcefdfeffe", "adcdcfe"]
    testTitles2 = ["CLSomGhcQNvFuzENTAMLCqxBdj", "CLSomNvFuXTASzENTAMLCqxBdj", "CLSomFuXTASzExBdj", "CLSoQNvFuMLCqxBdj", "SovFuXTASzENTAMLCq", "mGhcQNvFuXTASzENTAMLCqx"]
    testTitles3 = ["abcdefg", "abefg", "efg"]

    print(solution(4, "ad{xyz}cdc{y}f{x}e", testTitles1) == "True,False,False,True" )
    print(solution(6, "{xxx}h{cQ}N{vF}u{XTA}S{NTA}MLCq{yyy}", testTitles2) == "False,False,False,False,False,True" )
    print(solution(3, "a{bdc}efg", testTitles3) == "True,True,False" )