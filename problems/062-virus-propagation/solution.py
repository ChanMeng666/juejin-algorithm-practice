from collections import deque

def solution(row_n, column_m, seats, patient):
    if not seats or not seats[0]:
        return 0

    # Check if the patient position is valid
    if patient[0] < 0 or patient[0] >= row_n or patient[1] < 0 or patient[1] >= column_m:
        return 0

    # Initialize the distance array
    dist = [[float('inf')] * column_m for _ in range(row_n)]

    # Direction array: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Use a deque for BFS
    queue = deque()
    queue.append((patient[0], patient[1]))
    dist[patient[0]][patient[1]] = 0

    while queue:
        curr_row, curr_col = queue.popleft()
        curr_time = dist[curr_row][curr_col]

        for dx, dy in directions:
            new_row, new_col = curr_row + dx, curr_col + dy

            if 0 <= new_row < row_n and 0 <= new_col < column_m:
                # Calculate the time to reach the new position
                if seats[new_row][new_col] == 1:  # Wearing a mask
                    # Check if there are multiple infection sources
                    infected_count = 0
                    for dx2, dy2 in directions:
                        r2, c2 = new_row + dx2, new_col + dy2
                        if (0 <= r2 < row_n and 0 <= c2 < column_m and
                            dist[r2][c2] <= curr_time and (r2, c2) != (curr_row, curr_col)):
                            infected_count += 1

                    new_time = curr_time + (1 if infected_count >= 1 else 2)
                else:  # Not wearing a mask
                    new_time = curr_time + 1

                if new_time < dist[new_row][new_col]:
                    dist[new_row][new_col] = new_time
                    queue.append((new_row, new_col))

    # Find the maximum infection time and check if everyone is infected
    max_time = 0
    for i in range(row_n):
        for j in range(column_m):
            if dist[i][j] == float('inf'):
                return 0  # Someone was not infected
            max_time = max(max_time, dist[i][j])

    return max_time

if __name__ == "__main__":
    #  You can add more test cases here
    testSeats1 = [[0,1,1,1],[1,0,1,0],[1,1,1,1],[0,0,0,1]]
    testSeats2 = [[0,1,1,1],[1,0,1,0],[1,1,1,1],[0,0,0,1]]
    testSeats3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    testSeats4 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    testSeats5 = [[1]]

    print(solution(4, 4, testSeats1, [2, 2]) == 6 )
    print(solution(4, 4, testSeats2, [2, 5]) == 0 )
    print(solution(4, 4, testSeats3, [2, 2]) == 4 )
    print(solution(4, 4, testSeats4, [2, 2]) == 6 )
    print(solution(1, 1, testSeats5, [0, 0]) == 0 )
