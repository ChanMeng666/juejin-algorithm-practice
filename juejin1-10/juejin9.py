def solution(n: int, m: int, s: str, c: str) -> int:
    # 将商品列表转换为列表以便操作
    items = list(s)
    
    # 统计每个顾客想要购买的商品数量
    customer_wants = {}
    for char in c:
        customer_wants[char] = customer_wants.get(char, 0) + 1
    
    # 统计货架上每种商品的数量
    shelf_items = {}
    for char in s:
        shelf_items[char] = shelf_items.get(char, 0) + 1
    
    # 根据顾客需求对商品进行排序
    # 优先放置更多顾客想要的商品
    items.sort(key=lambda x: (-customer_wants.get(x, 0), x))
    
    # 模拟顾客购买过程
    sold = 0
    used_positions = set()
    
    for customer_item in c:
        found = False
        # 遍历所有位置
        for pos in range(n):
            if pos in used_positions:
                continue
            if items[pos] == customer_item:
                sold += 1
                used_positions.add(pos)
                found = True
                break
            # 如果遇到空格子，顾客离开
            if items[pos] == ' ':
                break
        # 如果没找到想要的商品，继续下一个顾客
        if not found:
            continue
            
    return sold

if __name__ == '__main__':
    print(solution(3, 4, "abc", "abcd") == 3)
    print(solution(4, 2, "abbc", "bb") == 2)
    print(solution(5, 4, "bcdea", "abcd") == 4)