def solution(inputArray):
    if not inputArray:
        return 0
    
    # 按照区间起始位置排序
    intervals = sorted(inputArray, key=lambda x: x[0])
    
    # 合并重叠区间
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1] + 1:  # 如果当前区间与上一个区间重叠或相邻
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    # 计算所有区间内的数字总数
    total_points = 0
    for start, end in merged:
        total_points += end - start + 1
        
    return total_points

if __name__ == "__main__":
    #  You can add more test cases here
    testArray1 = [[1,4], [7, 10], [3, 5]]
    testArray2 = [[1,2], [6, 10], [11, 15]]
    testArray3 = [[1,3], [2, 6], [8, 10]]

    print(solution(testArray1) == 9)  # True
    print(solution(testArray2) == 12)  # True
    print(solution(testArray3) == 9)  # True