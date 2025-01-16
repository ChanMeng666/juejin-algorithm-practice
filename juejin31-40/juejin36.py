def solution(s: str, a: list, m: int, k: int) -> int:
    n = len(s)  # 总菜品数
    
    # 如果需要选择的菜品数量大于总菜品数，返回-1
    if k > n:
        return -1
    
    # 将菜品信息整合到一起，每个元素为(价格, 是否含蘑菇)
    dishes = [(a[i], int(s[i])) for i in range(n)]
    
    def get_min_price(curr_dishes, curr_k, curr_m):
        if curr_k == 0:  # 已选够k个菜
            return 0
        if len(curr_dishes) < curr_k:  # 剩余菜品不够选
            return float('inf')
            
        # 不选第一个菜
        price1 = get_min_price(curr_dishes[1:], curr_k, curr_m)
        
        # 选第一个菜
        price2 = float('inf')
        if curr_dishes[0][1] <= curr_m:  # 如果蘑菇数量允许
            next_price = get_min_price(curr_dishes[1:], curr_k - 1, 
                                     curr_m - curr_dishes[0][1])
            if next_price != float('inf'):
                price2 = curr_dishes[0][0] + next_price
                
        return min(price1, price2)
    
    # 对菜品按价格排序，这样可以提高效率
    dishes.sort(key=lambda x: x[0])
    
    result = get_min_price(tuple(dishes), k, m)
    return result if result != float('inf') else -1

if __name__ == '__main__':
    print(solution("001", [10, 20, 30], 1, 2) == 30)
    print(solution("111", [10, 20, 30], 1, 2) == -1)
    print(solution("0101", [5, 15, 10, 20], 2, 3) == 30)