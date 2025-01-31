def solution(k, p, target):
    if not target:
        return 0
        
    # Convert to intervals and sort by right endpoint
    intervals = [(t[0], t[1]) for t in target]
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    pos = float('-inf')
    
    # Greedy: place line at rightmost point when needed
    for left, right in intervals:
        if left > pos:
            pos = right
            count += 1
            
    return count % p

if __name__ == "__main__":
    testTarget1 = [
        [10, 26, 3],
        [4, 8, 29],
        [1, 5, 8],
        [9, 9, 9]
    ]
    testTarget2 = [
        [10, 26, 3],
        [4, 8, 29],
        [1, 5, 8]
    ]
    testTarget3 = [
        [13, 20, 2],
        [15, 39, 3],
        [34, 89, 6],
        [2, 10, 1],
        [0, 87, 2],
        [23, 49, 3],
        [2, 45, 9],
        [9, 98, 0],
        [3, 12, 9],
        [35, 45, 21],
        [51, 67, 23],
        [37, 42, 54],
        [55, 76, 7],
        [2, 13, 6],
        [29, 31, 9],
        [10, 32, 1]
    ]

    print(solution(4, 100, testTarget1) == 3)
    print(solution(3, 100, testTarget2) == 2)
    print(solution(16, 100, testTarget3) == 5)