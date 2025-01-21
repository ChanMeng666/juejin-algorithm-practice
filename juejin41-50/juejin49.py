def solution(n: int, s: list, x: list) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # 创建一个包含索引、名字和金额的列表
    data = list(zip(range(n), s, x))
    
    # 按照金额降序排序，金额相同时按抢红包顺序（索引）升序
    sorted_data = sorted(data, key=lambda x: (-x[2], x[0]))
    
    # 返回排序后的名字列表
    result = [name for _, name, _ in sorted_data]
    
    return result

if __name__ == '__main__':
    print(solution(4, ["a", "b", "c", "d"], [1, 2, 2, 1]) == ['b', 'c', 'a', 'd'])
    print(solution(3, ["x", "y", "z"], [100, 200, 200]) == ['y', 'z', 'x'])
    print(solution(5, ["m", "n", "o", "p", "q"], [50, 50, 30, 30, 20]) == ['m', 'n', 'o', 'p', 'q'])