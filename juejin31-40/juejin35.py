def solution(a, b):
    # 创建两个集合用于存储数字
    set_a = set(a)
    set_b = set(b)
    
    # 找出两个集合的交集
    intersection = set_a & set_b
    
    # 将交集转换为列表并按从大到小排序
    result = sorted(list(intersection), reverse=True)
    
    return result

if __name__ == '__main__':
    print(solution([1, 2, 3, 7], [2, 5, 7]) == [7, 2])
    print(solution([1, 4, 8, 10], [2, 4, 8, 10]) == [10, 8, 4])
    print(solution([3, 5, 9], [1, 4, 6]) == [])
    print(solution([1, 2, 3], [1, 2, 3]) == [3, 2, 1])