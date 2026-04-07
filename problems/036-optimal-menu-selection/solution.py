def solution(s: str, a: list, m: int, k: int) -> int:
    n = len(s)  # Total number of dishes

    # If the number of dishes to select exceeds the total, return -1
    if k > n:
        return -1

    # Combine dish information: each element is (price, contains_mushroom)
    dishes = [(a[i], int(s[i])) for i in range(n)]

    def get_min_price(curr_dishes, curr_k, curr_m):
        if curr_k == 0:  # Already selected k dishes
            return 0
        if len(curr_dishes) < curr_k:  # Not enough remaining dishes
            return float('inf')

        # Skip the first dish
        price1 = get_min_price(curr_dishes[1:], curr_k, curr_m)

        # Select the first dish
        price2 = float('inf')
        if curr_dishes[0][1] <= curr_m:  # If the mushroom limit allows
            next_price = get_min_price(curr_dishes[1:], curr_k - 1,
                                     curr_m - curr_dishes[0][1])
            if next_price != float('inf'):
                price2 = curr_dishes[0][0] + next_price

        return min(price1, price2)

    # Sort dishes by price to improve efficiency
    dishes.sort(key=lambda x: x[0])

    result = get_min_price(tuple(dishes), k, m)
    return result if result != float('inf') else -1

if __name__ == '__main__':
    print(solution("001", [10, 20, 30], 1, 2) == 30)
    print(solution("111", [10, 20, 30], 1, 2) == -1)
    print(solution("0101", [5, 15, 10, 20], 2, 3) == 30)
