def calculate_group_familiarity(group, familiar_matrix):
    # 计算一个小组内的熟悉度总和
    i, j, k = group
    return familiar_matrix[i][j] + familiar_matrix[j][k] + familiar_matrix[i][k]

def dfs(people, familiar_matrix, used, current_groups):
    n = len(people)
    if len(current_groups) * 3 == n:  # 所有人都已分组
        total_familiarity = sum(calculate_group_familiarity(group, familiar_matrix) 
                              for group in current_groups)
        return total_familiarity
    
    min_familiarity = float('inf')
    # 选择第一个未使用的人作为组长
    first = -1
    for i in range(n):
        if not used[i]:
            first = i
            break
    if first == -1:
        return float('inf')
    
    used[first] = True
    # 尝试不同的组合
    for j in range(first + 1, n):
        if used[j]:
            continue
        for k in range(j + 1, n):
            if used[k]:
                continue
            used[j] = used[k] = True
            current_groups.append((first, j, k))
            
            familiarity = dfs(people, familiar_matrix, used, current_groups)
            min_familiarity = min(min_familiarity, familiarity)
            
            current_groups.pop()
            used[j] = used[k] = False
    
    used[first] = False
    return min_familiarity

def solution(N, familiar_matrix):
    people = list(range(N))
    used = [False] * N
    return dfs(people, familiar_matrix, used, [])

if __name__ == "__main__":
    #  You can add more test cases here
    familiar_matrix1 = [[100, 78, 97], [78, 100, 55], [97, 55, 100]]
    familiar_matrix2 = [[100, 56, 19, 87, 38, 61],
       [56, 100, 70, 94, 88, 94],
       [19, 70, 100, 94, 43, 95],
       [87, 94, 94, 100, 85, 11],
       [38, 88, 43, 85, 100, 94],
       [61, 94, 95, 11, 94, 100]]

    print(solution(3, familiar_matrix1) == 230)
    print(solution(6, familiar_matrix2) == 299)