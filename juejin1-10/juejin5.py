def solution(n, max, array):
    # 统计每个数字出现的次数
    count_dict = {}
    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # 找出所有可能的三张牌组合
    triples = []
    for num, count in count_dict.items():
        if count >= 3:
            triples.append(num)
    
    # 找出所有可能的对子组合
    pairs = []
    for num, count in count_dict.items():
        if count >= 2:
            pairs.append(num)
    
    # 如果没有足够的牌组成葫芦，返回[0, 0]
    if not triples or not pairs:
        return [0, 0]
    
    # 对triples和pairs按照牌面大小排序（考虑1是最大的）
    triples.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)
    pairs.sort(key=lambda x: (0 if x != 1 else 14, x), reverse=True)
    
    # 找出最大的合法葫芦组合
    result = [0, 0]
    for triple in triples:
        for pair in pairs:
            # 跳过使用同一个数字的情况
            if triple == pair:
                continue
            # 计算牌面总和
            total = triple * 3 + pair * 2
            # 检查是否超过最大值
            if total > max:
                continue
            # 如果找到合法组合，直接返回（因为我们已经按照大小排序）
            return [triple, pair]
    
    return [0, 0]


if __name__ == "__main__":
    # Add your test cases here
    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]) == [0, 0])
