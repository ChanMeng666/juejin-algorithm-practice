# Tree Gift Decoration

## Problem Description

Given a tree with `nodes` nodes, each node may have a gift type (or 0 for no gift). The task is to partition the tree into exactly `decorations` connected components by cutting edges, such that each component contains at most one distinct gift type. Return the number of valid ways to partition the tree. If no valid partition exists, return 0.

### Requirements

- The tree must be split into exactly `decorations` connected components by removing `decorations - 1` edges.
- Each resulting component can contain only one type of gift (nodes with gift type 0 are considered empty and compatible with any type).
- Results should be computed modulo 998244353.

### Constraints

- The tree is represented as an adjacency list built from edge pairs.
- Node indices are 1-based.
- Gift types are given as a list where index corresponds to node number.

## Examples

```
Input: nodes=5, decorations=2, tree=[[1,2,1,2,0], [1,2], [2,3], [3,4], [4,5]]
The tree has gifts of type 1 and 2, and must be split into 2 components.
```

## Solution Approach

1. **Build the Tree**: Construct an adjacency list from the edge information.
2. **DFS Traversal**: Perform a depth-first search from the root node (node 1).
3. **Gift Type Tracking**: At each node, track the set of gift types in its subtree.
4. **Edge Cutting Decision**: When merging a child's gift types with the parent's would create a conflict (more than one distinct type), cut the edge between them.
5. **Validation**: After DFS, verify that the number of cuts equals `decorations - 1`. If the number of distinct gift types exceeds the number of partitions, return 0 immediately.

## Implementation

```python
def solution(nodes, decorations, tree):
    gifts = tree[0]
    edges = tree[1:]

    graph = [[] for _ in range(nodes + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, cut_set):
        children = [child for child in graph[node] if child != parent]

        if not children:
            gift_type = set()
            if gifts[node-1] != 0:
                gift_type.add(gifts[node-1])
            return 1, gift_type

        total_ways = 1
        MOD = 998244353
        node_gift_types = set()
        if gifts[node-1] != 0:
            node_gift_types.add(gifts[node-1])

        for child in children:
            child_ways, child_types = dfs(child, node, cut_set)

            if child_types and node_gift_types and not child_types.issubset(node_gift_types):
                if len(cut_set) < decorations - 1:
                    cut_set.add((node, child))
                    total_ways = (total_ways * child_ways) % MOD
                else:
                    return 0, set()
            else:
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

    if len(set(g for g in gifts if g != 0)) > decorations:
        return 0

    cut_set = set()
    result, _ = dfs(1, 0, cut_set)

    if len(cut_set) == decorations - 1:
        return result
    return 0
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the number of nodes. Each node is visited once during DFS.
- **Space Complexity**: O(n), for the adjacency list, recursion stack, and gift type sets.

## Summary

This problem uses DFS on a tree to determine where edges should be cut so that each resulting component has a uniform gift type. The algorithm greedily cuts edges when merging subtrees would introduce gift type conflicts, and validates that exactly the right number of cuts are made.
