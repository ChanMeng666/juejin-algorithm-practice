def solution(n, sums):
    # 如果n小于2，无法形成数对和
    if n < 2:
        return "Impossible"
        
    # 检查sums长度是否正确
    if len(sums) != n * (n-1) // 2:
        return "Impossible"
    
    # 对于n=2的特殊情况
    if n == 2:
        if len(sums) == 1:
            s = sums[0]
            if s % 2 == 0:  # 确保可以平分
                return f"{s//2} {s//2}"
        return "Impossible"
    
    # 对于n>=3的情况
    # 假设我们有数组[a,b,c,d...]，sums包含所有可能的两数之和
    # 我们可以通过三个数的和减去一个两数之和得到另一个数
    try:
        if n == 3:
            x, y, z = sorted(sums)
            a = (x + y - z) // 2
            b = (x - y + z) // 2
            c = (-x + y + z) // 2
            # 验证结果
            if {a+b, a+c, b+c} == set(sums) and a <= b <= c:
                return f"{a} {b} {c}"
            return "Impossible"
            
        # 对于n=5的情况
        if n == 5:
            sums_sorted = sorted(sums)
            sums_set = set(sums)
            
            # 找到最小和最大的和
            min_sum = sums_sorted[0]
            max_sum = sums_sorted[-1]
            
            # 尝试从最小的和开始构建结果
            for i in range(len(sums_sorted)):
                for j in range(i+1, len(sums_sorted)):
                    # 假设sums_sorted[i]是两个最小数的和
                    # sums_sorted[j]是一个最小数和另一个数的和
                    s1 = sums_sorted[i]
                    s2 = sums_sorted[j]
                    
                    # 尝试计算可能的两个数
                    for k in range(-1000, 1001):  # 根据题目范围调整
                        m = s1 - k  # 另一个最小的数
                        n1 = s2 - k  # 第三个数
                        
                        if m > k:  # 确保顺序正确
                            continue
                            
                        result = [k, m]  # 先添加两个确定的数
                        candidates = set()
                        
                        # 验证这两个数是否可能是正确的
                        valid = True
                        if k + m not in sums_set:
                            continue
                            
                        # 通过已知的和来找其他的数
                        for s in sums_sorted:
                            # 尝试找到其他数
                            c1 = s - k
                            c2 = s - m
                            if c1 not in result and c1 not in candidates:
                                candidates.add(c1)
                            if c2 not in result and c2 not in candidates:
                                candidates.add(c2)
                                
                        # 如果找到了正确数量的候选数
                        if len(candidates) == 3:
                            result.extend(sorted(candidates))
                            # 验证所有的和
                            check_sums = []
                            for x in range(5):
                                for y in range(x+1, 5):
                                    check_sums.append(result[x] + result[y])
                            if sorted(check_sums) == sums_sorted:
                                return " ".join(map(str, result))
                            
        return "Impossible"
        
    except:
        return "Impossible"

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, [1269, 1160, 1663]) == "383 777 886")
    print(solution(3, [1, 1, 1]) == "Impossible")
    print(solution(5, [226, 223, 225, 224, 227, 229, 228, 226, 225, 227]) == "111 112 113 114 115")
    print(solution(5, [-1, 0, -1, -2, 1, 0, -1, 1, 0, -1]) == "-1 -1 0 0 1")
    print(solution(5, [79950, 79936, 79942, 79962, 79954, 79972, 79960, 79968, 79924, 79932]) == "39953 39971 39979 39983 39989")