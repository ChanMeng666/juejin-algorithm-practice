def get_prime_factors_with_count(n: int) -> dict:
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def solution(n: int, a: list) -> str:
    # 获取所有数的素因子及其次数
    numbers_factors = []
    total_prime_counts = {}
    
    for num in a:
        if num == 1:
            numbers_factors.append({})
            continue
        factors = get_prime_factors_with_count(num)
        numbers_factors.append(factors)
        
        # 统计每个素数出现的总次数
        for prime, count in factors.items():
            total_prime_counts[prime] = total_prime_counts.get(prime, 0) + count
    
    # 检查每个数的素因子情况
    for i, factors in enumerate(numbers_factors):
        if len(factors) <= 1:  # 如果数字已经只包含一种或没有素因子，跳过
            continue
            
        # 如果一个数有多个素因子，检查是否有其他数可以接收这些素因子
        # 同时要确保其他数没有被占用
        available_numbers = n - 1  # 除了当前数之外的数的数量
        needed_receivers = len(factors) - 1  # 需要转移的素因子数量
        
        # 如果需要的接收者数量大于可用的数的数量，返回 "No"
        if needed_receivers > available_numbers:
            return "No"
            
        # 检查其他数是否已经包含素因子
        available_receivers = 0
        for j, other_factors in enumerate(numbers_factors):
            if i != j and len(other_factors) <= 1:
                available_receivers += 1
                
        if available_receivers < needed_receivers:
            return "No"
    
    return "Yes"

if __name__ == '__main__':
    print(solution(4, [1, 2, 3, 4]) == "Yes")
    print(solution(2, [10, 12]) == "No")
    print(solution(3, [6, 9, 15]) == "Yes")
    print(solution(2, [14, 3]) == "No")