def solution(nodes, decorations, tree):
    # Get gift information and edges
    gifts = tree[0]  # List of gift types on nodes
    edges = tree[1:]  # List of edges

    # Build an adjacency list representation of the tree
    graph = [[] for _ in range(nodes + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, cut_set):
        """Depth-first search to process each node"""
        # Get children of the current node
        children = [child for child in graph[node] if child != parent]

        # If it is a leaf node, return the gift type set
        if not children:
            gift_type = set()
            if gifts[node-1] != 0:
                gift_type.add(gifts[node-1])
            return 1, gift_type

        # Process all child nodes
        total_ways = 1
        MOD = 998244353
        node_gift_types = set()
        if gifts[node-1] != 0:
            node_gift_types.add(gifts[node-1])

        for child in children:
            child_ways, child_types = dfs(child, node, cut_set)

            # If a cut is needed (gift type conflict)
            if child_types and node_gift_types and not child_types.issubset(node_gift_types):
                if len(cut_set) < decorations - 1:
                    cut_set.add((node, child))
                    total_ways = (total_ways * child_ways) % MOD
                else:
                    return 0, set()
            else:
                # No cut needed, merge gift types
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

    # If the number of gift types exceeds the required number of partitions, partitioning is impossible
    if len(set(g for g in gifts if g != 0)) > decorations:
        return 0

    # Start DFS from the root node
    cut_set = set()
    result, _ = dfs(1, 0, cut_set)

    # Check if the number of partitions is correct
    if len(cut_set) == decorations - 1:
        return result
    return 0
