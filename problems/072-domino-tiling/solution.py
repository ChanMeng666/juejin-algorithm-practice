def solution(num, data):
    # Convert the string to a list for modification
    dominoes = list(data)
    n = len(dominoes)

    # Record the net force at each position
    forces = [0] * n

    # Process the influence of R from left to right
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n
        elif dominoes[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] += force

    # Process the influence of L from right to left
    force = 0
    for i in range(n-1, -1, -1):
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] -= force

    # Find the positions of dominoes that remain standing
    standing = []
    for i in range(n):
        if forces[i] == 0 and dominoes[i] == '.':
            standing.append(i + 1)  # Convert to 1-based index

    # Format the output
    if not standing:
        return '0'
    return f'{len(standing)}:{",".join(map(str, standing))}'

if __name__ == "__main__":
    # Test cases
    print(solution(14, ".L.R...LR..L..") == "4:3,6,13,14")
    print(solution(5, "R....") == "0")
    print(solution(1, ".") == "1:1")
