from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    n = (len(maps[0]))
    m = (len(maps))

    visited = [[0] * n for i in range(m)]
    lst = [[0] * n for i in range(m)]
    q = deque()
    q.append((0, 0))
    answer = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                lst[nx][ny] = lst[x][y] + 1

    if lst[m - 1][n - 1] == 0:
        answer = -1
    else:
        answer = lst[m - 1][n - 1] + 1
    return answer