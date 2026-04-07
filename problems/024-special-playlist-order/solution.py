def solution(n: int, a: list) -> list:
    # Create a deque to store the songs
    from collections import deque
    songs = deque(a)
    result = []

    while songs:
        # Play and remove the first song
        result.append(songs.popleft())

        # If the queue is not empty, move the first song to the end
        if songs:
            songs.append(songs.popleft())

    return result

if __name__ == '__main__':
    print(solution(n = 5, a = [5, 3, 2, 1, 4]) == [5, 2, 4, 1, 3])
    print(solution(n = 4, a = [4, 1, 3, 2]) == [4, 3, 1, 2])
    print(solution(n = 6, a = [1, 2, 3, 4, 5, 6]) == [1, 3, 5, 2, 6, 4])
