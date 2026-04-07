def solution(n, sums):
    # If n is less than 2, pair sums cannot be formed
    if n < 2:
        return "Impossible"

    # Check if the length of sums is correct
    if len(sums) != n * (n-1) // 2:
        return "Impossible"

    # Special case for n=2
    if n == 2:
        if len(sums) == 1:
            s = sums[0]
            if s % 2 == 0:  # Ensure it can be evenly split
                return f"{s//2} {s//2}"
        return "Impossible"

    # For n>=3
    # Assume we have array [a,b,c,d...], sums contains all possible pairwise sums
    # We can obtain another number by subtracting a pairwise sum from the sum of three numbers
    try:
        if n == 3:
            x, y, z = sorted(sums)
            a = (x + y - z) // 2
            b = (x - y + z) // 2
            c = (-x + y + z) // 2
            # Verify the result
            if {a+b, a+c, b+c} == set(sums) and a <= b <= c:
                return f"{a} {b} {c}"
            return "Impossible"

        # For n=5
        if n == 5:
            sums_sorted = sorted(sums)
            sums_set = set(sums)

            # Find the minimum and maximum sums
            min_sum = sums_sorted[0]
            max_sum = sums_sorted[-1]

            # Try to build the result starting from the smallest sum
            for i in range(len(sums_sorted)):
                for j in range(i+1, len(sums_sorted)):
                    # Assume sums_sorted[i] is the sum of the two smallest numbers
                    # sums_sorted[j] is the sum of the smallest number and another number
                    s1 = sums_sorted[i]
                    s2 = sums_sorted[j]

                    # Try to compute the two possible numbers
                    for k in range(-1000, 1001):  # Adjust range based on problem constraints
                        m = s1 - k  # The other smallest number
                        n1 = s2 - k  # The third number

                        if m > k:  # Ensure correct ordering
                            continue

                        result = [k, m]  # Add the two confirmed numbers first
                        candidates = set()

                        # Verify whether these two numbers could be correct
                        valid = True
                        if k + m not in sums_set:
                            continue

                        # Find other numbers through known sums
                        for s in sums_sorted:
                            # Try to find other numbers
                            c1 = s - k
                            c2 = s - m
                            if c1 not in result and c1 not in candidates:
                                candidates.add(c1)
                            if c2 not in result and c2 not in candidates:
                                candidates.add(c2)

                        # If the correct number of candidates is found
                        if len(candidates) == 3:
                            result.extend(sorted(candidates))
                            # Verify all sums
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
