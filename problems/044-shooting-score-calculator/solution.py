def solution(x: int, y: int) -> int:
    # Calculate the distance from the shooting point to the bullseye
    distance = (x * x + y * y) ** 0.5

    # If the distance exceeds 10, it is outside all rings, score is 0
    if distance > 10:
        return 0

    # Round up to get the ring number, then subtract from 11 to get the score
    ring = int(distance) + (1 if distance > int(distance) else 0)
    return 11 - ring

if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)
