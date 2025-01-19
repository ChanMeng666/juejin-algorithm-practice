def solution(n: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # 复制输入数组，避免修改原数组
    nums = a.copy()
    steps = 0
    
    # 当还有非0数字时继续
    while any(nums):
        # 找到当前最大的数字
        max_num = max(nums)
        # 找到这个数字在数组中的位置
        max_idx = nums.index(max_num)
        
        # 删除最大数字的最高位
        str_num = str(max_num)
        if len(str_num) > 1:
            nums[max_idx] = int(str_num[1:])
        else:
            nums[max_idx] = 0
            
        steps += 1
    
    return steps

if __name__ == '__main__':
    print(solution(5, [10, 13, 22, 100, 30]) == 7)
    print(solution(3, [5, 50, 505]) == 4)
    print(solution(4, [1000, 1, 10, 100]) == 4)