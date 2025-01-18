def solution(nodes, decorations, tree):
    # 获取礼物信息和边
    gifts = tree[0]  # 节点上的礼物类型列表
    edges = tree[1:]  # 边的列表
    
    # 构建邻接表表示的树
    graph = [[] for _ in range(nodes + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    def dfs(node, parent, cut_set):
        """深度优先搜索处理每个节点"""
        # 获取当前节点的子节点
        children = [child for child in graph[node] if child != parent]
        
        # 如果是叶子节点，返回礼物类型集合
        if not children:
            gift_type = set()
            if gifts[node-1] != 0:
                gift_type.add(gifts[node-1])
            return 1, gift_type
        
        # 处理所有子节点
        total_ways = 1
        MOD = 998244353
        node_gift_types = set()
        if gifts[node-1] != 0:
            node_gift_types.add(gifts[node-1])
            
        for child in children:
            child_ways, child_types = dfs(child, node, cut_set)
            
            # 如果需要切割（礼物类型冲突）
            if child_types and node_gift_types and not child_types.issubset(node_gift_types):
                if len(cut_set) < decorations - 1:
                    cut_set.add((node, child))
                    total_ways = (total_ways * child_ways) % MOD
                else:
                    return 0, set()
            else:
                # 不需要切割，合并礼物类型
                node_gift_types.update(child_types)
                if len(node_gift_types) > 1:
                    if len(cut_set) < decorations - 1:
                        cut_set.add((node, child))
                        total_ways = (total_ways * child_ways) % MOD
                    else:
                        return 0, set()
                else:
                    total_ways = (total_ways * child_ways) % MOD
        
        return total_ways, node_gift_types
    
    # 如果礼物种类比要求的分块数多，无法划分
    if len(set(g for g in gifts if g != 0)) > decorations:
        return 0
        
    # 从根节点开始DFS
    cut_set = set()
    result, _ = dfs(1, 0, cut_set)
    
    # 检查分块数是否正确
    if len(cut_set) == decorations - 1:
        return result
    return 0