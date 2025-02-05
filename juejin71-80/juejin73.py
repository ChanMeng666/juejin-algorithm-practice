def solution(num, data, input):
    # 存储所有匹配的结果
    matches = []
    
    # 遍历数据列表，查找所有以input开头的字符串
    for item in data:
        if item.startswith(input) and item != input:  # 排除完全相等的情况
            matches.append(item)
    
    # 单独处理完全匹配的情况
    if input in data:
        matches.append(input)
    
    # 如果没有找到匹配项，返回"-1"
    if not matches:
        return "-1"
    
    # 对匹配结果按字典序排序
    matches.sort()
    
    # 将结果用逗号连接成字符串
    return ",".join(matches)

if __name__ == "__main__":
    #  You can add more test cases here
    testData1 = ["select", "from", "where", "limit", "origin_log_db", "event_log_table", "user_id", "from_mobile"]

    print(solution(8, testData1, "f") == "from,from_mobile" )
    print(solution(8, testData1, "wh") == "where")
    print(solution(8, testData1, "z") == "-1")