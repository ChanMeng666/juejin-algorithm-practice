def solution(n: int, m: int, s: str, c: str) -> int:
    # Convert the product list to a list for manipulation
    items = list(s)

    # Count the quantity of products each customer wants to buy
    customer_wants = {}
    for char in c:
        customer_wants[char] = customer_wants.get(char, 0) + 1

    # Count the quantity of each product on the shelf
    shelf_items = {}
    for char in s:
        shelf_items[char] = shelf_items.get(char, 0) + 1

    # Sort products based on customer demand
    # Prioritize products that more customers want
    items.sort(key=lambda x: (-customer_wants.get(x, 0), x))

    # Simulate the customer purchasing process
    sold = 0
    used_positions = set()

    for customer_item in c:
        found = False
        # Iterate through all positions
        for pos in range(n):
            if pos in used_positions:
                continue
            if items[pos] == customer_item:
                sold += 1
                used_positions.add(pos)
                found = True
                break
            # If an empty slot is encountered, the customer leaves
            if items[pos] == ' ':
                break
        # If the desired product was not found, move to the next customer
        if not found:
            continue

    return sold

if __name__ == '__main__':
    print(solution(3, 4, "abc", "abcd") == 3)
    print(solution(4, 2, "abbc", "bb") == 2)
    print(solution(5, 4, "bcdea", "abcd") == 4)
