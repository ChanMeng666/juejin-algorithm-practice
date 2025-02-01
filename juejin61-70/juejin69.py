def solution(nums, k):
    # 使用哈希表统计每个数字出现的频率
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # 创建桶，桶的索引表示频率，值为具有该频率的数字列表
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    # 从后向前遍历桶，收集前k个高频元素
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i]:
            # 对同一频率的数字进行排序
            buckets[i].sort()
            result.extend(buckets[i])
            if len(result) >= k:
                result = result[:k]
                break
    
    # 对结果进行排序并转换为字符串
    result.sort()
    return ','.join(map(str, result))

if __name__ == "__main__":
    # 测试用例
    print(solution([1,1,1,2,2,3], 2) == "1,2")
    print(solution([1], 1) == "1")
    print(solution([4,4,4,2,2,2,3,3,1], 2) == "2,4")