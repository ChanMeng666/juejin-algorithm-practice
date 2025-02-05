def solution(plates: list[int], n: int) -> str:
    if not plates:
        return ""
    
    result = []
    start = end = plates[0]
    count = 1
    
    # 遍历所有数字找连续序列
    for i in range(1, len(plates)):
        if plates[i] == plates[i-1] + 1:
            end = plates[i]
            count += 1
        else:
            # 处理之前的序列
            if count >= 3:
                result.append(f"{start}-{end}")
            else:
                # 不足3个数的序列，单独添加每个数
                for j in range(start, end + 1):
                    result.append(str(j))
            # 重置计数
            start = end = plates[i]
            count = 1
    
    # 处理最后一个序列
    if count >= 3:
        result.append(f"{start}-{end}")
    else:
        for j in range(start, end + 1):
            result.append(str(j))
            
    return ",".join(result)


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], 10) == "-3--1,2,10,15,16,18-20" )
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], 20) == "-6,-3-1,3-5,7-11,14,15,17-20")
    print(solution([1, 2, 7, 8, 9, 10, 11, 19], 8) == "1,2,7-11,19")
