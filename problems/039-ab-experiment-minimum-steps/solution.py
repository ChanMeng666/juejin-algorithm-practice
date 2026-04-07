def solution(x_position, y_position):
    # If the start equals the destination, no movement is needed
    if x_position == y_position:
        return 0

    # Calculate the total distance to move
    distance = abs(y_position - x_position)

    # If the distance is 1, only 1 step is needed
    if distance == 1:
        return 1

    # If the distance is 2, 2 steps are needed
    if distance == 2:
        return 2

    # For longer distances, we need to consider acceleration and deceleration
    # Initial step size is 1
    steps = 3  # Minimum 3 steps needed
    current_max = 2  # Excluding first and last step of size 1, max middle step starts at 2
    total = 4  # Distance already coverable (1 + 2 + 1 = 4)

    # If the target is already reachable, return the current step count
    if total >= distance:
        return steps

    # Keep increasing steps until the target is reachable
    while total < distance:
        steps += 1
        # Every two additional steps, the max step size can increase by 1
        if steps % 2 == 1:
            current_max += 1
        total += current_max

    return steps

if __name__ == "__main__":
    # Test cases
    print(solution(12, 6) == 4)  # True
    print(solution(34, 45) == 6)  # True
    print(solution(50, 30) == 8)  # True
    print(solution(0, 0) == 0)  # True
