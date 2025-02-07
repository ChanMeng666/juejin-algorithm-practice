def solution(nodes):
    if not nodes:
        return 0
        
    n = len(nodes)
    # 记录每个节点的状态：-1表示未覆盖，0表示被覆盖，1表示放置了暖炉
    status = [-1 if node == 1 else 0 for node in nodes]
    heaters = 0
    
    def warm_nodes(pos):
        # 暖炉覆盖父节点
        if pos > 0:
            parent = (pos - 1) // 2
            if status[parent] == -1:
                status[parent] = 0
                
        # 暖炉覆盖当前节点
        status[pos] = 1
        
        # 暖炉覆盖子节点
        left = 2 * pos + 1
        right = 2 * pos + 2
        if left < n and status[left] == -1:
            status[left] = 0
        if right < n and status[right] == -1:
            status[right] = 0
    
    # 从下往上遍历节点
    for i in range(n-1, -1, -1):
        if nodes[i] == 1 and status[i] == -1:
            # 如果当前节点未被覆盖，则在此放置暖炉
            warm_nodes(i)
            heaters += 1
            
    return heaters

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([1, 1, 0, 1, 1]) == 1)
    print(solution([1,0,1,1,0,1,0,1,0,1,0,0,1,1]) == 3)
    print(solution([1,1,0,0,1,1,0,0,1,0,1,1,0,0,1]) == 3)
