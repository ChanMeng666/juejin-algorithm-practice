def solution(n: int, a: list) -> str:
    def prime_factors(num):
        factors = []
        d = 2
        while num > 1:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
            if d * d > num:
                if num > 1:
                    factors.append(num)
                break
        return factors

    # Calculate the product of all elements
    product = 1
    for num in a:
        product *= num

    # Find all prime factors of the product
    all_factors = prime_factors(product)

    # Count unique prime factors
    unique_factors = set(all_factors)

    # Check if number of unique factors is less than or equal to n
    if len(unique_factors) <= n:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4]) == "Yes")
    print(solution(2, [10, 12]) == "No")
    print(solution(3, [6, 9, 15]) == "Yes")