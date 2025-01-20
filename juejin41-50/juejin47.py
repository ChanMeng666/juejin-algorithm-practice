def solution(n: int, l: int, r: int, a: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # 统计完美偶数的个数
    count = 0
    
    # 遍历数组中的每个数
    for num in a:
        # 检查是否满足完美偶数的两个条件：
        # 1. 是偶数 (num % 2 == 0)
        # 2. 在区间[l, r]之间 (l <= num <= r)
        if num % 2 == 0 and l <= num <= r:
            count += 1
            
    return count

if __name__ == '__main__':
    print(solution(5, 3, 8, [1, 2, 6, 8, 7]) == 2)
    print(solution(4, 10, 20, [12, 15, 18, 9]) == 2)
    print(solution(3, 1, 10, [2, 4, 6]) == 3)