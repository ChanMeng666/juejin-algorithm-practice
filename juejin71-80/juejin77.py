def solution(n, k, array_a):
    def count_quality_chapters(left, right):
        # 计算指定区间内的优质章节数
        if right - left < 2:  # 区间长度小于3时没有优质章节
            return 0
        count = 0
        for i in range(left + 1, right):
            if array_a[i] > array_a[i-1] and array_a[i] > array_a[i+1]:
                count += 1
        return count
    
    best_quality = 0  # 最佳优质章节数
    best_left = 0     # 最佳左边界
    best_right = 0    # 最佳右边界
    min_sum = float('inf')  # 最小总字数
    
    # 遍历所有可能的区间
    for left in range(n):
        window_sum = 0
        for right in range(left, n):
            window_sum += array_a[right]
            if window_sum > k:  # 如果超过总字数限制，跳出内循环
                break
                
            quality_count = count_quality_chapters(left, right)
            
            # 更新最优解
            if quality_count > best_quality:
                best_quality = quality_count
                best_left = left
                best_right = right
                min_sum = window_sum
            elif quality_count == best_quality:
                if window_sum < min_sum:
                    best_left = left
                    best_right = right
                    min_sum = window_sum
                elif window_sum == min_sum and left < best_left:
                    best_left = left
                    best_right = right
    
    # 返回结果字符串
    return f"{best_quality},{best_left + 1},{best_right + 1}"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(8, 15000, [1000, 3000, 2000, 4000, 3000, 2000, 4000, 2000]) == "2,1,5" )
    print(solution(8, 15000, [2000, 5000, 2000, 1000, 4000, 2000, 4000, 3000]) == "2,4,8" )