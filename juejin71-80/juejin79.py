def kadane(arr):
    # 计算最大子数组和
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def solution(N, data_array):
    # 首先计算不翻转情况下的最大子数组和
    original_max = kadane(data_array)
    
    # 如果数组长度小于2，直接返回原始最大值
    if N < 2:
        return original_max
    
    result = original_max
    
    # 对于每个可能的子数组，尝试翻转并计算最大子数组和
    for i in range(N):
        for j in range(i + 1, N):
            # 创建翻转后的数组副本
            flipped = data_array.copy()
            # 翻转子数组
            flipped[i:j+1] = flipped[i:j+1][::-1]
            # 计算翻转后的最大子数组和
            current_max = kadane(flipped)
            result = max(result, current_max)
    
    return result

if __name__ == "__main__":
    #  You can add more test cases here
    array1 = [-85, -11, 92, 6, 49, -76, 28, -16, 3, -29, 26, 37, 86, 3, 25, -43, -36, -27, 45, 87, 91, 58, -15, 91, 5, 99, 40, 68, 54, -95, 66, 49, 74, 9, 24, -84, 12, -23, -92, -47, 5, 91, -79, 94, 61, -54, -71, -36, 31, 97, 64, -14, -16, 48, -79, -70, 54, -94, 48, 37, 47, -58, 6, 62, 19, 8, 32, 65, -81, -27, 14, -18, -34, -64, -97, -21, -76, 51, 0, -79, -22, -78, -95, -90, 4, 82, -79, -85, -64, -79, 63, 49, 21, 97, 47, 16, 61, -46, 54, 44]
    print(solution(5, [1,2,3,-1,4]) == 10 )
    print(solution(100, array1) == 1348)