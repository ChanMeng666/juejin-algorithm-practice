def solution(airports):
    from collections import deque
    n = len(airports)

    # Use BFS to find the shortest path
    queue = deque([(0, 0)])  # (position, number of flights)
    visited = {0}  # Track visited positions

    while queue:
        pos, flights = queue.popleft()

        # If we reached the destination, return the number of flights needed
        if pos == n - 1:
            return flights

        # Try all possible next moves
        next_positions = set()

        # Add adjacent airports
        if pos + 1 < n:
            next_positions.add(pos + 1)
        if pos - 1 >= 0:
            next_positions.add(pos - 1)

        # Add other airports operated by the same airline
        for i in range(n):
            if airports[i] == airports[pos] and i != pos:
                next_positions.add(i)

        # Iterate through all possible next positions
        for next_pos in next_positions:
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, flights + 1))

    return -1  # If the destination is unreachable

if __name__ == "__main__":
    # Test cases
    print(solution([10,12,13,12,14]) == 3)  # True
    print(solution([10,11,12,13,14]) == 4)  # True
    print(solution([7,7,7,8,9,7]) == 1)     # True
