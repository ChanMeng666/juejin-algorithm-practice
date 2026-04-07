def solution(stones: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # Convert stone positions to a set for efficient lookup and removal
    stone_positions = set(stones)
    moves = 0

    while True:
        # Find the current minimum and maximum positions
        min_pos = min(stone_positions)
        max_pos = max(stone_positions)

        # Try to move an endpoint
        moved = False

        # Check if the minimum endpoint can be moved
        for pos in range(min_pos + 1, max_pos):
            if pos not in stone_positions:
                stone_positions.remove(min_pos)
                stone_positions.add(pos)
                moves += 1
                moved = True
                break

        if not moved:
            # If the minimum endpoint cannot be moved, check the maximum endpoint
            for pos in range(max_pos - 1, min_pos, -1):
                if pos not in stone_positions:
                    stone_positions.remove(max_pos)
                    stone_positions.add(pos)
                    moves += 1
                    moved = True
                    break

        if not moved:
            break

    return moves

if __name__ == '__main__':
    print(solution(stones=[7, 4, 9]) == 2)
    print(solution(stones=[6, 5, 4, 3, 10]) == 3)
    print(solution(stones=[1, 2, 3, 4, 5]) == 0)
