def solution(m, w, p, n):
    # m: number of machines
    # w: number of workers
    # p: cost to purchase a machine or worker (in cakes)
    # n: target number of cakes

    days = 0
    total_cakes = 0

    while total_cakes < n:
        # If cakes produced so far plus today's production meets the target, return the day count
        if total_cakes + m * w >= n:
            return days + 1

        # Calculate today's cake production
        current_production = m * w

        # If accumulated cakes are not enough to buy any resource, keep producing
        if total_cakes + current_production < p:
            total_cakes += current_production
            days += 1
            continue

        # Calculate how many resources can be purchased
        resources_to_buy = (total_cakes + current_production) // p

        # Calculate remaining cakes after purchase
        total_cakes = (total_cakes + current_production) % p

        # Decide how to allocate resources
        # To maximize production efficiency, m and w should be as close as possible
        while resources_to_buy > 0:
            if m < w:
                m += 1
            else:
                w += 1
            resources_to_buy -= 1

        days += 1

    return days

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution(3, 1, 2, 12) == 3 )
    print(solution(10, 5, 30, 500) == 8 )
    print(solution(3, 5, 30, 320) == 14 )
