def solution(nodes):
    if not nodes:
        return 0

    n = len(nodes)
    # Track the status of each node: -1 = uncovered, 0 = covered, 1 = heater placed
    status = [-1 if node == 1 else 0 for node in nodes]
    heaters = 0

    def warm_nodes(pos):
        # Heater covers the parent node
        if pos > 0:
            parent = (pos - 1) // 2
            if status[parent] == -1:
                status[parent] = 0

        # Heater covers the current node
        status[pos] = 1

        # Heater covers child nodes
        left = 2 * pos + 1
        right = 2 * pos + 2
        if left < n and status[left] == -1:
            status[left] = 0
        if right < n and status[right] == -1:
            status[right] = 0

    # Traverse nodes from bottom to top
    for i in range(n-1, -1, -1):
        if nodes[i] == 1 and status[i] == -1:
            # If the current node is uncovered, place a heater here
            warm_nodes(i)
            heaters += 1

    return heaters

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 1, 0, 1, 1]) == 1)
    print(solution([1,0,1,1,0,1,0,1,0,1,0,0,1,1]) == 3)
    print(solution([1,1,0,0,1,1,0,0,1,0,1,1,0,0,1]) == 3)
