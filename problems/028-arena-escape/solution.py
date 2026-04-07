def solution(N, M, data):
    # Find the exit position
    exit_pos = None
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'O':
                exit_pos = (i, j)
                break
        if exit_pos:
            break

    # Check if a position is within the map boundaries
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M

    # Get the next positions reachable from a given position
    def get_next_positions(x, y):
        positions = []
        curr = data[x][y]

        # If it's a teleporter, can only reach the teleport destination
        if curr == 'U' and is_valid(x-1, y):
            positions.append((x-1, y))
        elif curr == 'D' and is_valid(x+1, y):
            positions.append((x+1, y))
        elif curr == 'L' and is_valid(x, y-1):
            positions.append((x, y-1))
        elif curr == 'R' and is_valid(x, y+1):
            positions.append((x, y+1))
        # If it's a normal floor or exit, can move in all four directions
        elif curr in '.O':
            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if is_valid(nx, ny):
                    positions.append((nx, ny))

        return positions

    # Get positions that can reach a given position in reverse
    def get_prev_positions(x, y):
        positions = []
        # Check all four directions
        for px, py in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if not is_valid(px, py):
                continue
            # Check if that position can reach the current position
            curr = data[px][py]
            if curr == 'U' and x == px-1:
                positions.append((px, py))
            elif curr == 'D' and x == px+1:
                positions.append((px, py))
            elif curr == 'L' and y == py-1:
                positions.append((px, py))
            elif curr == 'R' and y == py+1:
                positions.append((px, py))
            elif curr in '.O':
                positions.append((px, py))
        return positions

    # Use BFS to find all positions that can reach the exit
    safe_positions = set()
    queue = [exit_pos]
    safe_positions.add(exit_pos)

    while queue:
        curr_x, curr_y = queue.pop(0)
        # Get all predecessor positions that can reach the current position
        prev_positions = get_prev_positions(curr_x, curr_y)
        for px, py in prev_positions:
            if (px, py) not in safe_positions:
                safe_positions.add((px, py))
                queue.append((px, py))

    # Calculate the number of dangerous positions
    danger_count = N * M - len(safe_positions)
    return danger_count

if __name__ == "__main__":
    # Test cases
    pattern = [
        [".",  ".", ".", ".", "."],
        [".",  "R", "R", "D", "."],
        [".", "U", ".", "D", "R"],
        [".", "U", "L", "L", "."],
        [".", ".", ".", ".", "O"]
    ]
    print(solution(5, 5, pattern) == 10)

    pattern2 = [[".", "R", ".", "O"],
                ["U", ".", "L", "."],
                [".", "D", ".", "."],
                [".", ".", "R", "D"]]
    print(solution(4, 4, pattern2) == 2)

    pattern3 = [[".", "U", "O"],
                ["L", ".", "R"],
                ["D", ".", "."]]
    print(solution(3, 3, pattern3) == 8)
