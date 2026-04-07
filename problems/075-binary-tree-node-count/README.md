# Binary Tree Node Count

## Problem Description

Given a binary tree represented as an array, where `1` indicates an existing node and `0` indicates no node at that position, determine the minimum number of heaters needed so that every existing node is covered. A heater placed at a node covers:
- The node itself
- Its parent node
- Its left and right child nodes

### Requirements

- Input: `nodes` - a list of integers (0 or 1) representing a binary tree in level-order (array representation)
- Output: the minimum number of heaters needed to cover all existing nodes (nodes with value 1)

### Constraints

- A heater covers the node it is placed on, its parent, and its children
- Only existing nodes (value 1) need to be covered
- Nodes with value 0 do not need coverage

## Examples

```
Input: [1, 1, 0, 1, 1]
Output: 1
Explanation: Place a heater at index 1 to cover nodes at indices 0, 1, 3, and 4.

Input: [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
Output: 3

Input: [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]
Output: 3
```

## Solution Approach

This problem uses a greedy algorithm with bottom-up traversal:

1. **Status Tracking**: Each node has a status:
   - `-1`: uncovered (exists but not yet warmed)
   - `0`: covered (either does not exist, or already warmed by a nearby heater)
   - `1`: a heater is placed here

2. **Bottom-Up Greedy**: Traverse the tree from the last node to the root. If an existing node is still uncovered, place a heater there. This greedy choice ensures coverage propagates upward efficiently.

3. **Coverage Propagation**: When a heater is placed at position `pos`:
   - The parent at `(pos - 1) // 2` is covered
   - The current node is marked as having a heater
   - Left child at `2 * pos + 1` and right child at `2 * pos + 2` are covered

## Implementation

```python
def solution(nodes):
    if not nodes:
        return 0
        
    n = len(nodes)
    status = [-1 if node == 1 else 0 for node in nodes]
    heaters = 0
    
    def warm_nodes(pos):
        if pos > 0:
            parent = (pos - 1) // 2
            if status[parent] == -1:
                status[parent] = 0
        status[pos] = 1
        left = 2 * pos + 1
        right = 2 * pos + 2
        if left < n and status[left] == -1:
            status[left] = 0
        if right < n and status[right] == -1:
            status[right] = 0
    
    for i in range(n-1, -1, -1):
        if nodes[i] == 1 and status[i] == -1:
            warm_nodes(i)
            heaters += 1
            
    return heaters
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the nodes array. Each node is visited once.
- **Space Complexity**: O(n), for the status array.

## Summary

This problem applies a greedy strategy on a binary tree represented as an array. By traversing from bottom to top and placing heaters only when a node is uncovered, we ensure the minimum number of heaters. The key insight is that handling leaf-level nodes first forces optimal placement decisions that propagate coverage upward through the tree.
