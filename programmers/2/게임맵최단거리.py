# from collections import deque
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def solution(maps):
#     n = (len(maps[0]))
#     m = (len(maps))
#
#     visited = [[0] * n for i in range(m)]
#     lst = [[0] * n for i in range(m)]
#     q = deque()
#     q.append((0, 0))
#     answer = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
#                 q.append((nx, ny))
#                 visited[nx][ny] = 1
#                 lst[nx][ny] = lst[x][y] + 1
#
#     if lst[m - 1][n - 1] == 0:
#         answer = -1
#     else:
#         answer = lst[m - 1][n - 1] + 1
#     return answer

from collections import deque


def solution(maps):
    answer = []
    n = len(maps[0])
    m = len(maps)
    visited = [[0] * n for i in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append([0, 0, 0])

    while q:
        print(q)
        a, b, c = q.popleft()

        for k in range(4):

            nx = a + dx[k]
            ny = b + dy[k]
            if a == 0 and b == 4:
                print("nx", nx, "ny", ny,"c",c)
                print(visited[nx][ny])
            if 0 <= nx < m and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append([nx, ny, c + 1])
                visited[nx][ny] = 1
        if a == n - 1 and b == m - 1:
            answer.append(c)

    if len(answer) == 0:
        answer2 = -1

    else:
        answer2 = min(answer) + 1

    return answer2

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])